from flask import Flask, render_template
import os


app = Flask(__name__)

picFolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    imageList = os.listdir('static/images')
    
    imagelist = ['images/' + image for image in imageList]
    print(imagelist)
    return render_template("test.html", imagelist=imagelist[0])


app.run()