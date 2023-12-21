import os


from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/imapp')
def imapp():
    return render_template('imapp.html')

if __name__ == '__main__':
    app.run(debug=True)
