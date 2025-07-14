# BasketBall Analysis with YoloV5 Model 
- This project implements an end-to-end basketball game video analysis system using computer vision and zero-shot learning techniques. The pipeline detects and tracks players and the ball in video footage, assigns players to teams based on jersey colors using zero-shot classification (CLIP model), and generates annotated videos that visualize player movements and ball tracking.

# Key components include:

- Player and ball detection using custom YOLOv5 models
- Multi-object tracking with ByteTrack
- Team assignment through zero-shot classification with OpenAI's CLIP model
- Visualization and annotation using OpenCV
- Data cleaning and interpolation to improve tracking accuracy
- This system can be extended to perform detailed tactical analysis, event classification, and other advanced basketball analytics.

# Features
- Custom-trained YOLOv5 models for basketball player and ball detection
- ByteTrack for robust multi-object tracking
- Zero-shot team classification using jersey color and CLIP model (no need for labeled jersey data)
- Confidence filtering and interpolation to improve ball tracking accuracy
- Modular design allowing easy updates and integration of new features
- Output annotated video visualizations for easy interpretation of tracking results

# Project Structure
├── input_videos/                # Input raw game videos  
├── output_videos/               # Output annotated videos  
├── models/                     # YOLOv5 player and ball detection models  
├── stubs/                      # Cached tracking and classification results  
├── trackers/                   # Player and ball tracking modules  
├── drawers/                    # Visualization modules for drawing tracks  
├── team_assigner/              # Zero-shot team assignment using CLIP  
├── utils/                      # Helper functions like video read/write  
├── main.py                     # Entry point for running the pipeline  
└── README.md                   # This file  

# Installation and Setup:

1. Clone the repository
- git clone https://github.com/yourusername/basketballAnalysis.git
- cd basketball_analysis

2. Create and activate a Python virtual environment
- python3 -m venv venv
- source venv/bin/activate

3. Install the required Python packages
- pip install -r requirements.txt

4. Add YoloV5 Model
- Place your custom-trained YOLOv5 player and ball detection models (.pt files) inside the models/ directory.

# Usage:
Run the main analysis script: python main.py

# This will:

- Read the input video from input_videos/video_1.mp4
- Detect and track players and ball across frames
- Assign players to teams using zero-shot jersey color classification
- Draw tracked objects with team-based coloring
- Save the annotated output video to output_videos/output_video.mp4

# How It Works
- Detection: YOLOv5 models detect players and ball in each frame.
- Tracking: ByteTrack associates detections to maintain continuous tracks.
- Team Assignment: CLIP zero-shot classification assigns team IDs based on jersey color without labeled data.
- Data Processing: Filters and interpolates ball detections to reduce noise.
- Visualization: Annotated video frames show player tracks colored by team and ball tracking.

