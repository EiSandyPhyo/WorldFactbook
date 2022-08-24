import re
from flask import Flask,render_template,request
import json

w = json.load(open("worldl.json"))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", allCountries = w)

@app.route("/country/<n>")
def country(n):
    return render_template("country.html", country=w[int(n)])

@app.route("/continent/<cont>")
def continent(cont):
    ret = [c for c in w if c['continent']==cont]
    return render_template(
        "index.html",
        allCountries = ret
        )

@app.route('/api/country/<name>')
def apicountry(name):
    ret= [c for c in w if c['name']==name]
    return {"result":ret}  
    
@app.route("/api/continentList")
def continentList():
    clist=list(set([c['continent'] for c in w]))
    clist.sort()
    return {"list":clist}

@app.route("/api/getListOfCountries/<cont>")
def getListOfCountries(cont):
    ret = [c['name'] for c in w if c['continent'] == cont ]
    return{"result":ret}

@app.route("/search")
def search():
    target = request.args.get('target')
    found = [x['id'] for x in w if x['name']==target]
    if len(found)>0:
        return country(found[0])
    else:
        return f"Could not find {target}"

app.run(debug=True)