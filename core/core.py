import requests
from PIL import Image
from io import BytesIO
import time

ESP32_IP = "http://192.168.1.38"   # <-- đổi thành IP của ESP32

url = f"http://192.168.1.38/capture"

count = 0

while True:
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))

            filename = f"image_{count}.jpg"
            img.save(filename)

            print(f"Saved {filename}")

            count += 1

        else:
            print("HTTP Error:", response.status_code)

    except Exception as e:
        print(e)

    time.sleep(1)