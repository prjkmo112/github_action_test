from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.get('/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=4344)