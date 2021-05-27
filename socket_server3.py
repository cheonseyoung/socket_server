########################
# # Server
#
# import asyncio  # 웹 소켓 모듈을 선언한다.
# import websockets  # 클라이언트 접속이 되면 호출된다.
# import datetime
# import time
#
# async def accept(websocket, path):
#     while True:
#         time.sleep(1)
#         data = await websocket.recv();  # 클라이언트로부터 메시지를 대기한다.
#         # data = datetime.datetime.now()
#         # print(str(data));
#         await websocket.send(data);  # 클라인언트로 echo를 붙여서 재 전송한다.
#
#
# # "0.0.0.0" => 서버 pc에 ip 주소를 입력해준다.
# # 0000 => 서버 pc에 포트를 입력 해 준다.
# start_server = websockets.serve(accept, "127.0.0.1", 12000);
#
# # 비동기로 서버를 대기한다.
# asyncio.get_event_loop().run_until_complete(start_server);
# asyncio.get_event_loop().run_forever();
# ########################

import asyncio

# 웹 소켓 모듈을 선언한다.
import websockets
import datetime

# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
    while True:
        # 클라이언트로부터 메시지를 대기한다.
        data = await websocket.recv();
        print(str(data))
        data = str(datetime.datetime.now())
        print("receive : " + data);

        # 클라인언트로 echo를 붙여서 재 전송한다.
        await websocket.send("echo : " + data);

# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다.
start_server = websockets.serve(accept, "localhost", 9998);

# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();

##############################

