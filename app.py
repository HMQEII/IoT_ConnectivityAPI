from flask import Flask, request, jsonify
import logging

# Create Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Global variable to store the last received data
last_received_data = {}

@app.route('/api/data', methods=['POST'])
def receive_data():
    global last_received_data  # Use the global variable

    # Get JSON data from request
    data = request.json

    # Validate that the data contains the required fields
    required_fields = ['temperature', 'humidity', 'ldr_value', 'distance', 'location', 'time']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({'status': 'error', 'message': f'Missing fields: {", ".join(missing_fields)}'}), 400

    # Extract sensor data with default values
    temperature = data.get('temperature', 0)
    humidity = data.get('humidity', 0)
    ldr_value = data.get('ldr_value', 0)
    distance = data.get('distance', 0)
    location = data.get('location', "Unknown")
    time = data.get('time', "00:00:00")

    # Store the received data in the global variable
    last_received_data = {
        'temperature': temperature,
        'humidity': humidity,
        'ldr_value': ldr_value,
        'distance': distance,
        'location': location,
        'time': time
    }

    # Log received data (for debugging or later use)
    logging.info(f"Received data: Temp={temperature}, Humidity={humidity}, LDR={ldr_value}, Distance={distance}, Location={location}, Time={time}")

    # Respond with success message
    return jsonify({'status': 'success', 'message': 'Data received successfully!'}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    # Return the last received data
    return jsonify(last_received_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
