#BasketBall Analysis with Yolo V5 Model
- This project implements an end-to-end basketball game video analysis system using computer vision and zero-shot learning techniques. The pipeline detects and tracks players and the ball in video footage, assigns players to teams based on jersey colors using zero-shot classification (CLIP model), and generates annotated videos that visualize player movements and ball tracking.

#Key components include:

-Player and ball detection using custom YOLOv5 models
-Multi-object tracking with ByteTrack
-Team assignment through zero-shot classification with OpenAI's CLIP model
-Visualization and annotation using OpenCV
-Data cleaning and interpolation to improve tracking accuracy
-This system can be extended to perform detailed tactical analysis, event classification, and other advanced basketball analytics.

#Features
-Custom-trained YOLOv5 models for basketball player and ball detection
-ByteTrack for robust multi-object tracking
-Zero-shot team classification using jersey color and CLIP model (no need for labeled jersey data)
-Confidence filtering and interpolation to improve ball tracking accuracy
-Modular design allowing easy updates and integration of new features
-Output annotated video visualizations for easy interpretation of tracking results

