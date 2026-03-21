# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {'scene': 'A 4K ultra realistic aerial view of the Odisha River, captured with a DSLR camera, showcasing the river\'s origin in Kandmal during daylight with a shallow depth of field, highlighting the lush green surroundings and the river\'s gentle flow.', 
     'sentences': ['ଓଡ଼ିଶା ନଦୀ କାନ୍ଦମାଳ ଜିଲ୍ଲାରେ ଉତ୍ପନ୍ନ ହୋଇଛି', 'ନଦୀ ପରିଚ୍ଛନ୍ନ ନ ହୋଇ ପରିବେଶ ସମସ୍ୟାର ସମ୍ମୁଖୀନ ହୋଇଛି']},
    {'scene': 'A high detail, ultra realistic visual of recent floods in the Odisha River, captured with a wide-angle lens, showcasing the devastating impact on the surrounding environment and human settlements during low light conditions with motion blur, emphasizing the urgency of the situation.', 
     'sentences': ['ହେଲେ ଓଡ଼ିଶା ନଦୀ ବୁଡ଼ ଯୋଗୁଁ ଲୋକମାନଙ୍କ ଜୀବନ ପ୍ରଭାବିତ ହୋଇଛି', 'ଏହା ନଦୀ ପରିଚ୍ଛନ୍ନ ପାଇଁ ଉନ୍ନତ ପରିଚାଳନା ପ୍ରଯ଼ୋଜନ ତୁଲାଇଛି']},
    {'scene': 'A 4K cinematic view of government officials and environmental experts discussing and implementing initiatives to address the environmental concerns of the Odisha River, captured with a DSLR camera, showcasing a conference room with natural daylight and a shallow depth of field, highlighting the determination and cooperation among the stakeholders.', 
     'sentences': ['ସରକାର ଓଡ଼ିଶା ନଦୀର ପରିବେଶ ସମସ୍ୟା ସମାଧାନ ପାଇଁ ଉପଯୁକ୍ତ ପଦକ୍ଷେପ ନେଇଛି', 'ଏଥିପାଇଁ ସରକାର ଉଦ୍ୟମ ଜାରି କରିଛି']}
]

flat_data = []
for scene in scenes:
    for sentence in scene["sentences"]:
        flat_data.append({
            "text": sentence,
            "scene": scene["scene"]
        })

music_keyword = "cinematic background music"

folders = [
    "working/video_001/audio",
    "working/video_001/image",
    "working/video_001/video",
    "working/video_001/output",
    "working/video_001/raw_video",
    "working/video_001/music"
]

for f in folders:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
