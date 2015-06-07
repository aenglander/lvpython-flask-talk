from flask import Flask, render_template
app = Flask(__name__)

def hello_world():
    return render_template('index.html', say='Hello World!')

@app.route('/')
@app.route('/hello/<noun>')
def hello_noun(noun='World'):
    return render_template('index.html', say=noun)

if __name__ == '__main__':
    app.run(debug=True)
