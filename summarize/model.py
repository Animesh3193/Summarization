from curses import nl
import nltk

from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')


def create_sentence_score(sentence_list):
    """
    Takes in a list if cleaned sentence list of text and 
    provides the sentence score of each sentence 
    """
    combined_text = " ".join(sentence_list)
    
    word_counter = Counter(nltk.word_tokenize(combined_text))
    
    stop_words_list = nltk.corpus.stopwords.words('english')
    
    for word in stop_words_list:
        if word in word_counter.keys():
            word_counter.pop(word)
            
    max_word_weight = max(word_counter.values())
    
    weighted_word_counter = {key: float(value / max_word_weight) 
                             for key, value in word_counter.items()}
    
    sentence_score = {}
    
    for sentence in sentence_list:
        for word in nltk.word_tokenize(sentence):
            if sentence not in sentence_score.keys():
                sentence_score[sentence] = weighted_word_counter.get(word, 0)
            else:
                sentence_score[sentence] += weighted_word_counter.get(word, 0)
    
    return sentence_score