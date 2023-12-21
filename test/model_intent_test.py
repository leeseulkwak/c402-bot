import os, sys

cwd=os.getcwd()
sys.path.append(os.path.join(cwd))

from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic=os.path.join(cwd,'train_tools','dict','chatbot_dict.bin'),
               userdic=os.path.join(cwd,'utils','user_dic.tsv'))

intent=IntentModel(model_name=os.path.join(cwd, 'models', 'intent', 'intent_model.h5'), proprocess=p)

query="영화 예매할께요"
predict=intent.predict_class(query)
prodict_label=intent.labels[predict]

print(query)
print("의도 예측 클래스 :", predict)
print('의도 예측 레이블:', prodict_label)

            