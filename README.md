### ChatbotDeepLearning Bahasa Indonesia ###

#training dengan dataset sendiri
Untuk melatih chatbot dengan data anda sendiri dapat menambahkan di folder chatbot/model/pengetahuan.json

1. setelah menambahkan data, waktunya training data dengan menjalankan file bot.py
2. setelah itu mencoba menjalankan bot dengan command python respon.py


###Way to Contribute###
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate

#run apps#
1. python manage.py createsuperuser
2. python manage.py runserver

-->open browser<--
1. 127.0.0.0:8000
2. 127.0.0.0:8000/admin (for cms mode)
