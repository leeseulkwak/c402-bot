import os, sys

cwd=os.getcwd()
sys.path.append(os.path.join(cwd))

from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic=os.path.join(cwd,'train_tools','dict','chatbot_dict.bin'),
               userdic=os.path.join(cwd,'utils','user_dic.tsv'))

ner=NerModel(model_name=os.path.join(cwd,'models','ner','ner_model.h5'), proprocess=p)

query='영화 예매할께요'
predicts=ner.predict(query)
print(predicts)