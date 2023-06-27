from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    """
    Renders Home Page
    """

    return render_template("home.html")

@app.route("/ping", methods=["GET"])
def ping():
    """
    Route to ping current flask app

    args: None
    returns: App Status
    """

    response = {"success": True, "msg": "Ping Successful", "data": []}

    return response, 200

if __name__ == "__main__":
    app.run(debug=True)