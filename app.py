from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<noun>')
def hello_noun(noun):
    return 'Hello %s!' % noun

if __name__ == '__main__':
    app.run(debug=True)
