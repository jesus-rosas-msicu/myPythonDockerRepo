from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/ff5527c9-7a49-4d92-a00c-14610fce6e9c-0.png",
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/8323a8df-866a-40c5-b50c-81d8e7cf1a18-0.png"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
