#import required libraries
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# Define stop words to be removed
stop_words = set(stopwords.words('english'))
# STOP WORDS # metinde herhangi bir anlamı olmayan ama dilde kullanılan yaygın kelimeler: bağlaçlar, zamirler vb. (for, is, of)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()
# LEMMATIZATION # kelimleri köklerine ayırmak / literatürde stemming işlemi de kullanılır köklerine ayırmak için 


# Define function to preprocess text data
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
   
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
   
    # Tokenize text into words
    words = word_tokenize(text)
   
    # Remove stop words
    words = [word for word in words if word not in stop_words]
   
    # Lemmatize words
    words = [lemmatizer.lemmatize(word) for word in words]
   
    # Join words back into text
    text = ' '.join(words)
   
    return text


# Load the DialoGPT 
chatbot_name = "microsoft/DialoGPT-medium"
chatbot_tokenizer = AutoTokenizer.from_pretrained(chatbot_name, padding_side='left')
chatbot_tokenizer.add_special_tokens({'pad_token': chatbot_tokenizer.eos_token})  # Add a new pad token
chatbot_model = AutoModelForCausalLM.from_pretrained(chatbot_name)


# AI Chatbot'tan yanıt oluşturmak için bir fonksiyon
def generate_response(input_text):
    bot_input_ids = chatbot_tokenizer.encode(input_text + chatbot_tokenizer.eos_token, return_tensors='pt', padding=True)
    chatbot_output = chatbot_model.generate(bot_input_ids, max_length=1000, num_return_sequences=1)
    chatbot_response = chatbot_tokenizer.decode(chatbot_output[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return chatbot_response 

def chat():
    print("606Bot: Hello! How can I assist you today?")
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "end chat":
            print("606Bot: Goodbye! Have a great day!")
            break
        
        response = generate_response(user_input)
        print("606Bot:", response)
        
chat()