"""Flask Web Server for Emotion Detection API.
This module provides endpoints to analyze text emotions using Watson NLP.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app=Flask(__name__)
@app.route('/emotionDetector')
def sent_detector():
    """Analyze input text and return emotion scores in JSON format.
    Returns:
        str: Formatted string containing anger, disgust, fear, joy, sadness scores 
             and dominant emotion.
    """
    text_to_analyze=request.args.get("textToAnalyze")
    response=emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
    f" 'anger': {response['anger']}, "
    f" 'disgust': {response['disgust']}, "
    f" 'fear': {response['fear']}, "
    f" 'joy': {response['joy']} and "
    f" 'sadness': {response['sadness']}. "
    f" The dominant emotion is {response['dominant_emotion']}.")
@app.route('/')
def render_index_page():
    """Render the main HTML interface.
    Returns:
        HTML: Rendered index.html template
    """
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True, port=5000, host='localhost')
