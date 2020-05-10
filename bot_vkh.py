from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from vk_api.utils import get_random_id
import random, json

users_data = {}

def button(label, color):
    return {"action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": label
                },
                "color": color
            }
keyboard = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1"
                },
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2"
                },
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "3"
                },
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "4"
                },
            }
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def main():
    print('Как скажите')
    rules = f'{random.choice(["Куда встал? Сиди пиши правила", "Ладно сидим и пишем это гов...", "А игру кто-нибудь деелает?"])}'
    gruop_id = 194651076
    vk_session = vk_api.VkApi(
        token='bb37681562bc4a86332f6e6ca1e9110af1e817d2dd7872f1fba77fb13df2e4d15a94e4d4aed37f9040816')
    vk = vk_session.get_api()
    long_poll = VkBotLongPoll(vk_session, gruop_id)
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.message
            uid = msg.from_id
            user = vk.users.get(user_ids=uid, fields=['city'])[0]
            if msg['text'] not in ['1', '2', '3', '4']:
                vk.messages.send(user_id=uid,
                                 message=f'Привет, {user["first_name"]} {user["last_name"]}',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'Как жиза? Чё надо?',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'Мои ухи недоразвиты (как и можг) поэтому только заранее заложенные команды.',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'Вот список команд',
                                 random_id=get_random_id(),
                                 keyboard=keyboard)
                vk.messages.send(user_id=uid,
                                 message=f'Вот список команд',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'1 - Список команд',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'2 - Правила игры',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'3 - Инффа о разрабах',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'4 - Последняя новость',
                                 random_id=get_random_id())
            elif msg['text'] == '1':
                vk.messages.send(user_id=uid,
                                 message=f'Вот список команд',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'1 - Список команд',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'2 - Правила игры',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'3 - Инффа о разрабах',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'4 - Последняя новость',
                                 random_id=get_random_id())
            elif msg['text'] == '2':
                vk.messages.send(user_id=uid,
                                 message=f'Z--z-z-z-z-z-z-z-z--z-z-z-z--z-z-z-z-z--z-z-z',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'Пацаны он ушел?',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=rules,
                                 random_id=get_random_id())
            elif msg['text'] == '3':
                vk.messages.send(user_id=uid,
                                 message=f'Ну там есть Илья, Иван и Леха',
                                 random_id=get_random_id())
            elif msg['text'] == '4':
                f1 = open('news.txt', 'r')
                vk.messages.send(user_id=uid,
                                 message=f'{f1.read()}',
                                 random_id=get_random_id())
                f1.close()

if __name__ == '__main__':
    main()