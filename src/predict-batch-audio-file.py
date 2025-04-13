import os
import sys
CWD_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.abspath(os.path.join(CWD_PATH,'..'))
UTILS_PATH = os.path.join(ROOT_PATH,'utils')
if not UTILS_PATH in sys.path:
    sys.path.append(UTILS_PATH)
MODELS_PATH = os.path.join(ROOT_PATH,'models')
from helper import *
import glob
from tqdm import tqdm
import pandas as pd
if __name__ == "__main__":
    model, extractor = list_models(MODELS_PATH)
    audio_files_path = input("\nEnter the path of the folder containing the audio files\n")
    audio_files_path = glob.glob(os.path.join(audio_files_path,'*.wav'))+ glob.glob(os.path.join(audio_files_path,'*.mp3')) 
    results = []
    for i ,audio_file_path in tqdm(enumerate(audio_files_path)):
        print("audio")
        print(audio_file_path)
        prediction = predict(model,extractor,audio_file_path)
        result = {
            'file_name': os.path.basename(audio_file_path),
            'predicted_label': prediction
        }
        results.append(result)

    saving_path = input("\nEnter the path to save the result\n")
    saving_name = input("\nEnter the file name you want to save under it\n")
    results = pd.DataFrame(results)
    result_path = os.path.join(saving_path,f"{saving_name}.xlsx")
    results.to_excel(result_path, index=False)
    print(f"Results saved to {result_path}")