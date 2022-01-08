from flask import Flask, render_template, request, redirect, url_for
import tesserocr
#import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = './vendor/tesseract-ocr/bin/tesseract'


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print('file uploaded')
        img = Image.open(uploaded_file)
        data = tesserocr.image_to_text(img)

        res = data.split()
        aadhar_number = ''
        for word in res:
            if len(word) == 4 and word.isdigit():
                aadhar_number = aadhar_number + word + ' '
        if len(aadhar_number) >= 12:
            print("Aadhar number is :" + aadhar_number)
        else:
            print("Aadhar number not read")
        pattern1=aadhar_number

        return render_template('index.html',
                                   msg='Successfully processed',
                                   extracted_text=pattern1)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(threaded=True, debug=True)


