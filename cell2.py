# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {'scene': 'A 35mm lens captures a warm, golden light-filled scene of a traditional Odia kitchen, with a large earthen pot in the foreground, a woman in the midground expertly preparing pakhala, and a blurred background of lush green trees swaying gently in the breeze, as the camera slowly zooms in on the pot.', 
     'sentences': ['ଓଡିଶାରେ ପଖାଳ ଖାଇବା ପରମ୍ପରା ରହିଛି, ଯାହା ଗ୍ରୀଷ୍ମ ଋତୁରେ ଶରୀର ଠଣା ରଖିବାକୁ ସାହାଯ୍ୟ କରେ ।', 
      'ପଖାଳ ଏକ ପାରମ୍ପରିକ ଓଡିଆ ଖାଦ୍ୟ ଯାହା ଓଡିଶାରେ ବାର୍ଷିକ ପଖାଳ ଦିବସ ପାଳନ କରାଯାଏ ।']},
    {'scene': 'A 50mm lens captures a vibrant, colorful scene of a bustling street in Odisha, with people of all ages walking in the foreground, street food stalls in the midground selling various traditional Odia dishes, and a clear blue sky in the background, as the camera pans across the scene, capturing the excitement and energy of the crowd.', 
     'sentences': ['ପଖାଳ ଦିବସ ଓଡିଶା ଆଦି ଓଡିଆ ସମ୍ପ୍ରଦାୟ ବିଶ୍ଵବ୍ୟାପୀ ଉତ୍ସାହର ସହିତ ପାଳନ କରାଯାଏ ।', 
      'ଏହି ଅନୁଷ୍ଠାନ ପାରମ୍ପରିକ ଓଡିଆ ଖାଦ୍ୟ ଏବଂ ସଂସ୍କୃତିର ଗୁରୁତ୍ଵ ଉପରେ ଜୋର ଦେଇ ।']},
    {'scene': 'A 35mm lens captures a serene, peaceful scene of a traditional Odia family sitting together, with a steaming hot bowl of pakhala in the foreground, a woman serving the dish in the midground, and a warm, cozy background of a decorated living room, as the camera slowly zooms out, capturing the love and bonding of the family.', 
     'sentences': ['ପଖାଳ ଓଡିଶାର ଏକ ଅତି ପୁରାତନ ଖାଦ୍ୟ, ଯାହା ଗ୍ରୀଷ୍ମ ଋତୁରେ ଶରୀର ଠଣା ରଖିବାକୁ ସାହାଯ୍ୟ କରେ ।', 
      'ପଖାଳ ଖାଇବା ପରମ୍ପରା ଓଡିଶାର ସଂସ୍କୃତି ଏବଂ ଐତିହ୍ୟର ଏକ ଅଙ୍ଗ ।']}]

flat_data = []

for scene in scenes:
    for sentence in scene['sentences']:
        flat_data.append({ 'text': sentence, 'scene': scene['scene'] })

music_keyword = "warm cultural traditional flute"

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