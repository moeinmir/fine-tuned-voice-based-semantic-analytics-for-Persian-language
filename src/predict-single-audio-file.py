import os
import sys
CWD_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.abspath(os.path.join(CWD_PATH,'..'))
UTILS_PATH = os.path.join(ROOT_PATH,'utils')
if not UTILS_PATH in sys.path:
    sys.path.append(UTILS_PATH)
MODELS_PATH = os.path.join(ROOT_PATH,'models')
from helper import *

if __name__=="__main__":
    model, extractor = list_models(MODELS_PATH)
    audio_path = input("Enter the audio file path")
    prediction = predict(model,extractor,audio_path)
    print(f"The predicted label is: {prediction}")