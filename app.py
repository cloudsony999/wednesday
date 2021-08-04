from flask import Flask
  
app = Flask(__name__)
  
@app.route("/")
def home():
        return "<h1>Welcome to Flask by Python running in Heroku</h1>"

if (__name__=='__main__'):
    app.run(debug=True)

    

