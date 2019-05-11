import json
import urllib.parse as urlparse
import play_scraper

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_app_info():
    app_url = request.args.get('app_url')

    if app_url is None:
        return "{\"error\": \"You need to specify an app_url argument\"}", 400

    try:
        parsed_app_url = urlparse.urlparse(app_url)
        app_id = urlparse.parse_qs(parsed_app_url.query)['id'][0]

    except Exception:
        return "{\"error\": \"The Playstore URL is invalid\"}", 400

    app_details = play_scraper.details(app_id)

    app_json = {
        "app_id": app_details.get('app_id'),
        "title": app_details.get('title'),
        'icon': app_details.get('icon'),
        "video": app_details.get('video'),
        "price": app_details.get('price'),
        "description": app_details.get('description_html')
    }

    return str(json.dumps(app_json)), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)

