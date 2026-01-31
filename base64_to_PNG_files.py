import base64
import json

with open("C:/Users/user/Downloads/response_1769837822161.json", "r") as f:
    raw = f.read()

data = json.loads(raw)
images = data.split("\n\n\n\n---")

for i, img in enumerate(images):
    img = img.strip()
    if not img:
        continue

    with open(f"image_{i}.png", "wb") as out:
        out.write(base64.b64decode(img))

