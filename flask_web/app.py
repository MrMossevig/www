# flask_web/app.py

from flask import Flask, url_for, render_template, request
from projects.TheMathAge import run_helpers
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="mr.mossevig.no")

@app.route('/projects/')
def projects():
    return 'Projects Page'

@app.route('/projects/TheMathAge')
def projects_TheMathAge():
    faction = request.args.get('faction')
    factionlist = run_helpers.list_factions()
    if (not faction in factionlist):
        faction = None

    unitlist = None
    unit = None
    models = None

    if (faction):
        unitlist = run_helpers.list_units(faction)
        unit   = request.args.get('unit')
        models = request.args.get('models')
        if (not unit in unitlist):
            unit = None

    return render_template('TheMathAge.html', 
                           title="TheMathAge",
                           faction=faction,
                           factionlist=factionlist,
                           unit=unit,
                           unitlist=unitlist,
                           models=models)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
