from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin


import deneme

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/')
@cross_origin()
def hello_world():
    movie_id = int(request.args['movie_id'])
    return jsonify(deneme.get_recommendation(movie_id))





if __name__ == '__main__':
    app.run(debug=True)
