from fastapi import FastAPI, UploadFile, File, HTTPException
import pymupdf 
import base64

app = FastAPI()

SEPARATOR = "\n\n\n\n---"


@app.post("/parse-pdf")
async def parse_pdf(file: UploadFile = File(...)):
    #Check file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    # Read PDF
    pdf_bytes = await file.read()
    pdf_document = pymupdf.open(stream=pdf_bytes, filetype="pdf")

    images_base64 = []

    for page_index in range(len(pdf_document)):
        page = pdf_document[page_index]

        # Get images on page
        images = page.get_images(full=True)

        for image in images:
            xref = image[0]

            # Extract image bytes
            image_data = pdf_document.extract_image(xref)
            image_bytes = image_data["image"]

            # Convert to base64
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")
            images_base64.append(encoded_image)

    # Edge case
    if not images_base64:
        return ""

    # Join images with separator
    result = SEPARATOR.join(images_base64)

    return result
