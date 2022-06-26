from flask import Flask, render_template, request, send_from_directory
import smtplib

user_id = "directortesting@gmail.com"
password = "shweta@492318"

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home-one.html")


@app.route("/upload/<path:filename>")
def upload_file(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == "__main__":
    app.run(debug=True)
