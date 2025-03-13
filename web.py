from bottle import Bottle, route, run, template, static_file, post, request
import webbrowser
from remover import RemovePII
import sys

def StartWebserver():
    webbrowser.open("http://localhost:1986/", )
    app = Bottle()
    run(host="localhost", port=1986)
    exit(0)


@route("/")
def landing():
    return static_file("index.html", "static")

@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root='static')

@post("/PII")
def processPII():
    data = request.json

    fullText = data["text"]
    fullText = RemovePII(fullText)

    response = {
        "text": fullText
    }
    return response


@post("/kill")
def kill():
    print("Terminated via page closed")
    sys.stderr.close()
    