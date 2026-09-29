import os
from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_KEYS = {
    "KAIRI CROWN": {"serial": None},
    "VIPUSER": {"serial": None}
}

@app.route('/connect', methods=['POST'])
@app.route('/api/connect', methods=['POST'])
def check_license():
    user_key = request.form.get('user_key')
    serial = request.form.get('serial')

    if user_key in VALID_KEYS:
        key_data = VALID_KEYS[user_key]
        if key_data["serial"] is None:
            key_data["serial"] = serial
        elif key_data["serial"] != serial:
            return jsonify({"status": False, "reason": "MAX DEVICE REACHED"})

        return jsonify({"status": True, "data": {"message": "License Active"}})
    else:
        return jsonify({"status": False, "reason": "USER OR GAME NOT REGISTERED"})

def handler(request, response):
    return app(request, response)
      
