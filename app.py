from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    print("kdfnlfk")
    return jsonify({'greetings': 'Python is running'})


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')