import requests, json
from flask import Flask,render_template,request


app=Flask(__name__)

def fonksiyon(takim):

    url = "https://fibakodtest/FibaCollection/{}/_apis/release/definitions/2?api-version=5.0".format(takim)

    payload = ""
    headers = {
    'Authorization': 'Basic OjNxcjZ5Z20yb3F4MnppcWszc2sybm93NWlsaWM2MnhmYmc1ZmJleHptZ2Vhb2VlbXc1N3E='
    }

    response = requests.request("GET", url, headers=headers, data=payload,verify=False)

    b=response.json()

    a = (b["variables"])
    return a

@app.route("/listele",methods=["GET","POST"])
def getVariables():
    ## team = request.form["team"]
    fonksiyon()
    ## print(team)
    return render_template("index.html",liste=fonksiyon())

@app.route("/",methods=["GET"])
def home():
    return render_template("form.html")

@app.route("/deneme",methods=["POST"])
def deneme():
    a = request.form["team"]
    fonksiyon(a)
    return render_template("index.html",liste=fonksiyon(a))
    
    
app.run(debug=True)


