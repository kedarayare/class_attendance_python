from flask import Flask, jsonify
from flask import request
import face_recog as fr


app = Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def index():
#     data = request.files['images']
#     data.save('kedar.jpeg')
#     print(data)
#     print("kdfnlfk")
#     return jsonify({'greetings': 'lksvlkn'})
@app.route('/',methods=['GET','POST'])
def index():
    print("kdfnlfk")
    return jsonify({"greetings": "Thank God"})

# @app.route('/face_recog/',methods=['GET','POST'])
# def index2():
#     data = request.files['images']
#     data.save('received.jpeg')
#     name = fr.face_recog('group.jpeg')
#     print(name)
#     # return jsonify({'name':name})
    

if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0')


