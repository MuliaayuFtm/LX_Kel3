from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


MONGODB_CONNECTION_STRING = 'mongodb://niksondinarfranselasihombing18:niksondinarfranselasihombing18@ac-zvfqymp-shard-00-00.tekjg64.mongodb.net:27017,ac-zvfqymp-shard-00-01.tekjg64.mongodb.net:27017,ac-zvfqymp-shard-00-02.tekjg64.mongodb.net:27017/?ssl=true&replicaSet=atlas-731qa5-shard-0&authSource=admin&retryWrites=true&w=majority'
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.finalproject

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


users_collection = db["users"]


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Proses otentikasi pengguna
        user = users_collection.find_one({"email": email, "password": password})

        if user:
            # login sukses
            return render_template("About.html")
        else:
            # login gagal
            return "Email atau password salah"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # periksa apakah user sudah terdaftar
        existing_user = users_collection.find_one({"email": email})

        if existing_user:
            # jika sudah terdaftar maka
            return "Email sudah terdaftar"

        # add user baru
        users_collection.insert_one(
            {"name": name, "email": email, "password": password}
        )

        # jika registrasi sukses maka
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/halaman admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Proses otentikasi pengguna
        user = users_collection.find_one({"email": email, "password": password})

        if user:
            # login sukses
            return render_template("halaman admin.html")
        else:
            # login gagal
            return "Email atau password salah"

    return render_template("login admin.html")



@app.route("/Destinasi")
def Destinasi():
    return render_template("Destinasi.html")


@app.route("/reservasi")
def reservasi():
    return render_template("reservasi.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/contact us")
def contact():
    return render_template("contact us.html")


@app.route("/chek harga")
def chek():
    return render_template("chek harga.html")

@app.route("/home")
def main():
    return render_template("home.html")

@app.route("/pemesanan")
def pemesanan():
    return render_template("pemesanan.html")


@app.route("/layout")
def layout():
    return render_template("layout.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
