from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)

blog_url = "https://api.npoint.io/e1249369ca6c46bc8d8f"
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()

SENDER = os.environ["SENDER"]
RECEIVER = os.environ["RECEIVER"]
PASSWORD = os.environ["PASSWORD"]
EMAIL_PROVIDER = "smtp.gmail.com"


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    post_index = blog_id - 1
    return render_template("post.html", posts=all_posts, index=post_index)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        email_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        with smtplib.SMTP(EMAIL_PROVIDER) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=f"Subject: New Message\n\n{email_content}")
        header_text = "Successfully sent your message"
        return render_template("contact.html", h1_text=header_text)
    else:
        header_text = "Contact Me"
        return render_template("contact.html", h1_text=header_text)


if __name__ == "__main__":
    app.run(debug=True)