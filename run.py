import urllib.parse as urlparse

from flask import Flask, request

app = Flask(__name__)


@app.route('/app', methods=["GET"])
def get_app_info():

    if not request.args.contains('app_url'):
        return "{\"error\": \"You need to specify an app_url argument\"}", 400

    app_url = request.args.get('app_url')

    try:
        parsed_app_url = urlparse.urlparse(app_url)
        app_id = urlparse.parse_qs(parsed_app_url.query)['id'][0]

    except Exception:
        return "{\"error\": \"The Playstore URL is invalid\"}", 400

