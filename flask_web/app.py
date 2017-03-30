# flask_web/app.py

from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="mr.mossevig.no")

@app.route('/projects/')
def projects():
    return 'Projects Page'

@app.route('/projects/TheMathAge')
def projects_TheMathAge():
    return render_template('TheMathAge.html', title="TheMathAge")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
