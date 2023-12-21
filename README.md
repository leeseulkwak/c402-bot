
기술 : python, html, javascript, css, mariadb, virtualbox
간단 설명

 1) 챗봇예약하기[bot.py엔진 서버는 항상 On상태되어야함)
    : 챗봇엔진으로 채팅 질문을 분류해서 답변하는 채팅 기능
    * 동작 방법 (질문이 추가 될때 마다 반복 작업)
      (1) train_data.xlsx에 신규 질문 및 답변 기능 작업해서 DB에 넣어 줌
          -> chatbot_data_excel.py 실행해서 자동 DB 업데이트 가능
      (2) total_train_data.csv를 통해서 질문과 의도 숫자를 넣어줌
      (3) train_model.py를 재생성
      (4) ner_train.txt에서 전처리 진행(품사 구분)
      (5) train_model.py를 재생성
      (6) bot.py파일 실행 -> 챗봇 서버 실행
         -> flask/project/my_app을 실행하여 flask api 서버 실행
         -> bot.py 는 my_app을 통해 클라이언트 접속을 기다리며 실시간 답변을 처리해줌
       
