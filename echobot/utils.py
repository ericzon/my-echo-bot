import os
import base64

def create_directory(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print(f"Error: {error}")

def save_image(image_data, folder_name, file_name):
    cwd = os.getcwd()    
    directory = f"{cwd}/{folder_name}"
    create_directory(directory)

    imageCleaned = image_data.replace("data:image/png;base64,", "")
    if imageCleaned:
        img_bytes = base64.b64decode(imageCleaned)
        with open(f"{directory}/{file_name}", "wb") as img_file:
            img_file.write(img_bytes)