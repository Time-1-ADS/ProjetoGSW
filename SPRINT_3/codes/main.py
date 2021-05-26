from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)

#TODO modularizar

# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/project')
# def projeto():
#     return render_template('projetoY.html')


# @app.route('/collaborators')
# def collaborators():
#     return render_template('colaboradores.html')


# @app.route('/task')
# def tasks():
#     return render_template('Tasks.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
