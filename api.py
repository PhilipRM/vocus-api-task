from flask import Flask, request
import json
import phonenumbers
app = Flask(__name__)

@app.route("/")
def index():
    return ""

@app.route("/api/validate")
def validate():
    number = request.args.get('number')
    if number is None:
        valid = False
    else:
        try:
            parsed = phonenumbers.parse(number,"NZ")
            valid = phonenumbers.is_valid_number(parsed)
        except Exception as e:
            valid = False

    return json.dumps({"valid": valid})

if __name__ == "__main__":
    app.run()
