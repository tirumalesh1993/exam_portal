from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class ExamConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        if str(self.user) == 'AnonymousUser':
            self.room_group_name = 'exam_%s' % self.id
        else:
            self.room_group_name = 'exam_admin'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_type = text_data_json['type']

        if message_type == 'add_user':
            async_to_sync(self.channel_layer.group_send)(
                'exam_admin',
                {
                    'type': 'add_user',
                    'message': message,
                }
            )
        elif message_type == 'check_answer':
            async_to_sync(self.channel_layer.group_send)(
                'exam_admin',
                {
                    'type': 'check_answer',
                    'message': message,
                    'id': text_data_json['id'],
                    'user': text_data_json['user']
                }
            )
        else:
            async_to_sync(self.channel_layer.group_send)(
                'exam_%s' % self.id,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

    def check_answer(self, event):
        user = event['user']
        answer = event['message']
        id = event['id']
        print(user)
        print(answer)
        print(id)
        if int(id) == 0 and int(answer) == 8:
            self.send(text_data=json.dumps({
                'type': 'score',
                'user': user,
                'score': 20
            }))
        elif int(id) == 1 and int(answer) == 3:
            self.send(text_data=json.dumps({
                'type': 'score',
                'user': user,
                'score': 20
            }))
        elif int(id) == 2 and int(answer) == 10:
            self.send(text_data=json.dumps({
                'type': 'score',
                'user': user,
                'score': 20
            }))
        elif int(id) == 3 and int(answer) == 29:
            self.send(text_data=json.dumps({
                'type': 'score',
                'user': user,
                'score': 20
            }))
        elif int(id) == 4 and int(answer) == 25:
            self.send(text_data=json.dumps({
                'type': 'score',
                'user': user,
                'score': 20
            }))

    def add_user(self, event):
        event['type'] = 'add_user'
        self.send(text_data=json.dumps(event))
