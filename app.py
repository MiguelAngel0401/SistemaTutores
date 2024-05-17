from flask import Flask, render_template
from views.add_register import submitForm, get_form

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/home')
def home():
    return render_template('/index.html')

@app.route('/form', methods=['GET', 'POST'])
def add_product():
    return ()

@app.route('/submit', methods=['POST'])
def submit():
    return submitForm()

@app.route('/table')
def table():
    return render_template('table.html', data=get_form())

if __name__ == '__main__':
    app.run(debug=True)
