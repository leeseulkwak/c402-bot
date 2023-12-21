import pickle
import sys, os

cwd = os.getcwd()
sys.path.append(os.path.join(cwd))

from utils.Preprocess import Preprocess
# from tensorflow.keras import preprocessing
from keras.api._v2.keras import preprocessing
import pickle

#말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=[line.split('\t') for line in f.read().splitlines()]
        data=data[1:] #헤더 제거
    return data

#말뭉치 데이터 가져오기
cwd=os.getcwd()
filename = os.path.join(cwd, 'train_tools', 'dict', 'corpus.txt')
corpus_data=read_corpus_data(filename)

#말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성

p = Preprocess()
dict=[]
for c in corpus_data:
    pos=p.pos(c[1])
    for k in pos:
        dict.append(k[0])

# 사전에 사용될 word2index 생성
# "word2index"는 단어를 인덱스로 매핑하는 과정 또는 그 결과를 나타내는 용어
# NLP 모델은 텍스트 데이터를 처리하고 이해하기 위해 주로 단어를 다루며,
# 이때 단어를 효율적으로 다루기 위해 각 단어에 고유한 인덱스를 할당하는 것이 일반적
# 이렇게 하면 모델은 텍스트 데이터를 숫자로 표현할 수 있으며, 이를 통해 계산 및 처리를 수행
# 사전의 첫 번재 인덱스는 OOV 사용
tokenizer=preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index=tokenizer.word_index

#사전 파일 생성
f = open(os.path.join(cwd,'train_tools','dict','chatbot_dict.bin'), "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()