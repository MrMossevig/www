# flask_web/app.py
from flask import Flask, render_template, request
import p_TheMathAge

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="mr.mossevig.no")

@app.route('/projects/')
def projects():
    return 'Projects Page'

@app.route('/projects/TheMathAge')
def projectPage_TheMathAge():
    return p_TheMathAge.projects_TheMathAge(request=request)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
