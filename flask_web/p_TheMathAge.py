# flask_web/p_TheMathAge.py

# Adding projects to path, to be able to get models
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'projects/TheMathAge'))

from flask import Flask, url_for, render_template, request
from run_helpers import list_factions, list_units
from unit_objects import unit
import TheMathAge_combat

def projects_TheMathAge(request):
    factionlist = list_factions()
    # Attacker faction
    afaction = request.args.get('afaction')
    if (not afaction in factionlist):
        afaction = None

    # Attacker unit
    aunitlist = None
    attacker  = None

    if (afaction):
        aunitlist = list_units(afaction)
        aunit   = request.args.get('aunit')
        amodels = request.args.get('amodels')
        if (not aunit in aunitlist):
            aunit = aunitlist[0]
        if (not amodels):
            amodels = 1
        attacker = unit(XML=True, models = amodels)
        attacker.loadData(factionFileName=afaction, name=aunit)
        # attacker.employRules(['Lance','Heavy Armor','Shield','Barding','Mounts Protection (6+)'])


    # Defender faction
    dfaction = request.args.get('dfaction')
    if (not dfaction in factionlist):
        dfaction = None

    # Defender unit
    dunitlist = None
    defender  = None

    if (dfaction):
        dunitlist = list_units(dfaction)
        dunit   = request.args.get('dunit')
        dmodels = request.args.get('dmodels')
        if (not dunit in dunitlist):
            dunit = dunitlist[0]
        if (not dmodels):
            dmodels = 1
        defender = unit(XML=True, models = dmodels)
        defender.loadData(factionFileName=dfaction, name=dunit)
        # defender.employRules(['Born Predator','Innate Defence (3+)', 'Multiple Wounds (D3)']) 


    woundTotTable = []

    calculated = False

    if (request.args.get('run') == "calculate"):
        woundTotTable = TheMathAge_combat.main(attacker, defender)
        calculated = True

    return render_template('p_TheMathAge.html', 
                           title="TheMathAge",
                           factionlist=factionlist,
                           aunitlist=aunitlist,
                           a=attacker,
                           dunitlist=dunitlist,
                           d=defender,
                           result=woundTotTable,
                           calculated=calculated)
