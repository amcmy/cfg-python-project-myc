#from flask import Flask

#app = Flask(__name__)

#@app.route("/") #decorator
#def say_hello():
#  return "hello world!"

#app.run(debug=True) #automatic restart itself GREAT FOR WEB DEVELOPMENT

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

app.run(debug=True)