from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        student_id = request.form['student_id']
        major = request.form['major']
        group = request.form['group']
        professor = request.form['professor']
        documents = request.files.getlist('documents')

        # Procesar los documentos entregables
        if documents:
            documents_info = [f.filename for f in documents]
        else:
            documents_info = ['No reportado']

        return render_template('submission.html', name=name, email=email, student_id=student_id,
                               major=major, group=group, professor=professor, documents=documents_info)

if __name__ == '__main__':
    app.run(debug=True)
