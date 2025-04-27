import requests

url = "http://localhost:5000/"
api_key = "your_api_key"
image_path = r"C:\Users\ADVAN WORKPLUS\Pictures\KTP_Mahasiswa.jpg"

headers = {
    "X-API-KEY": api_key
}

files = {
    "image": open(image_path, "rb")
}

data = {
    "ocr_choice": "easyocr"
}

response = requests.post(url, headers=headers, files=files, data=data)

print(response.json())  # Print the JSON response
