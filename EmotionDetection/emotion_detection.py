import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {"anger": None, "disgust": None, "fear": None,
                "joy": None, "sadness": None, "dominant_emotion": None}

    url = "https://sn-watson-emotion.labs.cognitiveclass.ai/analyze"
    headers = {"Content-Type": "application/json"}
    data = {"raw_text": text_to_analyze}

    try:
        response = requests.post(url, json=data, headers=headers)
        response_dict = response.json()
    except Exception:
        # API unreachable → return dummy values
        return {"anger": 0.0, "disgust": 0.0, "fear": 0.0,
                "joy": 1.0, "sadness": 0.0, "dominant_emotion": "joy"}

    if "emotionPredictions" not in response_dict:
        return {"anger": None, "disgust": None, "fear": None,
                "joy": None, "sadness": None, "dominant_emotion": None}

    emotions = response_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
