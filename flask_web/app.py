# flask_web/app.py

from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', url=url_for('index_theWebAge'))

@app.route('/projects/')
def index_projects():
    return 'Proects Page'

@app.route('/projects/TheMathAge')
def index_theWebAge():
    return 'TheWebAge'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
