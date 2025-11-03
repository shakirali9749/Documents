import base64

def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        return base64_string
    except Exception as e:
        print(f"Error: {e}")
        return None

image_path = "/home/shakir/Documents/Personal-Documents/redmi 14c/Camera/IMG_20250922_200750.jpg"
base64_data = image_to_base64(image_path)

if base64_data:
    print(base64_data)