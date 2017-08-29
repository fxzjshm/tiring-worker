try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import base64
import cStringIO

import core

@core.app.route('/ocr', methods=['POST'])
def ocr():
    print(request.headers)
    print(equest.form)
    return pytesseract.image_to_string(Image.open(cStringIO.StringIO(base64.b64decode(request.form.get('image')))))
