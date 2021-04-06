import requests
import random

"""Apidata docstrings.

This module used to get game information from de API. using http get request
to this URL https://api-escapamet.vercel.app

Attributes:
    roomName (str): the name of room, used for extract specific room into json

    gameName (str): the name of game, used for extract specific game into json

"""
class GameInfo:
  def __init__(self,roomName,gameName):
    url = 'https://api-escapamet.vercel.app'
    maxRetry = 2
    countReq = 0
    self.clueMsg=[]

    while countReq<maxRetry:
        try:
            #snet HTML get request
            resp = requests.get(url)

            #convert response to json
            data_api = resp.json()
            break
        except msjError:
                print('Error:'+msjError)
                countReq +=1

    for data in data_api:
        if (data.get('name')==roomName):
      
            data_obj = data['objects']
            for obj in data_obj:
                self.game = obj['game']
                if (self.game['name']==gameName):
                    if (gameName=="ahorcado"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.answer = q['answer']
                        self.question = q['question']
                        self.clueMsg.append(q['clue_1'])
                        self.clueMsg.append(q['clue_2'])
                        self.clueMsg.append(q['clue_3'])
                        break
                    elif (gameName=="Preguntas matemáticas"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.question = q['question']
                        break
                    elif (gameName=="Criptograma"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.question = q['question']
                        self.desplaz = q['desplazamiento']
                        break
                    elif (gameName=="Lógica Booleana"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.question = q['question']
                        self.answer = q['answer']
                        break
                    elif (gameName=="Adivinanzas"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.answers = q['answers']
                        self.question = q['question']
                        self.clueMsg.append(q['clue_1'])
                        self.clueMsg.append(q['clue_2'])
                        self.clueMsg.append(q['clue_3'])
                        break
                    elif (gameName=="Palabra mezclada"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.category = q['category']
                        self.question = q['question']
                        self.words = q['words']
                        break
                    elif (gameName=="escoge un número entre"):
                        #get questions
                        self.questions = self.game['questions']

                        q = random.choice(self.questions)
                        self.answer = q['answer']
                        self.question = q['question']
                        self.clueMsg.append(q['clue_1'])
                       
                        break