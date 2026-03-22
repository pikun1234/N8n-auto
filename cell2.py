# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {'scene': '4K ultra realistic cinematic image of a cybercrime police operation in Odisha, with officers in the foreground, computers and gadgets in the midground, and a cityscape in the background, with a sense of motion and depth of field', 
     'sentences': ['ଓଡିଶା ପୋଲିସ ଅଭିଯାନ ଏକ ନିର୍ବାଚନ, ଯେଉଁଥିରେ ସାଇବର ଅପରାଧ ମାମଲାରେ ଚାରି ଜଣକୁ ଗିରଫତାର କରାଯାଇଛି', 
              'ଏହି ଅଭିଯାନ ସାଇବର ଅପରାଧକୁ ରୋକିବାରେ ଏକ ମୁଖ୍ୟ ସଫଳତା ଅର୍ଜନ କରିଛି']},
    {'scene': 'DSLR shot of a police officer explaining the operation to a group of people, with a sense of lighting and emotion, and a cityscape in the background', 
     'sentences': ['ପୋଲିସ ଅଧିକାରୀ ଏହି ଅଭିଯାନ ବିଷୟରେ ଲୋକଙ୍କୁ ଜଣାଉଛନ୍ତି, ଯେ ଏଥିରେ ଲକ୍ଷ ଲକ୍ଷ ଟଙ୍କା ଲୋକଙ୍କୁ ଠକି ଦେଉଥିବା ଲୋକଙ୍କୁ ଗିରଫତାର କରାଯାଇଛି', 
              'ଏହି ଅଭିଯାନ ଓଡିଶା ପୋଲିସର ଏକ ମୁଖ୍ୟ ସଫଳତା']},
    {'scene': 'Ultra realistic cinematic image of a person who was a victim of cybercrime, with a sense of emotion and depth of field, and a cityscape in the background', 
     'sentences': ['ସାଇବର ଅପରାଧର ଶିକାର ହୋଇଥିବା ଲୋକଙ୍କ ପାଇଁ ଏହି ଅଭିଯାନ ଏକ ନିଶ୍ଚିତ ସହାୟତା', 
              'ଏହି ଅଭିଯାନ ଓଡିଶା ପୋଲିସର ଏକ ମୁଖ୍ୟ ପଦକ୍ଷେପ']},
    {'scene': '4K ultra realistic cinematic image of a police officer helping a victim of cybercrime, with a sense of emotion and depth of field, and a cityscape in the background', 
     'sentences': ['ପୋଲିସ ଅଧିକାରୀ ସାଇବର ଅପରାଧର ଶିକାର ହୋଇଥିବା ଲୋକଙ୍କୁ ସହାୟତା କରୁଛନ୍ତି', 
              'ଏହି ଅଭିଯାନ ଓଡିଶା ପୋଲିସର ଏକ ମୁଖ୍ୟ ସଫଳତା']},
    {'scene': 'DSLR shot of a person who was a victim of cybercrime, with a sense of emotion and depth of field, and a cityscape in the background, with a message of hope and resilience', 
     'sentences': ['ସାଇବର ଅପରାଧର ଶିକାର ହୋଇଥିବା ଲୋକଙ୍କ ପାଇଁ ଏହି ଅଭିଯାନ ଏକ ନିଶ୍ଚିତ ସହାୟତା', 
              'ଆସୁନ୍ତୁ ଆମେ ଏକସାଥି ସାଇବର ଅପରାଧ ବିରୁଦ୍ଧରେ ଲଢ଼ୁଛୁ']}
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