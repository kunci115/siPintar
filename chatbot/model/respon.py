import os
import sys
from django.conf import settings
import numpy as np
import tflearn
import random
import pickle
import nltk
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
sys.path.append('/home/kunci115/PycharmProjects/skripsi/siPintar')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","siPintar.settings")
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

factory = StemmerFactory()
stemmer = factory.create_stemmer()
training_file = os.path.join(settings.BASE_DIR, 'chatbot/model/'+'training_data')
data = pickle.load(open(training_file, "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

pengetahuan = os.path.join(settings.BASE_DIR, 'chatbot/model/'+'pengetahuan.json')

with open(pengetahuan) as json_data:
    pengetahuan = json.load(json_data)


# deepneuralnet
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model dan setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("test : %s" % w)
    return(np.array(bag))

# load model yang disimpan
load_model = os.path.join(settings.BASE_DIR, 'chatbot/model/'+'./model.tflearn')
model.load(load_model)

context = {}

ERROR_THRESHOLD = 0.25

def classify(sentence):
    results = model.predict([bow(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))

    return return_list

def response(sentence, userID='kunci115', show_details=False):
    results = classify(sentence)

    if results:
        while results:
            for i in pengetahuan['pengetahuan']:
                if i['tag'] == results[0][0]:
                    if 'context_set' in i:
                        if show_details:
                            print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details:
                            print ('tag:', i['tag'])
                        return random.choice(i['responses'])

            results.pop(0)