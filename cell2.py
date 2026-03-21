# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {'scene': 'A 4K ultra realistic shot of a busy street in the morning with low light, captured using a DSLR camera with a shallow depth of field, showing child beggars on the street with a mix of emotions on their faces, while people walk by with a sense of urgency', 
     'sentences': ['ଓଡିଶା ରାଜ୍ୟ ଶିଶୁ ଅଧିକାର ସୁରକ୍ଷା ଆୟୋଗ ରାସ୍ତାରୁ ଶିଶୁ ଭିକାରୀଙ୍କୁ ଅପସାରଣ କରିବା ପାଇଁ ନିର୍ଦେଶ ଜାରୀ କରିଛି', 
      'ଏଥିରେ ପୁନର୍ବାସ ଓ ଅପମାନକ ବିରୁଦ୍ଧରେ ଆଇନଗତ କାର୍ଯ୍ୟ କରାଯିବ']}, 
    {'scene': 'A high detail, ultra realistic visual of a care center in the daytime with natural light, captured using a wide-angle lens, showing rescued children engaging in educational activities with a sense of hope and rehabilitation', 
     'sentences': ['ଉଦ୍ଧାର କରାଯାଇଥିବା ଶିଶୁମାନଙ୍କୁ ଯତ୍ନ କେନ୍ଦ୍ରରେ ରଖାଯିବ', 
      'ସେମାନଙ୍କୁ ଶିକ୍ଷା ଓ ପରାମର୍ଶ ଦିଆଯିବ']}, 
    {'scene': 'A 4K cinematic shot of a city location at night with emergency lights, captured using a DSLR camera with a high shutter speed, showing authorities taking immediate action against child exploitation', 
     'sentences': ['ବିଭିନ୍ନ ସହର ସ୍ଥାନରେ ତତ୍କ୍ଷଣାତ କାର୍ଯ୍ୟ କରାଯିବ', 
      'ଶୋଷଣକାରୀଙ୍କ ବିରୁଦ୍ଧରେ ଆଇନଗତ କାର୍ଯ୍ୟ କରାଯିବ']}
]

flat_data = []

for scene in scenes:
    for sentence in scene['sentences']:
        flat_data.append({
            'text': sentence,
            'scene': scene['scene']
        })

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