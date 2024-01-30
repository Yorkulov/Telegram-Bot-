import base64
import requests
import os

from data.config import API_KEY

url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"


async def image_generate(text_one):
    body = {
    "steps": 40,
    "width": 1024,
    "height": 1024,
    "seed": 0,
    "cfg_scale": 5,
    "samples": 1,
    "style_preset": 'photographic',
    "text_prompts": [
        {
        "text": text_one,
        "weight": 1
        },
        {
        "text": "blurry, bad",
        "weight": -1
        }
    ],
    }

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    if not os.path.exists("./out"):
        os.makedirs("./out")

    name = ""

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
            name = f'./out/txt2img_{image["seed"]}.png'
            
    return name

    # return data["artifacts"]["image"]["seed"].png

