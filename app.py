from flask import Flask, request, jsonify

app = Flask(__name__)

def get_highest_alphabet(alphabets):
    sorted_alphabets = sorted(alphabets, key=lambda x: x.upper())
    return sorted_alphabets[-1] if sorted_alphabets else None

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        
        # Extract and categorize data
        numbers = [item for item in data.get('data', []) if item.isdigit()]
        alphabets = [item for item in data.get('data', []) if item.isalpha()]
        
        # Determine the highest alphabet
        highest_alphabet = get_highest_alphabet(alphabets)
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
