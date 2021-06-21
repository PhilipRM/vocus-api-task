from flask import Flask, request
import json
import phonenumbers
app = Flask(__name__)

@app.route("/")
def index():
    return ""

def is_valid_number(number):
    if number is None:
        return False
    try:
        formatted = "+" + number.strip()
        parsed = phonenumbers.parse(formatted, None)
        validity = phonenumbers.is_valid_number(parsed)
    except Exception as e:
        return False
    return validity

@app.route("/api/validate")
def validate():
    number = request.args.get('number')
    validity = is_valid_number(number)
    return json.dumps({"valid": validity})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
