from flask import Flask, render_template, request
app = Flask(__name__,template_folder="template")

@app.route("/")
def home():
     return render_template('home.html')
 
@app.route("/about")
def about():
     return render_template('about.html')

@app.route("/login")
def login():
     return render_template('login.html')

@app.route("/register")
def register():
     return render_template('register.html')

@app.route("/reservasi")
def reservasi():
     return render_template('reservasi.html')
 
 
 
if __name__ == "__main__":
     app.run(debug=True ,port=8080,use_reloader=False)




