from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
FILE_PATH = "static\\voti.txt"

# Funzione per leggere i voti dal file
def leggi_voti():
    try:
        with open(FILE_PATH, "r") as file:
            print("ciao")
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        return []

# Funzione per salvare un voto nel file
def salva_voto(professore, voto):
    with open(FILE_PATH, "a") as file:
        file.write(f"{professore},{voto}\n")

@app.route("/")
def index():
    voti = leggi_voti()
    return render_template("index.html", voti=voti)

@app.route("/aggiungi", methods=["POST"])
def aggiungi():
    professore = request.form["professore"]
    voto = request.form["voto"]
    if professore and voto:
        salva_voto(professore, voto)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
