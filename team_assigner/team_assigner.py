from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import cv2
import sys 
sys.path.append('../')
from utils.stubs_utils import read_stub, save_stub

class TeamAssigner:
  def __init__(self,
               team_1_class_name="basketball player wearing white jersey",
               team_2_class_name="basketball player wearing dark blue jersey"):
    
    self.team_1_class_name=team_1_class_name
    self.team_2_class_name=team_2_class_name

    # self.team_colors = {}
    self.player_team_dict = {}

  def load_model(self):
        
          self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
          self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
  
  def get_player_color(self,frame,bbox):
      image = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]

      # Convert to PIL Image
      rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      pil_image = Image.fromarray(rgb_image)
      # image = pil_image

      classes = [self.team_1_class_name, self.team_2_class_name]

      inputs = self.processor(text=classes, images=pil_image, return_tensors="pt", padding=True)

      outputs = self.model(**inputs)
      logits_per_image = outputs.logits_per_image
      probs = logits_per_image.softmax(dim=1) 


      class_name=  classes[probs.argmax(dim=1)[0]]
      # print("Predicted probs:", probs)
      # print("Predicted class:", class_name)

      return class_name
  
    
  def get_player_team(self,frame,player_bbox,player_id):
       
        if player_id in self.player_team_dict:
          return self.player_team_dict[player_id]

        player_color = self.get_player_color(frame,player_bbox)

        team_id=2
        if self.team_1_class_name.lower() in player_color.lower():
          team_id = 1

        self.player_team_dict[int(player_id)] = team_id
        return team_id
  
  def get_player_teams_across_frames(self,video_frames,player_tracks,read_from_stub=False, stub_path=None):
      
        
        player_assignment = read_stub(read_from_stub,stub_path)
        if player_assignment is not None:
            if len(player_assignment) == len(video_frames):
                return player_assignment

        self.load_model()

        player_assignment=[]
        for frame_num, player_track in enumerate(player_tracks):        
            player_assignment.append({})
            
            if frame_num%50 ==0:
                self.player_team_dict = {}

            for player_id, track in player_track.items():
                team = self.get_player_team(video_frames[frame_num],   
                                                    track["bbox"],
                                                    player_id)
                player_assignment[frame_num][player_id] = team
        
        save_stub(stub_path,player_assignment)

        return player_assignment

  