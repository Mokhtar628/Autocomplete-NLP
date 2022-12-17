def get_propability_of_specific_word(word, current_token, unigram, bigram, vocabulary_size, k=1.0):
    
    current_token = tuple(current_token)

    current_token_count = unigram[current_token] if current_token in unigram else 0
    
    denominator = current_token_count + k * vocabulary_size

    n_plus1_gram = current_token + (word,)
  
    n_plus1_gram_count = bigram[n_plus1_gram] if n_plus1_gram in bigram else 0
        
    numerator = n_plus1_gram_count + k

    probability = numerator / denominator
    
    return probability

from operator import itemgetter
def get_propability_of_all_words(current_token, unigram, bigram, vocabulary, k=1.0):
   
    current_token = tuple(current_token)
    vocabulary = vocabulary + ["", ""]
    vocabulary_size = len(vocabulary)
    
    probabilities = {}
    for word in vocabulary:
        probability = get_propability_of_specific_word(word, current_token, 
                                           unigram, bigram, 
                                           vocabulary_size, k=k)
        probabilities[word] = probability
    #dict(list(probabilities.items())[:3])
    return dict(sorted(probabilities.items(), key = itemgetter(1), reverse = True)[:10])
