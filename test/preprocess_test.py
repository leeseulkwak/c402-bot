import os
import sys

cwd = os.getcwd()
print(cwd)
sys.path.append(os.path.join(cwd))

from utils.Preprocess import Preprocess

sent="영화 예매할께요"

#파일 경로 수정
cwd=os.getcwd()
print(cwd)
p = Preprocess(userdic=os.path.join(cwd, 'utils', 'user_dic.tsv'))

#형태소 분석기 실행
pos=p.pos(sent)

#품사 태그와 같이 키워드 출력
ret=p.get_keywords(pos, without_tag=False)
print(ret)

#품사 태그 없이 키워드 출력
ret=p.get_keywords(pos, without_tag=True)
print(ret)