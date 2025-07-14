from utils.video_utils import read_video, save_video
from trackers.player_tracker import PlayerTracker
from trackers.ball_tracker import BallTracker
from drawers.player_tracks_drawer import(
  PlayerTracksDrawer
  
)
from drawers.ball_tracks_drawer import(
  BallTracksDrawer
  
)
from team_assigner.team_assigner import TeamAssigner
from ball_acquisition.ball_acquisition_detector import BallAquisitionDetector
def main():
  #read the video 1
  video_frames = read_video("input_videos/video_1.mp4")
  #Initialize the tracker
  player_tracker = PlayerTracker("models/player_detector.pt")
  ball_tracker = BallTracker("models/ball_detector.pt")
  #Run trackers
  player_tracks = player_tracker.get_object_tracks(video_frames,
                                                   read_from_stub=True,     stub_path="stubs/player_track_status.pkl")
  #Ball Tracker
 
  ball_tracks = ball_tracker.get_object_tracks(video_frames,
                                               read_from_stub=True,
                                               stub_path="stubs/ball_track_stubs.pkl")
  
   #Remove wrong ball detections
  ball_tracks = ball_tracker.remove_wrong_detections(ball_tracks)
  #Interpolate ball tracks
  ball_tracks=ball_tracker.interpolate_ball_positions(ball_tracks)

  #Assign player teams
  team_assigner = TeamAssigner()
  player_assignment = team_assigner.get_player_teams_across_frames(video_frames,
                                                              player_tracks,
                                                              read_from_stub=True,
                                                              stub_path="stubs/player_assignment_stub.pkl")
 
  # print(player_assignment)
  # print(player_teams)
  #Ball Acquisition
  ball_acquisition_detector=BallAquisitionDetector()
  ball_acquisition=ball_acquisition_detector.detect_ball_possession(player_tracks,ball_tracks)
  print(ball_acquisition)
  #Draw Output
  #Initialize drawers
  player_tracks_drawer = PlayerTracksDrawer()
  ball_tracks_drawer = BallTracksDrawer()

 

  #Draw Object Tracks
  output_video_frames=player_tracks_drawer.draw(video_frames,player_tracks,player_assignment, ball_acquisition)
  output_video_frames=ball_tracks_drawer.draw(output_video_frames,ball_tracks)
  #save the video
  save_video(output_video_frames, "output_videos/output_video.mp4")

if __name__ == "__main__":
  main()
