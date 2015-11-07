from flask import Flask, render_template, request, redirect

import twitter

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('/app')


@app.route("/app", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        topic = request.form['searchtopic']
        results = twitter.twit_search(topic)

        return render_template('home.html', result=results)

    return render_template('home.html')


if __name__ == "__main__":
    app.debug = True
    app.run()