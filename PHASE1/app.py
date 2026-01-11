from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>SIMPLICITY IS KEY</h1><p>The app is finally running.</p>"

if __name__ == '__main__':
    # Runs the built-in Flask server (Easiest to debug)
    app.run(host='0.0.0.0', port=5000)