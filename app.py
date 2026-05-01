from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback, score

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    strength, feedback, score = check_password(password)
    return jsonify({
        "strength": strength,
        "feedback": feedback,
        "score": score
    })

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))