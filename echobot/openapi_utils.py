import os

"""Return the explanation from OpenAPI for the image provided.
:param image_data: The image data to describe
:client: The OpenAPI client
:returns: The description of the image"""

def describe_image(image_data, client):
    try:
        result =  client.chat.completions.create(
            model=f"{os.environ.get('OPENAI_DEPLOYMENT_NAME')}",
                messages=[
                { "role": "system", "content": "You are a very patient childcare nurse." },
                {
                    "role": "user",
                    "content": [
                    {"type": "text", "text": "Explain to a child what's in this image. Avoid describing and listing individual elements."},
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": image_data,
                        },
                    },
                    ],
                }
                ],
                max_tokens=2000,
        )
        return result
    except Exception as e:
        print(f"error: {e}")
        return None
   