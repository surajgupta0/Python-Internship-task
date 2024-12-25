from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_text = request.form["user_text"]
        if user_text.strip():
            blob = TextBlob(user_text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            result = {
                "text": user_text,
                "sentiment": sentiment,
                "polarity": round(polarity, 2),
                "subjectivity": round(subjectivity, 2),
            }
        else:
            result = {"error": "Please enter valid text."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
