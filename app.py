from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/formsubmit")
def form_submit():
    if request.method == 'POST':
        pass


if __name__ == "__main__":
    app.debug = True
    app.run()