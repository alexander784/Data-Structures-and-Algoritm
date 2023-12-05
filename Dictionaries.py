import string

def word_frequency(sentence):
    sentence =sentence.translate(str.maketrans('','', string.punctuation))
##split sentence into words.
    words = sentence.split()
    ##Count frequency of each word
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1


        return frequency_dict

