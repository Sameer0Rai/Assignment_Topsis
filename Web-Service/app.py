from flask import Flask, render_template, request
from topsis_logic import run_topsis
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

EMAIL_ADDRESS = "samkr2340005@gmail.com"
EMAIL_PASSWORD = "lpnskizyykatuhfr"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"].split(",")
        impacts = request.form["impacts"].split(",")
        email = request.form["email"]

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

        file.save(input_path)

        run_topsis(input_path, weights, impacts, output_path)

        msg = EmailMessage()
        msg["Subject"] = "TOPSIS Result"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email
        msg.set_content("Please find the TOPSIS result attached.")

        with open(output_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename="result.csv"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return "Result sent to email successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
