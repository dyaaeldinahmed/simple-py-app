
from flask import Flask

app = Flask(__name__)
message = "helloooo"
@app.route('/')
def hello():
    return 'Our message is {}.\n'.format(message)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
