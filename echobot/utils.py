import os
import base64

def create_directory(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print(f"Error: {error}")

def save_image(image_data, file_name):
    cwd = os.getcwd()    
    directory = f"{cwd}/public/img"
    create_directory(directory)

    if image_data:
        img_bytes = base64.b64decode(image_data)
        with open(f"{directory}/{file_name}", "wb") as img_file:
            img_file.write(img_bytes)