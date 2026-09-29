import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# ဒီနေရာမှာ မိမိပေးချင်တဲ့ Key များကို စာရင်းသွင်းပါ
VALID_KEYS = {
    "KAIRI CROWN": {"serial": None},
    "VIPUSER": {"serial": None}
}

@app.route('/connect', methods=['POST'])
def check_license():
    user_key = request.form.get('user_key')
    serial = request.form.get('serial')

    # Key ရှိမရှိ စစ်ဆေးခြင်း
    if user_key in VALID_KEYS:
        key_data = VALID_KEYS[user_key]
        
        # Device Serial လော့ခ်ချခြင်း (တစ်ယောက်ပဲ သုံးလို့ရအောင်)
        if key_data["serial"] is None:
            key_data["serial"] = serial
        elif key_data["serial"] != serial:
            return jsonify({"status": False, "reason": "MAX DEVICE REACHED"})

        return jsonify({"status": True, "data": {"message": "License Active"}})
    else:
        return jsonify({"status": False, "reason": "USER OR GAME NOT REGISTERED"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    