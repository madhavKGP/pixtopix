from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

from app.model import predict
from app.utils import preprocess_image, postprocess_image

app = FastAPI()

@app.post("/predict/")
async def generate_image(file: UploadFile = File(...)):
    # Load image from request
    image = Image.open(file.file).convert("RGB")
    
    # Preprocess and predict
    input_array = preprocess_image(image)
    output_array = predict(input_array)
    output_image = postprocess_image(output_array)

    # Return image as response
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
