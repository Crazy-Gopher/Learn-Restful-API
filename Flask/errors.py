from app import app

@app.errorhandler(422)
@app.errorhandler(400)
def handle_validation_error(err):
    exc = getattr(err, "exc", None)
    if exc:
        headers = err.data["headers"]
        messages = exc.messages
    else:
        headers = None
        messages = ["Invalid request."]
    if headers:
        return {"errors": messages}, err.code, headers
    else:
        return {"errors": messages}, err.code
