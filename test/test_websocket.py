import websocket

import _thread as thread

import time

import json


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        msg = [
            {'ticket': "test"},
            {
                'type': "trade",
                'codes': ["KRW-BTC"],
            }]
        json_msg = json.dumps(msg)
        for i in range(3):
            time.sleep(1)
            ws.send(json_msg)
        time.sleep(1)
        # result = ws.recv()
        # print(result)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api-beta.upbit.com/websocket/v1",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


