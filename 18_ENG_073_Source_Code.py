#necessary libraries
import io
import random
import string # to process standard python strings
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Keyword Matching
GREETING_INPUTS = LemNormalize("hello hi hii greetings sup what's up hey",)
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

ABOUT_INPUTS = LemNormalize("who are you your name")
ABOUT_RESPONSES = ("My name is Super Bot")

PAY_INPUTS = LemNormalize("How can pay accept Mastercard? Visa cards cash only for paying")
PAY_RESPONSES = ["You can use VISA or Mastercard and Paypal or cash for paying","We accept mostly credit cards, and Paypal other than cash"]

BUYGOODS_INPUTS=LemNormalize("want food buy some these items")
BUYGOODS_RESPONSES=("Please tell your list","Tell the goods list","Good list please")

VEGETABLES_INPUTS=LemNormalize("vege vegetables carrot pumpkin corn potato onion leek ginger fennal cucumber beet ")
VEGETABLES_RESPONSES=("Shelf No 11")

FRUITS_INPUTS=LemNormalize("fruits mango guava banana apple orange lemon grapes strawbery papaya passion fruit cherry")
FRUITS_RESPONSES=("Shelf No 12")

BUISCUITS_INPUTS=LemNormalize("buiscuit marie lemmon puff cracker")
BUISCUITS_RESPONSES=("Shelf No 15")

DRINKS_INPUTS=LemNormalize("cola fanta milo faluda milk juice vine lemonade")
DRINKS_RESPONSES=("Shelf No 17")

MEAT_INPUTS=LemNormalize("bacon chicken fish ham beef lamb pork sausage scalloops shrimp steak turkey lobster")
MEAT_RESPONSES=("Shelf No 19")

STATIONERY_INPUTS=LemNormalize("stationery books pens pencils erasers files rulers")
STATIONERY_RESPONSES=("Shelf No 22")

ELEC_INPUTS=LemNormalize("computer mobiles tabs headsets gaming cd dvd mouse keyboards display back covers circuits bulbs cameras cables")
ELEC_RESPONSES=("Shelf No 31")

PLASTIC_INPUTS=LemNormalize("plastic toys rubber buckets cups jugs plates bags coves")
PLASTIC_RESPONSES=("Shelf No 34")

SOAP_INPUTS=LemNormalize("soap sunlight lux detol lifebouy")
SOAP_RESPONSES=("Shelf No 41")

COSMETICS_INPUTS=LemNormalize( "face cream face wash hair color body wash perfumes body cream powder lotion tooth paste tooth powder mouth washes hair oil shampoos lipstic makeup sun cream")
COSMETICS_RESPONSES=("Shelf No 43")

CLEANERS_INPUTS=LemNormalize("sponge wipes tub & tile cleaner dishwashing soap bleach Paper air freshener dryer sheets stain remover vacuum bags laundry detergent dishwasher detergent")
CLEANERS_RESPONSES=("Shelf No 45")

MEDI_INPUTS=LemNormalize("medicine tablets herbals")
MEDI_RESPONSES=("Shelf No 51")

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence:
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def pay(sentence):
    for word in sentence:
        if word.lower() in PAY_INPUTS:
            return random.choice(PAY_RESPONSES)

def vege(sentence):
    for word in sentence:
        if word.lower() in VEGETABLES_INPUTS:
            return VEGETABLES_RESPONSES

def buying(sentence):
    for word in sentence:
        if word.lower() in BUYGOODS_INPUTS:
            return random.choice(BUYGOODS_RESPONSES)

def fruits(sentence):
    for word in sentence:
        if word.lower() in FRUITS_INPUTS:
            return FRUITS_RESPONSES

def buiscuit(sentence):
    for word in sentence:
        if word.lower() in BUISCUITS_INPUTS:
            return BUISCUITS_RESPONSES

def soap(sentence):
    for word in sentence:
        if word.lower() in SOAP_INPUTS:
            return SOAP_RESPONSES            

def stationery(sentence):
    for word in sentence:
        if word.lower() in STATIONERY_INPUTS:
            return STATIONERY_RESPONSES

def drink(sentence):
    for word in sentence:
        if word.lower() in DRINKS_INPUTS:
            return DRINKS_RESPONSES
            
def meat(sentence):
    for word in sentence:
        if word.lower() in MEAT_INPUTS:
            return MEAT_RESPONSES
            
def elec(sentence):
    for word in sentence:
        if word.lower() in ELEC_INPUTS:
            return ELEC_RESPONSES

def cleaner(sentence):
    for word in sentence:
        if word.lower() in CLEANERS_INPUTS:
            return CLEANERS_RESPONSES

def plastic(sentence):
    for word in sentence:
        if word.lower() in PLASTIC_INPUTS:
            return PLASTIC_RESPONSES

def cosmetics(sentence):
    for word in sentence:
        if word.lower() in COSMETICS_INPUTS:
            return COSMETICS_RESPONSES            

def medi(sentence):
    for word in sentence:
        if word.lower() in MEDI_INPUTS:
            return MEDI_RESPONSES  

flag=True
ITEM_LIST=[]
PLACE_LIST=[]

print("Super Bot : My name is Super Bot. I will help you to find goods easily. When you want to exit, type Bye!")
while(flag==True):
    user_input=input()
    user_response = LemNormalize(user_input)
    if(user_input!='bye'):
        if(user_input=='thanks' or user_input=='thank you' ):
            flag=False
            print("Super Bot : You are welcome..")
            input()
        else:
            if(greeting(user_response)!=None):
                print("Super Bot : "+greeting(user_response))

            elif(pay(user_response)!=None):
                print("Super Bot : "+pay(user_response))    

            elif(buying(user_response)!=None):
                print("Super Bot : "+buying(user_response))

            elif(vege(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+vege(user_response))
                PLACE_LIST.append(vege(user_response))

            elif(fruits(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+fruits(user_response))
                PLACE_LIST.append(fruits(user_response))

            elif(buiscuit(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+buiscuit(user_response))
                PLACE_LIST.append(buiscuit(user_response))

            elif(drink(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+drink(user_response))
                PLACE_LIST.append(drink(user_response))

            elif(meat(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+meat(user_response))
                PLACE_LIST.append(meat(user_response))

            elif(elec(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+elec(user_response))
                PLACE_LIST.append(elec(user_response))

            elif(soap(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+soap(user_response))
                PLACE_LIST.append(soap(user_response))

            elif(cleaner(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+cleaner(user_response))
                PLACE_LIST.append(cleaner(user_response))

            elif(plastic(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+plastic(user_response))
                PLACE_LIST.append(plastic(user_response))

            elif(cosmetics(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+cosmetics(user_response))
                PLACE_LIST.append(cosmetics(user_response))

            elif(medi(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+medi(user_response))
                PLACE_LIST.append(medi(user_response))

            elif(stationery(user_response)!=None):
                ITEM_LIST.append(user_input)
                print("Super Bot : "+stationery(user_response))
                PLACE_LIST.append(stationery(user_response))
            else:
                 print("Super Bot : ",end="I'm Sory. I could not uderstand you\n")
    else:
        flag=False

print("Super Bot : Bye! take care..\n")    
print("Your Item list is here with the relevant places\n")
for i in range(len(ITEM_LIST)):
    print ("\t" + ITEM_LIST[i] + "\t:"+ PLACE_LIST[i]+"\n")
    