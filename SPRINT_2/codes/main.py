from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/project')
def projeto():
    return 'projeto Y'


@app.route('/collaborators')
def collaborators():
    return 'collaborators'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
