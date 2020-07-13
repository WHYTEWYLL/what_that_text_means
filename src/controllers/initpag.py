from src.app import app


@app.route("/")
def unprueba():
    return "Hello World ! "