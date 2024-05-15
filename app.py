from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/store_data": {"origins": "*"}})
# CORS(app)

DATA_FILE = 'data.csv'
@app.route('/store_data', methods=['POST'])
@cross_origin()
def store_data():
    try:
        if request.is_json:
            data = request.get_json()
            if not ('user_email' in data and 'Hiscore' in data):
                return jsonify({'error': 'Missing required keys: username, highScore'}), 400

            username = data['user_email']
            high_score = data['Hiscore']
            
            with open(DATA_FILE, 'a') as f:
                f.write(f"{username},{high_score}\n")

            return jsonify({'message': 'Data stored successfully!'}), 201
        else:
            return jsonify({'error': 'Request content type must be application/json'}), 415
    except Exception as e:
        print(f"Error storing data: {e}")
        return jsonify({'error': 'An error occurred while storing data'}), 500

if __name__ == '__main__':
    app.run(debug=False)  
