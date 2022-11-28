# Messenger
### About the App
Приложение выполняет базовые функции мессенджера.
<br>
Позволяет вести беседу с одним или несколькими пользователями сети 
и обмениваться медиа данными.  
### App platform
`Frontend` реализован через `VUE.js`.
<br>
`Backend` реализован через `Django` с дополнением его библиотеками 
<br>
`DRF` и `Django-Channels`.  
Написаны тесты на ключевые методы приложения при помощи `Pytest`.
<br>
В качестве DB было отдано предпочтение `Postgresql`.
### API
Была реализована идея передачи данных по вэб-сокетам, что в значительной степени ускорило получение ответа от сервера для пользователя. 
<br>
На `VUE.js` написаны методы, которые открывают канал, принимают данные от пользователя, обрабатывают и отправляют их на `backend`. 
Так же написан триггер перезапускающий канал вэб-сокета в случае его падения по тайм-ауту или принудительного разрыва связи при открытии новой страницы в браузере. 
<br>
``` js
# открытие канала и прослушивание сигналов 
this.wsMessages = new WebSocket('ws://' + this.urlServer + '/ws/getMessages/' + this.data_chat_id + '/?token=' + this.token);
this.wsMessages.onopen = () => this.get_message_connect();
this.wsMessages.onmessage = e => this.get_message_message(e);
this.wsMessages.onclose = () => this.get_message_close();

# отправка данных по каналу
this.wsMessages.send(JSON.stringify({
    quantity_start: this.quantity_start,
    quantity_finish: this.quantity_finish
}));
```
В свою очередь на `Django` выстроена логика обработки входящих данных. В приложении до 90% информации на странице обновляется без ее перезагрузки, поэтому было
реализовано множество методов разделяющих входящие данные по типу и их назначению. После обработки этих данных сервер выдает ответ в `json` формате.
<br>
```python
class AsyncMessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['pk']
        self.group = 'chat_' + self.chat_id
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

    async def receive_json(self, data, **kwargs):
        action = data['action']
        text = data['message']
        ...
        
    await self.channel_layer.group_send(
            self.group,
            {
                'type': func,
                'data': new_message
            }
        )
        ...
```
### Functions the App
Функциональность добавленная в приложение:
- [X] Авторизация 
- [X] Регистрация
- [X] Смена / Восстановление пароля
- [X] Создание, изменение данных профиля
- [X] Приватность профиля
- [X] Оформление профиля
- [X] Приглашение в друзья
- [X] Отображение статуса в случае отправки заявки на дружбу
- [X] Возможность подтвердить или отвергнуть приглашение
- [X] Удаление из списка друзей
- [X] Счетчик непрочитанных сообщений и не принятых приглашений
- [X] Создание диалога через кнопку выбора действий у конкретного пользователя
- [X] Создание чата / диалога через специализированную кнопку 
- [X] Динамическая сортировка чат блоков по дате написания сообщения
- [X] Поиск пользователей
- [X] Создание / Редактирование / Удаление сообщений
- [X] Эмоджи
- [X] Добавление Фото / Видео контента
- [X] История вложений чата
- [X] Позиционирование медиа для полноэкранного просмотра
- [X] Загрузка контента в зависимости от высоты прокрутки
- [X] Создание / Изменение имени диалога / беседы
- [X] Сохранение последней сессии в браузере 
- [X] Адаптация верстки под экран мобильного устройства
### Install Ubuntu Server
Установку можно произвести как на 1 сервер так и разбить каждую часть под отдельный сервер.
<br>
На данный момент каждый блок имеет свои настройки докер файла для независимой установки.
<br>
Устанавливаем зависимости.
<br>
```
sudo apt update
sudo apt install libpq-dev
sudo apt-get install python3-psycopg2
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Не забываем, что нужно вносить свои данные в `config.yaml` и данные по БД так же должны совпадать с данными в `Docker`.
<br>
Устанавливаем `git` и вытягиваем проект.
<br>
```
apt install git
git init .
git remote add origin git@github.com:kostroff-production/Chat.git
git clone https://github.com/kostroff-production/Chat.git
```
Делаем сборку с `Docker`.
<br>
```
chmod +x ./entrypoint.sh
docker build .
docker-compose up -d --build
```
### URL
[kostrov-production.ru](http://kostrov-production.ru/)
