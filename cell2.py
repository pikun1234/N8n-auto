# ==========================================
# 🟨 CELL 2: AUTO GENERATED NEWS SCRIPT
# ==========================================

import os
import shutil

BASE = "/content/drive/MyDrive/AI_VIDEO_SYSTEM"

scenes = [
    {'scene': 'A 4K ultra realistic shot of a gas station at dawn, with a DSLR camera capturing the scene from a low angle, depth of field focusing on the gas pumps, and motion blur from passing vehicles, as people wait in line to fill their tanks', 
     'sentences': ['ଓଡ଼ିଶା ସରକାର ଗ୍ୟাস ସରବରାହ ନିଶ୍ଚିତ କରିବା ପାଇଁ ଅତ୍ୟାବଶ୍ୟକ ଦ୍ରବ୍ୟ ଆଇନ ଲାଗୁ କରିଛି', 
      'ଏହି ପଦକ୍ଷେପ କଳା ବଜାର ପ୍ରତିରୋଧ ଏବଂ ଅତ୍ୟାବଶ୍ୟକ ସେବା ନିଶ୍ଚିତ କରିବାର ଲକ୍ଷ୍ୟ ରଖିଛି']},
    {'scene': 'A high detail, realistic texture, 4K cinematic shot of a news conference at a government office, with a DSLR camera positioned at a 45-degree angle, capturing the speaker and the audience, under daylight with soft natural lighting', 
     'sentences': ['ଏହି ଆଇନ ଅତ୍ୟାବଶ୍ୟକ ସେବା ଏବଂ ଦ୍ରବ୍ୟ ଉପଲବ୍ଧତା ବଜାୟ ରଖିବାରେ ସାହାଯ୍ୟ କରେ', 
      'ବିଶ୍ୱ ତେଲ ମୂଲ୍ୟ ବୃଦ୍ଧି ପରିପ୍ରେକ୍ଷିତେ ଏହି ପଦକ୍ଷେପ ନିଅାଯାଇଛି']},
    {'scene': 'A 4K ultra realistic visual of a person reading a newspaper with a headline about the Essential Commodities Act, shot with a DSLR camera, using a shallow depth of field to blur the background, under low light with a single emergency light source', 
     'sentences': ['ଅତ୍ୟାବଶ୍ୟକ ଦ୍ରବ୍ୟ ଆଇନ ଲାଗୁ କରିବା ଦ୍ଵାରା ସରକାର ଗ୍ୟାସ ସରବରାହ ନିଶ୍ଚିତ କରିଛି', 
      'ଏହି ଆଇନ କଳା ବଜାର ପ୍ରତିରୋଧ କରିବାରେ ସାହାଯ୍ୟ କରିବ']}
]

# Standard Validation and Folder Clean
total_sentences = sum(len(s['sentences']) for s in scenes)
print(f"✅ Loaded Script: {len(scenes)} Scenes and {total_sentences} Sentences.")
print(f"⏱️ Estimated Duration: {(total_sentences * 6.5) / 60:.2f} Minutes.")

folders = [
    "working/video_001/audio",
    "working/video_001/image",
    "working/video_001/video",
    "working/video_001/output",
    "working/video_001/raw_video"
]

for f in folders:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)

print("✅ Folders cleaned and ready for production!")
