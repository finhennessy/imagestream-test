import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello from Source-to-Image! I've changed since you were last here!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    application.run(host="0.0.0.0", port=port)
