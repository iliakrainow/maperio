from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from vk_api.utils import get_random_id
import datetime
import random

users_data = {}


def main():
    news = 'Я живоооооооооооооооооооооооооооооооооооооооооооой, Хотя ты это наверняка знаешь........... мдаа'
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
            if msg['text'] not in ['1', '2', '3', '4', '5']:
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
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'1 - Список команд',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'2 - Правила игры',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'3 - Последняя новость',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'4 - Инффа о разрабах',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'5 - твой id',
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
                                 message=f'3 - Последняя новость',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'4 - Инффа о разрабах',
                                 random_id=get_random_id())
                vk.messages.send(user_id=uid,
                                 message=f'5 - твой id',
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
                                 message=news,
                                 random_id=get_random_id())
            elif msg['text'] == '4':
                vk.messages.send(user_id=uid,
                                 message=f'Ну там есть Илья, Иван и Леха',
                                 random_id=get_random_id())
            elif msg['text'] == '5':
                vk.messages.send(user_id=uid,
                                 message=f'{msg["peer_id"]}',
                                 random_id=get_random_id())

def u():
    command = int(input('Здравствуй мой повелитель что вы хотите сделать. 1 - Опубликовать пост в группе,'
                    ' или 2 - дать мне нормально работать?'))
    if command == 1:
        news = input('Новость:')
        vk_session2 = vk_api.VkApi(input('Логин '), input('Пароль: '))
        vk_session2.auth()
        vk2 = vk_session2.get_api()
        print(vk2.wall.post(message=news,
                        owner_id='-194651076'))
        u()
    elif command == 2 and __name__ == '__main__':
        main()

u()