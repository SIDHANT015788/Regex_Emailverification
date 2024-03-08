from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    regex = re.compile(regex_pattern)
    matches = regex.findall(test_string)
    return render_template('index.html', matches=matches)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        
        regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        if regex.match(email):
            return render_template('validate_email.html', result="Valid Email")
        else:
            return render_template('validate_email.html', result="Invalid Email")
    return render_template('validate_email.html')

if __name__ == '__main__':
    app.run(debug=True)
