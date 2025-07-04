from flask import Flask, request, render_template, jsonify
from resume_generator import generate_resume_and_cover
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    print("Received data from form:", data)
    resume, cover = generate_resume_and_cover(data)
    return jsonify({"resume": resume, "cover_letter": cover})

if __name__ == "__main__":
    app.run(debug=True)
