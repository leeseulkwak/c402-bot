import os, sys

cwd = os.getcwd()
sys.path.append(os.path.join(cwd))

from utils.Preprocess import Preprocess
import pickle

f=os.path.join(cwd, 'chatbot_dic.bin') #경로 찾아서 f에 넣어 주고
with open(f, "rb") as f: #open은 따로 해서 rb로 읽어 주기

    word_index=pickle.load(f)
    f.close()

sent="영화 예매할꼐요"

#전처리 객체 생성
p = Preprocess(userdic=os.path.join(cwd, 'utils', 'user_dic.tsv'))

#형태소 분석기 실행
pos=p.pos(sent)

#품사 태그 없이 키워드 출력
keywords=p.get_keywords(pos, without_tag=True)
for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        #해당 단어가 사전에 없는 경우 OOV 처리
        print(word, word_index['OOV'])