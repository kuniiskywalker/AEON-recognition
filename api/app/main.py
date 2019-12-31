from typing import List

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from PIL import Image
import io
import json

from fastapi import FastAPI, File, UploadFile
from starlette.responses import HTMLResponse

IMAGE_SIZE = 224 # 画像サイズ
MODEL_FILE_PATH = '/app/vgg16_transfer.h5' # モデルファイル

model = load_model(MODEL_FILE_PATH)

with open('/app/stores.json') as f:
    classes = json.load(f)

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: bytes = File(...)):

    image = Image.open(io.BytesIO(file))
    image = image.convert("RGB")
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    data = np.asarray(image) / 255.0
    X = []
    X.append(data)
    X = np.array(X)

    result = model.predict([X])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)

    return classes[predicted], percentage

@app.get("/")
async def main():
    content = """ 
<!doctype html>
<html lang="ja">
<head>
<!-- Required meta tags -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<title>AEON Appearance Predict AI App</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">AEON Appearance Predict AI App </a>
    </nav>
    <div class="container">
        <h4 class="mt-4 mb-5 border-bottom">Predict</h4>
        <p>Select an image file and click on the predict button</p>
        
        <form id="my_form" action="/files/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <button type="button" class="btn btn-primary" onclick="file_upload()">Predict</button>
        </form>
        
        <div class="js-predict-result">
            <h4 class="mt-4 mb-5 border-bottom">Predict Result</h4>
            <table class='table'>
                <tbody>
                    <tr>
                        <td>image file name</td>
                        <td class="js-image-name"></td>
                        </tr>
                    <tr>
                    <tr>
                        <td>image file size</td>
                        <td class="js-image-size"></td>
                        </tr>
                    <tr>
                    <tr>
                        <td>image preview</td>
                        <td class="js-image-preview"></td>
                        </tr>
                    <tr>
                        <td>predict label</td>
                        <td class="js-label"></td>
                    </tr>
                    <tr>
                        <td>predict score</td>
                        <td class="js-score"></td>
                    </tr>
                </tbody>
            </table>
        </div>
        
    </div>
<script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script>
function file_upload()
{ 
    var formdata = new FormData(); 
    if($('input[name="files"]').val()){
      let file = $('input[name="files"]')[0].files[0];
      
      const fileReader = new FileReader();
      fileReader.readAsDataURL( file );
      fileReader.onload = function( event ) {
          const base64 = this.result.split(',')[1];
          
          $('.js-predict-result .js-image-name').text(file.name);
          $('.js-predict-result .js-image-size').text(file.size);
          
          const img = $("<img />").attr({src: "data:" + file.type +  ";base64," + base64})
          $('.js-predict-result .js-image-preview').html(img);
      };

      formdata.append('file', file);
    }

    $.ajax({
        url  : "/uploadfile/",
        type : "POST",
        dataType:"json", 
        data : formdata,
        cache       : false,
        contentType : false,
        processData : false
    })
    .done(function(data, textStatus, jqXHR){
        console.log(data);
		
        $('.js-predict-result .js-label').text(data[0]);
        $('.js-predict-result .js-score').text(data[1]);
    })
    .fail(function(jqXHR, textStatus, errorThrown){
        console.log("fail");
        alert('Server Error!');
    })
    .always(function(data){
        console.log("complete")
    });
}
</script>
</body>
</html>
    """
    return HTMLResponse(content=content)
