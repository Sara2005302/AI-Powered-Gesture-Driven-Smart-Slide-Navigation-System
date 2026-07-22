# AI-Powered Gesture-Driven Smart Slide Navigation System

> A computer vision–based presentation control system that enables touch-free slide navigation using real-time hand gesture recognition.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Overview

The AI-Powered Gesture-Driven Smart Slide Navigation System is designed to eliminate the need for traditional presentation devices such as keyboards, mice, or clickers. By leveraging computer vision and machine learning techniques, the system recognizes predefined hand gestures through a webcam and translates them into presentation control commands.

The application enables presenters to navigate slides, annotate content, erase annotations, and control an on-screen pointer in real time, providing a seamless and contactless presentation experience.

---

## Key Features

- Real-time hand gesture detection
- Next and Previous slide navigation
- Virtual laser pointer
- Slide annotation using finger gestures
- Annotation erase functionality
- Touch-free presentation control
- Fast and responsive gesture recognition
- Simple and intuitive user interaction

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Numerical Computing | NumPy |

---

## Project Architecture

```
User Hand Gesture
        │
        ▼
 Webcam Frame Capture
        │
        ▼
 MediaPipe Hand Detection
        │
        ▼
 Gesture Recognition
        │
        ▼
 Command Processing
        │
        ▼
 Slide Navigation / Annotation / Pointer Control
```

---

## Repository Structure

```
AI-Powered-Gesture-Driven-Smart-Slide-Navigation-System
│
├── Images/
├── modules/
├── docs/
│   ├── Final_Report.pdf
│   └── Final_Presentation.pptx
│
├── main.py
├── HandTracker.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Sara2005302/AI-Powered-Gesture-Driven-Smart-Slide-Navigation-System.git
```

Navigate to the project directory

```bash
cd AI-Powered-Gesture-Driven-Smart-Slide-Navigation-System
```

Create a virtual environment

```bash
python -m venv gesture_env
```

Activate the environment

Windows

```bash
gesture_env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

## Workflow

1. Launch the application.
2. Position your hand within the webcam frame.
3. Perform predefined gestures.
4. The system recognizes the gesture.
5. The corresponding presentation action is executed instantly.

---

## Applications

- Smart Classrooms
- Online Teaching
- Technical Presentations
- Business Meetings
- Conferences
- Interactive Demonstrations

---

## Documentation

Project documentation is available in the `docs` directory.

- Final Project Report
- Final Project Presentation

---

## Future Enhancements

- Multi-hand gesture support
- Custom gesture configuration
- Voice-assisted presentation control
- Cross-platform deployment
- Gesture personalization
- AI-based gesture learning

---

## Author

**Sara**

Bachelor of Engineering  
Information Science & Engineering

---

## License

This project is licensed under the MIT License.
