from flask import Flask,render_template,request
import requests

app=Flask(__name__)
l=[]
@app.route("/",methods=["POST","GET"])
def fun():
    temp=""
    if request.form.get("input")!=None:
        i=request.form.get("input")
        url="https://api.mfapi.in/mf/"+i
        resp=requests.get(url)
        temp=resp.json()
        code=temp.get("meta").get("scheme_code")
        house=temp.get("meta").get("fund_house")
        nav=temp.get("data")[0].get("nav")
        dict={"scheme_code":code,"fund_house":house,"nav":nav}
        l.append(dict)
    return render_template ("index.html",data=l)

l=[]
@app.route("/api",methods=["POST","GET"])
def fun1():
    i=request.json.get("input")
    url="https://api.mfapi.in/mf/"+str(i)
    resp=requests.get(url)
    temp=resp.json()
    code=temp.get("meta").get("scheme_code")
    code=temp.get("meta").get("scheme_code")
    house=temp.get("meta").get("fund_house")
    nav=temp.get("data")[0].get("nav")
    dict={"scheme_code":code,"fund_house":house,"nav":nav}
    l.append(dict)
    return l


if __name__ == "__main__":
    app.run(debug=True)
    