import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
import tflearn
import random
import pickle
import nltk
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']


with open('pengetahuan.json') as json_data:
    pengetahuan = json.load(json_data)


# deepneuralnet
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model dan setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    # stem dengan sastrawi
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("tersimpan di bag: %s" % w)

    return(np.array(bag))

p = bow("is your shop open today?", words)
#print (p)
#print (classes)



# load model yang disimpan
model.load('./model.tflearn')

# membuat struktur dari inputan konteks user
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilitas dari model
    results = model.predict([bow(sentence, words)])[0]
    # filter out prediksi dibawah threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # mengurutkan by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # mengembalikan tuple dari pengetahuan dan probabilitas
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in pengetahuan['pengetahuan']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        return print(random.choice(i['responses']))

            results.pop(0)
