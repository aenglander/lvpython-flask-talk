from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'bfc0af8d0d0dbd6fa9b7d8533b933277'

def hello_world():
    return render_template('index.html', say='Hello World!')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<noun>')
def hello_noun(noun='World'):
    return render_template('hello.html', say=noun)

@app.route('/form', methods=['GET'])
def form_show():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form_post():
    flash(request.form['say'])
    return redirect(url_for('form_show'));

if __name__ == '__main__':
    app.run(debug=True)
