from flask import Flask, render_template

# Creating a new application
app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

def run_debug(host=None, debug=True, user=None, port=5000):
    app.debug = debug
    app.run(host=host, port=port)

