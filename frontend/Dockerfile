FROM node:lts-alpine

WORKDIR /usr/src/app/frontend

COPY . .

RUN npm install && npm install -g vue

EXPOSE 8080

RUN npm run serve
