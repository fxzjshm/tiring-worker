from flask import Flask, request, render_template
from flask_script import Manager

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import base64
import cStringIO

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def test():
    return 'Hello but I will make you tired ...'

@app.route('/ocr', methods=['POST'])
def ocr():
    return pytesseract.image_to_string(Image.open(cStringIO.StringIO(base64.b64decode(request.data))))

@app.route('/ocr', methods=['GET'])
def ocrUI():
    return render_template('ocr.html')


if __name__ == "__main__":
    manager.run()
