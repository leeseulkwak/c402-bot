import socket

class BotServer:
    def __init__(self, srv_port, listen_num):
        self.port=srv_port
        self.listen=listen_num
        self.mySock=None

    #sock 생성
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock
    
    # client 대기
    def ready_for_client(self):
        if self.mySock is not None:
            return self.mySock.accept()
        else:
            # return None
            raise RuntimeError("소켓이 초기화되지 않았습니다.")

    # sock 반환
    def get_sock(self):
        return self.mySock
