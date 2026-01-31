# PDF Image Extraction Microservice

## Overview
This project is a lightweight REST microservice built with **FastAPI**.
It accepts a PDF file, extracts all embedded images, converts them to base64,
and returns them in a single response separated by a predefined delimiter.

## API Endpoint

### POST /parse-pdf

**Request**
- Content-Type: `multipart/form-data`
- Body:
  - `file` — PDF file

**Response**
- `200 OK`
- Plain text response
- Base64-encoded images separated by:

\n\n\n\n---

### I also added **Base64 to PNG Converter**, may be if you need it:
- base64_to_PNG_files.py

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
