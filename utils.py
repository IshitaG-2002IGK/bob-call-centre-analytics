from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_score(sentence):

    sentiment_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sentiment_obj.polarity_scores(sentence)

    neg_score = sentiment_dict['neg'] * 100
    pos_score = sentiment_dict['pos'] * 100
    neu_score = sentiment_dict['neu'] * 100

    # if sentiment_dict['compound'] >= 0.05 --> positive
    # if sentiment_dict['compound'] <= -0.05 --> negative
    # else sentiment_dict['compound'] >= 0.05 --> neutral

    overall_rating = sentiment_dict['compound']
    
    if overall_rating >= 0.05:

        print('positive')
    
    elif overall_rating <= -0.05:

        print ('negative')

    else:

        print('neutral')

# def sentiment_scores(sentence):

# 	sid_obj = SentimentIntensityAnalyzer()

# 	sentiment_dict = sid_obj.polarity_scores(sentence)
    
#     # neg_score = sentiment_dict['neg']*100



	
# 	# print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
# 	# print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
# 	# print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

# 	print("Sentence Overall Rated As", end = " ")

# 	# decide sentiment as positive, negative and neutral
# 	if sentiment_dict['compound'] >= 0.05 :
# 		print("Positive")

# 	elif sentiment_dict['compound'] <= - 0.05 :
# 		print("Negative")

# 	else :
# 		print("Neutral")

def start():

    sentence_1 = 'this is a masterpiece'
    sentence_2 = 'we have school tomorrow'
    sentence_3 = 'the food was horrible'

    get_sentiment_score(sentence_1)
    get_sentiment_score(sentence_2)
    get_sentiment_score(sentence_3)



# Driver code
if __name__ == "__main__" :

    start()

