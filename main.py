from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    category = request.form.get("category")
    print(category)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)