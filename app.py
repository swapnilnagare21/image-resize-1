#Import necessary packages
from flask import Flask
from flask_restful import Resource, reqparse, Api
import requests
import cStringIO
import base64
from io import BytesIO
from PIL import Image

#Instantiate a flask object 
app = Flask(__name__)
#Instantiate Api object
api = Api(app)

#app.app_context().push()



class ResizeImage(Resource):
    def get(self, posterPath):        
        imgbbKey = '7560011cb554421936fd80696b850a18'

        requiredWidth = 500;
        requiredHeight = 750;
        
        baseUrl = "https://image.tmdb.org/t/p/w500/"
        


        #titleNames = ["The Dark Knight"]
        #imageIds = ["https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"]


        imageUrl = baseUrl + str(posterPath)
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
        return uploadedImageJson


#Adding the URIs to the api
api.add_resource(ResizeImage, '/<string:movie>')

if __name__=='__main__':        
    #Run the applications
    app.run()
