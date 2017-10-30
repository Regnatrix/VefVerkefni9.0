from bottle import run,route,template,redirect
import urllib.request, json
with urllib.request.urlopen("http://apis.is/concerts") as url:
    data = json.loads(url.read().decode())

    dataind = json.dumps(data)



@route('/')
def index():
    return template("index.tpl" ,dataind = dataind)


run(host="localhost",port=8080,debug=True,reloader=True)