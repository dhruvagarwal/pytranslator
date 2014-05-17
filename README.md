pytranslator
============

CLI based translator for quick translation to english within the terminal

Dependencies:
=============
* goslate
 
install it by :

     $pip install goslate

Working:
========

* You can run it as :

     $python main.py arg1 arg2 arg3
     
it fetches you translation directly or by the conventional method

     $python main.py
     Enter the text to be translated: (your text)
     (translated text to english)

* You can also use it for transalting bulk text using pipes as:

	$cat sample.txt | python main.py


API Used:
=========

I have used goslate python module which is a free google translate api for python.
