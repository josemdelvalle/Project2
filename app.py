from flask import Flask
from controllers import front_controller as lc, product_controller as pc, orders_controller as oc, \
    product_cart_controller as pcc
from flask_cors import CORS

app = Flask(__name__)

lc.route(app)
pc.route(app)
oc.route(app)
pcc.route(app)

CORS(app, supports_credentials=True)

# app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == '__main__':
    app.run(debug=True)
