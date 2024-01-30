import base64
import os
import requests

from data.config import API_KEY

async def image_update(image_path):        
    response = requests.post(
        "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        files={
            "init_image": open(image_path, "rb")
        },
        data={
            "init_image_mode": "IMAGE_STRENGTH",
            "image_strength": 0.35,
            "steps": 40,
            "width": 1024,
            "height": 1024,
            "seed": 0,
            "cfg_scale": 5,
            "samples": 1,
            "text_prompts[0][text]": 'A painting of a cat',
            "text_prompts[0][weight]": 1,
            "text_prompts[1][text]": 'blurry, bad',
            "text_prompts[1][weight]": -1,
        }
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # make sure the out directory exists
    if not os.path.exists("./input"):
        os.makedirs("./input")

    for i, image in enumerate(data["artifacts"]):
        with open(f'./input/img2img_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
            name = f'./input/txt2img_{image["seed"]}.png'

    return name