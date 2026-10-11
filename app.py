from flask import Flask, render_template, request, redirect 
import json
import os
app = Flask(__name__)
DATA_FILE = "application.json"
def load_applications():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    return []
@app.route("/", methods=["GET", "POST"])
def home():
    applications = load_applications()
    if request.method == "POST":
        application = request.form.to_dict()
        applications.append(application)
        with open(DATA_FILE, "w") as file:
            json.dump(applications, file, indent=4)
            return redirect("/")
    return render_template("index.html", applications=applications)
if __name__ == "__main__":
    app.run(debug=True)
