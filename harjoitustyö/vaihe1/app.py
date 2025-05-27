from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():

    # alla oleva rivi vaihtaa työhakemistoksi tämän koodin hakemiston
    # se varmistaa että index.html löytyy jos koodin käynnistää vscodella
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('index.html', 'r') as file:
        html_content = file.read()
    formatted_html = html_content.format(body="<h1>Hello Wordl!</h1>")
    return render_template_string(formatted_html)

if __name__ == '__main__':
    app.run(debug=True)