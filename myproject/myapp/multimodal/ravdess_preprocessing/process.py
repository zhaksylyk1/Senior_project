# -*- coding: utf-8 -*-
import os
import numpy as np          
import cv2
from tqdm import tqdm
import torch
import soundfile as sf
from facenet_pytorch import MTCNN
import librosa
import matplotlib.pyplot as plt
import librosa.display
from moviepy.editor import VideoFileClip
from create_annotations import create_annotations

device = torch.device('cuda') if torch.cuda.is_available() else 'cpu'
mtcnn = MTCNN(image_size=(720, 1280), device=device)
# root = 'c:/Users/zhk27/OneDrive/Рабочий стол/em_video'
target_time=3.6
save_avi = True

def extract_audio_from_video(video_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(os.path.join(video_path[:-4]+'.wav'))

def split_audio(start_frame, fps,root):
    for audiofile in os.listdir(root):
        if not audiofile.endswith('.wav') or 'croppad' in audiofile:
            continue

        audio_path = os.path.join(root, audiofile)
        y, sr = librosa.core.load(audio_path, sr=22050)

        # Calculate the starting and ending sample indices
        start_sample = int((start_frame / fps) * sr)
        end_sample = int(start_sample + (target_time * sr))

        # Ensure end_sample does not exceed the length of y
        end_sample = min(end_sample, len(y))

        # If start_sample is greater than the length of y, skip this file
        if start_sample >= len(y):
            print(f"Skipping {audiofile}: start frame is beyond audio duration.")
            continue

        # Extract the desired clip
        y_clip = y[start_sample:end_sample]

        # If the extracted clip is shorter than target_time, pad it with zeros
        if len(y_clip) < target_time * sr:
            y_clip = np.pad(y_clip, (0, int(target_time * sr) - len(y_clip)), 'constant')

        # Save the processed clip
        sf.write(audio_path[:-4] +"_"+str(start_frame)+ '_croppad.wav', y_clip, sr)

def extract_fa(root):
    for filename in os.listdir(root):
        if filename.endswith('.mp4'):
            cap = cv2.VideoCapture(os.path.join(root,filename))  
            fps = cap.get(cv2.CAP_PROP_FPS)
            framen = 0
            while True:
                i,q = cap.read()
                if not i:
                    break
                framen += 1
            cap = cv2.VideoCapture(os.path.join(root,filename))
            extract_audio_from_video(os.path.join(root,filename))
            all_frames_to_select=[i for i in range(1,framen,7)]
            for cri in range(0,len(all_frames_to_select),5):
                if cri+15>len(all_frames_to_select):
                    break
                frames_to_select=all_frames_to_select[cri:cri+15]
                numpy_video = []
                frame_ctr = 0

                while True: 
                    ret, im = cap.read()
                    if not ret:
                        break
                    if frame_ctr not in frames_to_select:
                        frame_ctr += 1
                        continue
                    else:
                        frames_to_select.remove(frame_ctr)
                        frame_ctr += 1

                    try:
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    except:
                        break
                    temp = im[:,:,-1]
                    im_rgb = im.copy()
                    im_rgb[:,:,-1] = im_rgb[:,:,0]
                    im_rgb[:,:,0] = temp
                    im_rgb = torch.tensor(im_rgb)
                    im_rgb = im_rgb.to(device)

                    bbox = mtcnn.detect(im_rgb)
                    if bbox[0] is not None:
                        bbox = bbox[0][0]
                        bbox = [round(x) for x in bbox]
                        x1, y1, x2, y2 = bbox
                        im = im[y1:y2, x1:x2, :]
                        im = cv2.resize(im, (224,224))
                        numpy_video.append(im)
                if len(frames_to_select) > 0:
                    for i in range(len(frames_to_select)):
                        numpy_video.append(np.zeros((224,224,3), dtype=np.uint8))
                np.save(os.path.join(root,filename[:-4]+"_"+str(all_frames_to_select[cri])+'_facecroppad.npy'), np.array(numpy_video))
                if len(numpy_video) != 15:
                    print('Error', root, filename)   
                    
                split_audio(all_frames_to_select[cri], fps,root)
    create_annotations(root)
                
                


                    
            


        
        
