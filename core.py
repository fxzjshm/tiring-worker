from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def test():
    return 'Hello but I am so tired ...'

if __name__ == "__main__":
    manager.run()
