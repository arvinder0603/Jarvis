import random 
import json 
import torch 
from Brain import NeuralNetwork
from NeuralNetwork import bag_of_word,tokenizer
from Task import NonInputExecution
from Task import InputExecution
from Listen import speech_to_text


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("Jarvis\intents.json",'r') as json_data:
    intents=json.load(json_data)


FILE="Jarvis\Train_data.pth"
data=torch.load(FILE)

input_size=data['input_size']
hidden_size=data['hidden_size']
output_size=data['output_size']
all_words=data['All_words']
tags=data['tags']
model_state=data['model_state']

model=NeuralNetwork(input_size,hidden_size,output_size).to(device)


model.load_state_dict(model_state)
model.eval()


#-------------------------------
name="jarvis"
# from Listen import Listen
from Speak import say

def Main():

    

    sentence=speech_to_text()
    result=str(sentence)

    

    if sentence == "bye":
        exit()

    sentence=tokenizer(sentence)
    X = bag_of_word(sentence,all_words)
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X).to(device)
    
    output=model(X)
    
    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    prob = torch.softmax(output,dim=1)

    prob = prob[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tags']:
               
                reply  = random.choice(intent['responses'])
                
                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                      NonInputExecution(reply)
                elif "day" in reply:
                    NonInputExecution(reply)
                elif "wikipedia" in reply:
                    InputExecution(reply,result)
                elif "google" in reply:
                    InputExecution(reply,result)
                else:
                  say(reply)



 











Main()
