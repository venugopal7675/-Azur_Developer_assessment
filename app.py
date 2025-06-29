from flask import Flask, request, jsonify
from utils import load_events, save_events

app = Flask(__name__)
events = load_events()

# Create an event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    try:
        event = {
            "id": str(len(events) + 1),
            "title": data['title'],
            "description": data['description'],
            "start_time": data['start_time'],
            "end_time": data['end_time']
        }
        events.append(event)
        save_events(events)
        return jsonify(event), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400

# List events
@app.route('/events', methods=['GET'])
def list_events():
    sorted_events = sorted(events, key=lambda x: x['start_time'])
    return jsonify(sorted_events), 200

# Update event
@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    for event in events:
        if event['id'] == event_id:
            event.update(data)
            save_events(events)
            return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404

# Delete event
@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    events = [event for event in events if event['id'] != event_id]
    save_events(events)
    return jsonify({"message": "Event deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
