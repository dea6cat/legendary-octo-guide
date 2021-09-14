# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import ctypes
import time
import sqlite3
ctypes.windll.kernel32.SetConsoleTitleA(":A2_")
#Done with machine learning, this version of A2 is way better than before,
#and it can now be more like an actual thinking machine, that can have a conversation with anygiven human.
#I tried to make a ver using tensorflow, to make it DEEP LEARNING, but my computer (Dell Latitude D820) held me back,
#at least this version will learn from future conversations, like I had planned, I will keep improving the database so it can be better at 
#talking, and I'll try to make an UI for it aswell. JUNE 23/2018
#"chatterbot.input.VariableInputTypeAdapter"
# "chatterbot.input.TerminalAdapter"
# output_adapter="chatterbot.output.TerminalAdapter",
#"chatterbot.corpus.english",
    #"chatterbot.corpus.english.greetings",
    #"chatterbot.corpus.english.conversations",

A2 = ChatBot("A2",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapter=[{
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.TimelogicAdapter",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.comparisons.levenshtein_distance",
        "chatterbot.response_selection.get_first_response"},
                   {
        
            'chatterbot.logic.LowConfidenceAdapter',
            'threshold: 0.90',
            'default_response: I am sorry, but I do not understand.'
        }],
    filters=["chatterbot.filters.RepetitiveResponseFilter"],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database="./2018-06.db")

A2.set_trainer(ChatterBotCorpusTrainer)
"""
A2.train(
    "chatterbot.corpus.spanish"
    #"chatterbot.corpus.english",
    #"chatterbot.corpus.english.greetings",
    #"chatterbot.corpus.english.conversations",
    
)
"""

"""
#subprocess.call("mv %s %s" % (source, dest1), shell=True)
files = [i for i in os.listdir(source) if i.startswith({}) and os.path.isfile(os.path.join(source, i))]
for f in files:
    shutil.copy(os.path.join(source, f), dest1)
    print"\n\tEl Estudiante sera transferid
    """
A2.set_trainer(ListTrainer)
source = r"C:/Users/xande/Desktop/"

files= os.listdir(source)
"""
for file in files:    
    if file.startswith("k"):
        chats=open(file, "r").readlines()
        A2.train(chats)
"""
"""
conv = open("chat.txt","r").readlines()
A2.set_trainer(ListTrainer)
A2.train(conv)"""


while True:
    re=input("You: ")
    boi=A2.get_response(re)
    print ("Niska: ",boi)
    
    




