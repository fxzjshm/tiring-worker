from flask import Flask, request
from flask_script import Manager

import ocr


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def test():
    return 'Hello but I will make you tired ...'

if __name__ == "__main__":
    manager.run()
