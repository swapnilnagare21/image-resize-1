import base64
import requests
import cStringIO
from io import BytesIO
from PIL import Image

imgbbKey = '7560011cb554421936fd80696b850a18'

requiredWidth = 500;
requiredHeight = 750;


titleNames = ["The Dark Knight"]
imageIds = ["https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"]


imageUrl = imageIds[0]
img_data = requests.get(imageUrl).content

image = Image.open(BytesIO(img_data))
resizedImage = image.resize((requiredWidth,requiredHeight), Image.NEAREST)



buffered = cStringIO.StringIO()
resizedImage.save(buffered, format="JPEG")
#img_str = base64.b64encode(buffered.getvalue())


url = "https://api.imgbb.com/1/upload"

payload = {
    "key": imgbbKey,
    "image": base64.b64encode(buffered.getvalue()),
    "expiration": 300,
}
res = requests.post(url, payload)

uploadedImageJson = res.json()

#print(uploadedImageJson.keys())
print(uploadedImageJson['data']['image']['url'])