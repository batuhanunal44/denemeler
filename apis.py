from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///datalar.db"

class Nots(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    isim = db.Column(db.String())
    notu = db.Column(db.Integer())
    durum = db.Column(db.String())
db.create_all()

@app.route("/notgir",methods=["POST"])
def notgir():
    yeninot=Nots(isim=request.json["isim"],notu=request.json["notu"],durum=request.json["durum"])
    db.session.add(yeninot)
    db.session.commit()
    return "basariyla eklendi"

@app.route("/notsil/<id>",methods=["DELETE"])
def notsil(id):
    sil = Nots.query.get(id)
    db.session.delete(sil)
    db.session.commit()
    return "basariyla silindi"
@app.route("/notgor/")
def view():
    notlar = Nots.query.all()
    g=[]
    for i in notlar:
        a= {"isim:": i.isim,"not:":i.notu,"durum":i.durum}
        g.append(a)
    return jsonify(g) 

app.run(debug=True)



