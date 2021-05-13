from flask import Flask, jsonify
from flask import request
import face_recog as fr


app = Flask(__name__)

<<<<<<< HEAD
# @app.route('/',methods=['GET','POST'])
# def index():
#     data = request.files['images']
#     data.save('kedar.jpeg')
#     print(data)
#     print("kdfnlfk")
#     return jsonify({'greetings': 'lksvlkn'})
=======
@app.route('/',methods=['GET'])
def index():
    print("kdfnlfk")
    return jsonify({"greetings": "Thank God"})
>>>>>>> f6df8fee7600983f6d43b0a696dd0870fc5a55ff

@app.route('/face_recog/',methods=['GET','POST'])
def index2():
    data = request.files['images']
    data.save('received.jpeg')
    name = fr.face_recog('group.jpeg')
    print(name)
    # return jsonify({'name':name})
    

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True,host='0.0.0.0')
=======
    app.run(debug=False,host='0.0.0.0')
>>>>>>> f6df8fee7600983f6d43b0a696dd0870fc5a55ff
