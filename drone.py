from ultralytics import YOLO
import cv2
import requests
import time

# Config
SERVER_URL = "http://10.177.64.81:5000/detections"
SEND_RATE = 0.2  # Send data every 0.2 seconds (5Hz)

def run_drone():
    # Load model (auto-downloads on first run)
    model = YOLO("yolov8n.pt") 
    
    
    # 0 = Webcam, or replace with 'video.mp4'
    cap = cv2.VideoCapture(0) 
    
    last_send_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        # Run inference
        results = model(frame, verbose=False)
        
        # Prepare payload
        detections = []
        for r in results:
            for box in r.boxes:
                # Get normalized coordinates [cx, cy, w, h]
                # xywhn returns normalized center-x, center-y, width, height
                b = box.xywhn[0].tolist() 
                cls = model.names[int(box.cls[0])]
                conf = float(box.conf[0])
                
                if conf > 0.5: # Confidence threshold
                    detections.append({
                        "class": cls,
                        "bbox": b,
                        "conf": round(conf, 2)
                    })

        # Visualization (Local View)
        annotated_frame = results[0].plot()
        cv2.imshow("Drone View (Local)", annotated_frame)

        # Send Data (Throttled)
        if time.time() - last_send_time > SEND_RATE:
            if detections:
                try:
                    payload = {"detections": detections}
                    requests.post(SERVER_URL, json=payload, timeout=0.1)
                    print(f"📡 Sent {len(detections)} targets")
                except:
                    print("⚠️ Server unreachable")
            last_send_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_drone()