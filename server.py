"""This module emotion detector"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

"""This route for emotion detector"""
@app.route("/emotionDetector")
def emotion_analyzer():
    """This method for emotion detector"""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return "For the given statement, the system response is "\
        f" 'anger': {response['anger']},"\
        f" 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}" \
        f" and 'sadness': {response['sadness']}."\
        f"The dominant emotion is {response['dominant_emotion']}"


@app.route("/")
def render_index_page():
    """This method for default page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
