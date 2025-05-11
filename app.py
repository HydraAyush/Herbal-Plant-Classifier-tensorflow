from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

new_model = load_model('model_inception.h5')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", data = "YO hoo")

@app.route("/prediction", methods=["POST"])
def predicition():
    img = request.files['img']

    img.save("img.jpg")
    return "Welcome to the prediction"

if __name__ == "__main__":
    app.run(debug=True)