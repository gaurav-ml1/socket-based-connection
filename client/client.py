import ssl
import websocket
import time
import jwt
try:
    import thread
except ImportError:
    import _thread as thread
from pyhocon import ConfigFactory

# initializing
config = ConfigFactory.parse_file('config.hocon')


class WebSocketConnection:
    """
    This is connection class to define connection type.
    """
    agent = None
    def __init__(self, server_url, enable_trace, auth_header):
        """
        :param server_url:
        :param enable_trace:
        :param auth_header:
        """
        websocket.enableTrace(enable_trace)
        self.connection = websocket.WebSocketApp(
            server_url,
            header={"authorization": auth_header},
            on_message= WebSocketConnection.message_listener,
            on_error= WebSocketConnection.error_listener,
            on_close= WebSocketConnection.close_listener
        )
        self.connection.on_open = WebSocketConnection.connection_open_listener

    def start(self):
        while True:
            self.connection.run_forever(
                sslopt={
                    "cert_reqs": ssl.CERT_NONE,
                    "check_hostname": True
                },
                ping_interval= 3
            )
            time.sleep(5) #---- stop iteration for 5 sec and then it again try to make connection.



    @staticmethod
    def connection_open_listener(ws):
        """
        It called at open a connection.
        :param ws:
        :return:
        """
        print ("connection opened")
        # ws.send("Hi")

    @staticmethod
    def error_listener(ws, error):
        """
        It called when come error in connection establishment.
        :param error:
        :return: None
        """
        print (error)

    @staticmethod
    def message_listener(ws, message):
        """
        It called when any message received on connection
        :param message:
        :return: None
        """
        print(message)

    @staticmethod
    def close_listener(ws):
        """
        It called at close time.
        :param ws:
        :return:
        """
        pass


def get_unique_token(device_name):
    input_parameters = {'secret-key': config.get("secret_key"), 'name': device_name, 'device_id': config.get("device_id")}
    return jwt.encode(input_parameters, 'secret', algorithm='HS256').decode("utf-8")


if __name__ == "__main__":
    connection = WebSocketConnection(config.get("server.url"), True, get_unique_token("PCs"))
    connection.start()

