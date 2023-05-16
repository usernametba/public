import json
from flask import Flask, request
from kiteconnect import KiteConnect

import datetime
import json

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

# Base settings
PORT = 5010
HOST = "127.0.0.1"

# Kite Connect App settings. Go to https://developers.kite.trade/apps/
# to create an app if you don't have one.
kite_api_key = "xxxxxxxxxxxxxxxxxxxxx"
kite_api_secret = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

# Create a redirect url
redirect_url = "http://{host}:{port}/login".format(host=HOST, port=PORT)

# Login url
login_url = "https://api.kite.trade/connect/login?api_key={api_key}".format(api_key=kite_api_key)

# Kite connect console url
console_url = "https://developers.kite.trade/apps/{api_key}".format(api_key=kite_api_key)

# App
app = Flask(__name__)

# Templates
index_template = """
    <div>Make sure your app with api_key - <b>{api_key}</b> has set redirect to <b>{redirect_url}</b>.</div>
    <div>If not you can set it from your <a href="{console_url}">Kite Connect developer console here</a>.</div>
    <a href="{login_url}"><h1>Login to generate access token.</h1></a>"""

login_template = """
    <h2 style="color: green">Success</h2>
    <div>Access token: <b>{access_token}</b></div>
    <h4>User login data</h4>
    <pre>{user_data}</pre>
    <a target="_blank" href="{holdings_url}"><h4>Fetch user holdings</h4></a>
    <a target="_blank" href="{orders_url}"><h4>Fetch user orders</h4></a>
    <a target="_blank" href="https://kite.trade/docs/connect/v1/"><h4>Checks Kite Connect docs for other calls.</h4></a>"""


@app.route("/")
def index():
    return index_template.format(api_key=kite_api_key,
                                redirect_url=redirect_url,
                                console_url=console_url,
                                login_url=login_url)


@app.route("/login")
def login():
    request_token = request.args.get("request_token")

    if not request_token:
        return """
            <span style="color: red">Error while generating request token.</span><a href='/'>
            Try again.<a>"""

    kite = KiteConnect(api_key=kite_api_key)
    data = kite.generate_session(request_token, api_secret="zzzzzzzzzzzzzzzzzzzzzzzzzzz")
    kite.set_access_token(data["access_token"])
    #data = kite.request_access_token(request_token, secret=kite_api_secret) # This was not working for some reason
    holdings_url = ("https://api.kite.trade/portfolio/holdings?api_key={api_key}&access_token={access_token}").format(api_key=kite_api_key,access_token=data["access_token"])
    orders_url = ("https://api.kite.trade/orders?api_key={api_key}&access_token={access_token}").format(api_key=kite_api_key,access_token=data["access_token"])

    return login_template.format(access_token=data["access_token"],
                                user_data=json.dumps(data, sort_keys=True, indent=4, default=datetime_handler),
                                holdings_url=holdings_url,
                                orders_url=orders_url)

if __name__ == "__main__":
    print("Starting server: http://{host}:{port}".format(host=HOST, port=PORT))
    app.run(host=HOST, port=PORT, debug=True)
