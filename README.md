# drone-eye
🦅 Sentinel-AI
Autonomous Edge Reconnaissance System

“The Digital Spotter That Never Blinks.”

📌 Overview

Sentinel-AI is a lightweight, real-time situational-awareness system designed for research, disaster response, border monitoring, wildlife tracking, and security automation.
It uses efficient neural networks running directly on edge hardware, enabling instant analysis without cloud dependency.

This repository contains the core inference engine, edge-processing pipeline, and modular architecture that allows the system to adapt to different mission profiles.

⚠️ Ethical Notice
This project is for educational, research, and civilian safety applications only.
It must NOT be used to cause harm, violate privacy, or perform unauthorized surveillance.

🚀 Key Features
⚡ Edge-First AI

Built on YOLOv8 Nano for ultra-fast inference.

Optimized for low-power CPUs/GPUs (Jetson, Raspberry Pi, laptops).

No cloud required → ideal for low-bandwidth or jammed environments.

👁️ Real-Time Detection

Processes live optical feeds via OpenCV.

Detects and tracks objects with high FPS.

Modular detection profiles (human, vehicle, wildlife, etc.)

🧩 Modular Threat/Asset Library

Swap model weights to change detection focus:

Personnel detection

Vehicle detection

Wildlife or environmental monitoring

Infrastructure/asset analysis

🖥️ Hardware-Agnostic Design

Runs on:

Laptops with CUDA

Jetson Nano / Orin

Raspberry Pi + NPU accelerators

Compact field computers

🛠️ Tech Stack
Layer	Technology
Core AI Engine	Ultralytics YOLOv8n
Programming Language	Python 3.12
Computer Vision	OpenCV
Acceleration	NVIDIA CUDA (optional)
Deployment	Edge devices, drones, laptops
📸 System Pipeline
Video Feed → Preprocessing → Object Detection → Tracking → Event Alerts

Capture: OpenCV video stream or onboard camera

Inference: YOLOv8 Nano (FP16 optimized)

Tracking: ByteTrack / SORT (configurable)

Event Logic: Configurable rule engine for alerts

Output: Annotated video + JSON logs

🧪 Current Prototype (Phase 1)

Real-time detection running on ground station GPU laptop

Web-cam based simulated drone feed

Human/vehicle detection with high FPS

Working end-to-end pipeline:
Frame → AI Inference → Classification → On-Screen Alerts

🔮 Roadmap (Phase 2 – In Progress)
🎯 Enhanced Classification

Training on specialized datasets (vehicles, assets, gear types)

Improved distinction across object sub-types

🚁 Aerial Integration

Deployment to lightweight autonomous platforms

Edge-only inference for offline operation

🗂️ Mission Profiles

Switch between detection modes by loading different weight files

For example: wildlife monitoring, crowd analysis, infrastructure inspection

📦 Installation
git clone https://github.com/yourname/Sentinel-AI
cd Sentinel-AI
pip install -r requirements.txt

▶️ Running the Demo
python sentinel_ai.py --source 0 --model weights/yolov8n.pt

📁 Project Structure
Sentinel-AI/
│
├── models/               # Model weights (generic or custom)
├── configs/              # Mission profiles / detection configs
├── core/
│   ├── detector.py       # YOLO inference engine
│   ├── tracker.py        # Object tracking module
│   ├── pipeline.py       # Frame → Inference → Alert logic
│
├── utils/
│   ├── visualization.py  # Bounding boxes, overlays
│   ├── logger.py         # JSON logs / event data
│
├── sentinel_ai.py        # Main entry script
└── README.md

🛡️ Ethics, Compliance & Safety

Sentinel-AI is intended for:
✔ Disaster response
✔ Wildlife protection
✔ Border safety monitoring
✔ Threat-free research and automation
✔ Civilian infrastructure safety

It must NOT be used for:
✘ Targeting or weapon guidance
✘ Harmful autonomous operations
✘ Surveillance of individuals without consent
✘ Military deployment without legal authorization

🤝 Contributing

We welcome contributions related to:

Model optimization

Edge device deployment

Dataset improvement

Ethical AI research

📜 License

Choose a license such as MIT, Apache-2.0, or CC-BY-NC depending on your goals.
For sensitive AI applications, Non-Commercial license is recommended.
