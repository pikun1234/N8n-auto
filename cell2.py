# -*- coding: utf-8 -*-
import os
import shutil

BASE = os.getcwd()

scenes = [
    {
        'scene': 'A 4K, ultra-realistic, daytime shot with a slight zoom, captured using a DSLR camera, showing a bustling industrial area in Odisha with steel and mining equipment in the foreground, workers in the midground, and a clear blue sky in the background, emphasizing the growth in the steel and mining sectors.',
        'sentences': ['ଓଡ଼ିଶାର ଶିଳ୍ପ କ୍ଷେତ୍ର ଇସ୍ପାତ ଓ ଖଣିଜ କ୍ଷେତ୍ରରେ ଉଲ୍ଲେଖନୀୟ ବୃଦ୍ଧି ପାଇଛି।', 
                 'ଏହି ବୃଦ୍ଧି ରାଜ୍ୟର ଅର୍ଥନୈତିକ ଉନ୍ନତିରେ ଗୁରୁତ୍ଵପୂର୍ଣ୍ଣ ଭୂମିକା ପାଲନ କରିଛି।']
    },
    {
        'scene': 'A high-detail, ultra-realistic visual of a renewable energy farm in Odisha, with wind turbines and solar panels in the foreground, and a vast, open landscape in the background, captured during a sunny day with a slight motion blur to convey activity, using a DSLR camera with a wide-angle lens.',
        'sentences': ['ନବୀକରଣୀୟ ଶକ୍ତି କ୍ଷେତ୍ରରେ ମଧ୍ୟ ଓଡ଼ିଶା ଉଲ୍ଲେଖନୀୟ ଅଗ୍ରଗତି କରିଛି।', 
                 'ଏହି ପ୍ରୟାସ ପରିବେଶ ସୁରକ୍ଷା ଏବଂ ଶକ୍ତି ସୁରକ୍ଷାର ଦିଗରେ ଏକ ମହତ୍ଵପୂର୍ଣ୍ଣ ପଦକ୍ଷେପ।']
    },
    {
        'scene': 'A 4K, cinematic shot of a meeting between investors and government officials in Odisha, discussing infrastructure and technology investments, with a shallow depth of field to focus on the speakers, and a professional background to convey a sense of importance, captured with a DSLR camera and a standard zoom lens.',
        'sentences': ['ଓଡ଼ିଶା ସରକାର ପ୍ରତ୍ୟକ୍ଷ ଓ ପরୋକ୍ଷ ନିବେଶ ଆକର୍ଷଣ କରିବା ପାଇଁ ଏକ ନିର୍ଦ୍ଦିଷ୍ଟ ଶିଳ୍ପ ନୀତି ଅନୁସରଣ କରୁଛି।', 
                 'ଏହି ନୀତି ମାଧ୍ୟମରେ ରାଜ୍ୟ ଅଧିକ ନିବେଶ ଆକର୍ଷଣ କରି ଅର୍ଥନୈତିକ ବୃଦ୍ଧି ହାର ବଢାଇବାର ଲକ୍ଷ୍ୟ ରଖିଛି।']
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