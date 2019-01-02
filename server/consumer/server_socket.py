from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class SocketConsumer(WebsocketConsumer):
    def websocket_connect(self, event):
        # Called on connection.
        # To accept the connection call:
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        self.accept()

    def websocket_receive(self, event):
        self.send("True")

    def disconnect(self, close_code):
        pass

    # -----------------------------------------------------------------------------------
    # Handler definitions! handlers will accept their corresponding message types.
    # A message with type events.send_commands has to have a function event_alarm
    # -----------------------------------------------------------------------------------

    def events_listener(self, event):
        """
        This is custom event handler called at time send message to client or equipment.
        :param event: passed dictionary
        :return:
        """
        self.send("cmd")

