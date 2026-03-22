# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {
        'scene': 'A 4K, ultra-realistic, daytime shot with a slight zoom, captured using a DSLR camera, showing a veterinarian in a livestock farm in Odisha, with a depth of field emphasizing the interaction between the veterinarian and the animals, set against a backdrop of green pastures and farm buildings under a clear blue sky with a few white clouds, conveying a sense of hope and improvement in the animal husbandry sector.',
        'sentences': ['ଓଡ଼ିଶା ତାର ପଶୁ ସମ୍ପଦ କ୍ଷେତ୍ରକୁ ଉନ୍ନତ କରିବା ପାଇଁ ପାଞ୍ଚ ବର୍ଷିଆ ବିନିଯୋଗ ଯୋଜନା ଉପର ଜୋର ଦେଇଛି।', 'ଏଥିରେ ପଶୁ ସ୍ୱାସ୍ଥ୍ୟ ଓ ଉତ୍ପାଦନଶୀଳତା ଉନ୍ନତ କରିବା ପାଇଁ ଫୋକସ କରାଯାଉଛି।']
    },
    {
        'scene': 'A high-detail, 4K, ultra-realistic visual of a vaccination drive in progress, with a motion blur hinting at the movement of the veterinarians and the animals, captured in a slight low-light condition using a DSLR camera, emphasizing the depth of field to highlight the vaccination process, set in a bustling farm environment with animals and farm workers in the foreground and background.',
        'sentences': ['ରାଜ୍ୟରେ ଉଲ୍ଲେଖନୀୟ ଟିକାକରଣ କଭରେଜ ଦେଖାଯାଇଛି।', 'ପଶୁ ସ୍ୱାସ୍ଥ୍ୟ ଉନ୍ନତ କରିବା ପାଇଁ ନବୀନ ଅଭ୍ୟାସ ଗ୍ରହଣ କରାଯାଉଛି।']
    },
    {
        'scene': 'An inspirational, 4K, ultra-realistic shot of a farmer in Odisha, with a slight pan to the right, showcasing the farmer's interaction with the livestock, captured using a DSLR camera, emphasizing the depth of field to highlight the farmer's smile and the healthy animals, set against a backdrop of a thriving farm with lush greenery and clear blue sky, conveying a sense of prosperity and success in the animal husbandry sector.',
        'sentences': ['ସରକାର ଆର୍ଥିକ ଆର୍ଥିକ ଲାଭ ବୃଦ୍ଧି କରିବା ଏବଂ ପଶୁ ସମ୍ପଦ କ୍ଷେତ୍ରରେ ବୈଜ୍ଞାନିକ ଅଭ୍ୟାସ ପ୍ରଚାର କରିବା ପାଇଁ ଉଦ୍ୟୋଗ ସମର୍ଥନ କରୁଛି।']
    }
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