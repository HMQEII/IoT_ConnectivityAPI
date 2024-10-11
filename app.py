from flask import Flask, request, jsonify
from Adafruit_IO import Client, RequestError

# Adafruit IO credentials


# Initialize Adafruit IO Client
# aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Create Flask app
app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get JSON data from request
    data = request.json

    # Validate that the data contains the required fields
    required_fields = ['temperature', 'humidity', 'ldr_value', 'distance', 'location', 'time']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({'status': 'error', 'message': f'Missing fields: {", ".join(missing_fields)}'}), 400

    # Extract sensor data
    temperature = data['temperature']
    humidity = data['humidity']
    ldr_value = data['ldr_value']
    distance = data['distance']
    location = data['location']
    time = data['time']

    # Print received data (Optional for debugging)
    print(f"Received data: Temp={temperature}, Humidity={humidity}, LDR={ldr_value}, Distance={distance}, Location={location}, Time={time}")

    # Send data to Adafruit IO Feeds
    # try:
    #     # Ensure all feeds exist before sending data
    #     feeds = ['distance', 'humidity', 'ldr-value', 'location', 'temperature', 'time']
    #     for feed in feeds:
    #         try:
    #             aio.feeds(feed)  # Check if feed exists
    #         except RequestError:
    #             aio.create_feed(feed)  # Create feed if it doesn't exist

    #     # Send data to respective feeds
    #     # aio.send('temperature', temperature)
    #     # aio.send('humidity', humidity)
    #     # aio.send('ldr-value', ldr_value)
    #     # aio.send('distance', distance)
    #     # aio.send('location', location)
    #     # aio.send('time', time)

    # # Check if data is present, otherwise send a default value
    #     aio.send('temperature', temperature if temperature is not None else 0)
    #     aio.send('humidity', humidity if humidity is not None else 0)
    #     aio.send('ldr-value', ldr_value if ldr_value is not None else 0)
    #     aio.send('distance', distance if distance is not None else 0)
    #     aio.send('location', location if location is not None else "Unknown")
    #     aio.send('time', time if time is not None else "00:00:00")

    #     return jsonify({'status': 'success', 'message': 'Data sent to Adafruit IO successfully!'}), 200
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
