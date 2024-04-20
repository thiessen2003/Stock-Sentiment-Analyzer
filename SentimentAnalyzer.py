import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

class SentimentAnalyzer:

    def __init__(self, text):
        self.text = text
        self.MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL)

    def evaluate_sentiment(self):
        encoded_text = self.tokenizer(self.text, return_tensors='pt')
        output = self.model(**encoded_text)
        scores = output[0][0].detach().np()
        scores = softmax(scores)
        scores_dict = {
            'roberta_neg': scores[0],
            'roberta_neu': scores[1],
            'roberta_pos': scores[2]
        }
        print(scores_dict)