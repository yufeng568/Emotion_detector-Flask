import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        text1="I am glad this happened"
        text2="I am really mad about this"
        text3="I feel disgusted just hearing about this"
        text4="I am so sad about this"
        text5="I am really afraid that this will happen"
        result1=emotion_detector(text1)
        self.assertEqual(result1['dominant_emotion'], "joy")
        result2=emotion_detector(text2)
        self.assertEqual(result2['dominant_emotion'], "anger")
        result3=emotion_detector(text3)
        self.assertEqual(result3['dominant_emotion'], "disgust")
        result4=emotion_detector(text4)
        self.assertEqual(result4['dominant_emotion'], "sadness")
        result5=emotion_detector(text5)
        self.assertEqual(result5['dominant_emotion'], "fear")

if __name__=="__main__":
    unittest.main