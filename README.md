### Chatbot Deep Neural Network for Bahasa Indonesia ###

siPintar, Indonesian Chatbot Deep Neural Network
======
**siPintar** is an indonesian chatbot built with NLP technique combine with MLP algorithm
for your business need. 
Built with multi layer perceptron and you can customize with your own datasets.

#### Screenshot
![Screenshot software](https://github.com/kunci115/siPintar/blob/master/ss1.png)
![alt text](https://github.com/kunci115/siPintar/blob/master/ss2.png)
## Usage
```
If you want to train with your own datasets, checkout pengetahuan.json file
after that you have to run bot.py to train your own models and you are using
respon.py to classify and make a response chat with it.

Go to chatbot -> model -> pengetahuan.json(to suit with your own data)

$ python bot.py
$ python respon.py

if error while you run the respon.py:
    please edit this code based on your environment
    in respon.py
        sys.path.append('/Users/detikcom/Documents/skripsi/')
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siPintar.settings")
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

...
```
## Contributors

### Contributors on GitHub
* [Rino Alfian](https://github.com/kunci115)


### Third party libraries
* see [Tensorflow](https://github.com/tensorflow/tensorflow) 
* see [tflearn](https://github.com/tflearn/tflearn)
* see [Pysastrawi](https://github.com/har07/PySastrawi)
* see [nltk](https://github.com/nltk/nltk)
* see [django](https://github.com/django/django)


## How-to use this code
```
$ git clone https://github.com/kunci115/siPintar.git
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
...
```
## Contact
#### Developer
* e-mail: rino.alpin@gmail.com
* Twitter: [@rinoalf](https://twitter.com/rinoalf "rinoalf")

# Expectation
<h4> I was expect that if you are using this, please share the data so we can work together<h4>

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=rinoalfian&url=https://github.com/kunci115/siPintar&title=siPintar&language=&tags=github&category=software) 
