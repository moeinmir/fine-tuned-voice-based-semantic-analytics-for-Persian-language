import glob
import os
import librosa
from transformers import AutoFeatureExtractor, Wav2Vec2ForSequenceClassification
import torch

def list_models(models_paths):
    models_paths = glob.glob(os.path.join(models_paths,'*'))
    if not models_paths:
        print("NO MODELS EXIST")
    for i, model_path in enumerate(models_paths):
        print(f"{i+1}.{model_path}")
    choice = int(input("\nChoose a model (Enter the number)")) -1
    model_path = models_paths[choice-1]
    print("here is model path")
    print(model_path)
    model = Wav2Vec2ForSequenceClassification.from_pretrained(model_path)
    extractor = AutoFeatureExtractor.from_pretrained(model_path)
    return model, extractor


def predict(model, extractor, audio_path,duration = 8, sample_rate = 16000):
    audio, _ = librosa.load(audio_path, sr=sample_rate, duration=duration)
    inputs = extractor(audio, sampling_rate=sample_rate, return_tensors="pt")
    id2label = model.config.id2label
    with torch.no_grad():
        logits = model(**inputs).logits
    return id2label[torch.argmax(logits).item()]

