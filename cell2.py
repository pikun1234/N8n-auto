# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {'scene': 'A 4K ultra realistic shot of a hockey stadium in Rourkela, captured with a DSLR camera, under daylight, with a shallow depth of field, showing teams from various regions gathered on the field, with a mix of excitement and focus on their faces', 
     'sentences': ['୭୫ତମ ଓଡ଼ିଶା ପୁଲିଶ ହକି ଚ୍ୟାମ୍ପିୟନସିପ ୨୦୨୫-୨୬ ରାଉରକେଲାରେ ସଫଳତାର ସାଥେ ସମାପ୍ତ ହୋଇଛି', 
              'ବିଭିନ୍ନ ଅଞ୍ଚଳର ଦଳଗୁଡ଼ିକ ଏଥିରେ ଭାଗ ନେଇଛନ୍ତି']},
    {'scene': 'A high detail, realistic texture, ultra realistic visual of the championship trophy, captured with a close-up shot, using a macro lens, under emergency lights, with a high depth of field, showing the intricate design and details of the trophy', 
     'sentences': ['ଏହି ଘଟଣା ଭଲ ଭାବରେ ଆୟୋଜିତ ହୋଇଥିଲା', 
              'କାର୍ଯକ୍ରମ ସମୟ ମଧ୍ୟରେ ସମାପ୍ତ ହୋଇଥିଲା']},
    {'scene': 'A 4K cinematic shot of the hockey players in action, captured with a wide-angle lens, under daylight, with a low depth of field, showing the speed and skill of the players, with a sense of motion blur, and realistic textures of the grass and stadium', 
     'sentences': ['ରାଉରକେଲାରେ ଏହି କାର୍ଯକ୍ରମ ଅନୁଷ୍ଠିତ ହୋଇଥିଲା']}
]

flat_data = []

for scene in scenes:
    for sentence in scene['sentences']:
        flat_data.append({ 'text': sentence, 'scene': scene['scene'] })

music_keyword = 'cinematic background music'

folders = [
    'working/video_001/audio',
    'working/video_001/image',
    'working/video_001/video',
    'working/video_001/output',
    'working/video_001/raw_video',
    'working/video_001/music'
]

for f in folders:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)