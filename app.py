from flask import Flask
from controllers import login_controller as lc
from flask_cors import CORS

app = Flask(__name__)

lc.route(app)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
