from application import app

@app.route("/")
@app.route("/index")
def index():
    return "<h1>hello everybody</h1>"