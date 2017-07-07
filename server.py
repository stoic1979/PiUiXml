from flask import Flask, render_template

from data import get_vapes, get_syringes, get_accessories, get_concentrates, \
    get_other, get_cat, get_satvia_first, get_satvia_second


app = Flask(__name__)


@app.route("/prerolls")
def prerolls():

    templateData = {'title': 'Home Page', 'first': get_satvia_first(),
                    'second': get_satvia_second()}
    return render_template("prerolls.html", **templateData)


@app.route("/extracts")
def extracts():

    vapes = []

    templateData = {'title': 'Home Page', 'vapes': get_vapes(),
                    'syringes': get_syringes(),
                    'accessories': get_accessories(),
                    'concentrates': get_concentrates(),
                    'other': get_other(),
                    'cat': get_cat()}
    return render_template("extracts.html", **templateData)


@app.route("/premium")
def premium():
    templateData = {'title': 'Home Page'}
    return render_template("premium.html", **templateData)

if __name__ == '__main__':
    app.run(debug=True)
