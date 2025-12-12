from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO, emit
import time
import numpy as np

# Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage
OBJECT_DB = {} 
MAP_W, MAP_H = 400, 400  # Matched to canvas size for simplicity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detections', methods=['POST'])
def receive_detections():
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'msg': 'No JSON'}), 400
    
    updates = []
    # Process detections
    for det in data.get('detections', []):
        cls = det['class']
        conf = det['conf']
        bbox = det['bbox'] # [cx, cy, w, h] normalized
        
        # Simple mapping: Normalized Image Coords -> Map Coords
        # In a real app, this would use GPS/Altitude logic
        mx = int(bbox[0] * MAP_W) 
        my = int(bbox[1] * MAP_H)
        
        # Deduplication key (spatial hashing)
        key = f"{cls}_{mx//20}_{my//20}" 
        
        OBJECT_DB[key] = {
            'class': cls, 
            'pos': [mx, my], 
            'conf': conf, 
            'last_seen': time.time()
        }
        
        updates.append({'class': cls, 'pos': [mx, my], 'conf': conf})

    # Broadcast to dashboard
    if updates:
        socketio.emit('map_update', {'updates': updates})
        
    return jsonify({'status': 'received', 'count': len(updates)})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)