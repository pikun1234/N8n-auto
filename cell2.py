# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {'scene': 'a 4K ultra realistic cinematic shot of a traditional Odia kitchen with a large earthen pot of pakhala, with steam rising from it, and a woman in the foreground stirring the pakhala with a wooden spoon, with a blurred background of a kitchen garden', 'sentences': ['ଓଡିଶାରେ ପଖାଳ ଖାଇବା ପରମ୍ପରା ରହିଛି, ଯାହା ଗ୍ରୀଷ୍ମ ଋତୁରେ ଶରୀର ଠଣା ରଖିବାକୁ ସାହାଯ୍ୟ କରେ', 'ପଖାଳ ଏକ ପାରମ୍ପରିକ ଓଡିଆ ଖାଦ୍ୟ ଯାହା ଓଡିଶାରେ ବାର୍ଷିକ ପଖାଳ ଦିବସ ଭାବରେ ପାଳନ କରାଯାଏ']},
    {'scene': 'a 4K ultra realistic cinematic shot of a group of people from different age groups and professions gathered around a large table, with a variety of traditional Odia dishes, including pakhala, and they are all smiling and chatting while enjoying their meal', 'sentences': ['ପଖାଳ ଦିବସ ଓଡିଶାର ସାଂସ୍କୃତିକ ଐତିହ୍ୟ ଏବଂ ଖାଦ୍ୟ ପରମ୍ପରାକୁ ପ୍ରଚାର କରିବା ଲକ୍ଷ୍ୟରେ ପାଳନ କରାଯାଏ', 'ଏହି ଅନୁଷ୍ଠାନ ଓଡିଶା ଏବଂ ବିଶ୍ଵର ଓଡିଆ ସମ୍ପ୍ରଦାୟଦ୍ୱାରା ଉତ୍ସାହର ସହିତ ପାଳନ କରାଯାଏ']},
    {'scene': 'a 4K ultra realistic cinematic shot of a woman sitting in a traditional Odia setting, with a bowl of pakhala in front of her, and she is smiling while taking a bite of the pakhala, with a blurred background of a traditional Odia kitchen', 'sentences': ['ପଖାଳ ଓଡିଶାର ଏକ ଅତ୍ୟନ୍ତ ଲୋକପ୍ରିୟ ଖାଦ୍ୟ, ଯାହା ଗ୍ରୀଷ୍ମ ଋତୁରେ ଶରୀର ଠଣା ରଖିବାକୁ ସାହାଯ୍ୟ କରେ', 'ପଖାଳ ଖାଇବା ପରମ୍ପରା ଓଡିଶାର ସାଂସ୍କୃତିକ ଐତିହ୍ୟର ଏକ ଅନନ୍ୟ ଅଂଶ']},
    {'scene': 'a 4K ultra realistic cinematic shot of a group of people from different age groups and professions gathered around a large table, with a variety of traditional Odia dishes, including pakhala, and they are all smiling and chatting while enjoying their meal, with a blurred background of a traditional Odia setting', 'sentences': ['ପଖାଳ ଦିବସ ଓଡିଶାର ସାଂସ୍କୃତିକ ଐତିହ୍ୟ ଏବଂ ଖାଦ୍ୟ ପରମ୍ପରାକୁ ପ୍ରଚାର କରିବା ଲକ୍ଷ୍ୟରେ ପାଳନ କରାଯାଏ', 'ଏହି ଅନୁଷ୍ଠାନ ଓଡିଶା ଏବଂ ବିଶ୍ଵର ଓଡିଆ ସମ୍ପ୍ରଦାୟଦ୍ୱାରା ଉତ୍ସାହର ସହିତ ପାଳନ କରାଯାଏ']},
    {'scene': 'a 4K ultra realistic cinematic shot of a woman sitting in a traditional Odia setting, with a bowl of pakhala in front of her, and she is smiling while taking a bite of the pakhala, with a blurred background of a traditional Odia kitchen', 'sentences': ['ପଖାଳ ଖାଇବା ପରମ୍ପରା ଓଡିଶାର ସାଂସ୍କୃତିକ ଐତିହ୍ୟର ଏକ ଅନନ୍ୟ ଅଂଶ', 'ପଖାଳ ଏକ ପାରମ୍ପରିକ ଓଡିଆ ଖାଦ୍ୟ ଯାହା ଓଡିଶାରେ ବାର୍ଷିକ ପଖାଳ ଦିବସ ଭାବରେ ପାଳନ କରାଯାଏ']}
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