from flask import Flask
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# helper function
# query 


@app.route('/')
def index():
    html = "<html><body><h1>Homepage here!</h1></body></html>"
    return html


if __name__ == "__main__":
    app.debug = True

    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
