FROM node:16.15.1-alpine

ENV TZ Europe/Moscow

# устанавливаем простой HTTP-сервер для статики
RUN npm install -g http-server

# делаем каталог 'app' текущим рабочим каталогом
RUN mkdir -p /app/
WORKDIR /app

# копируем оба 'package.json' и 'package-lock.json' (если есть)
COPY package*.json ./

# устанавливаем зависимости проекта
RUN npm install
RUN npm install -g npm

RUN npm install vuex --save 
RUN npm install axios

# копируем файлы и каталоги проекта в текущий рабочий каталог (т.е. в каталог 'app')
COPY . ./app

# собираем приложение для production с минификацией
# RUN npm run build

CMD [ "http-server", "dist" ]
