FROM node:18-alpine

WORKDIR /usr/src/app/frontend

COPY . .

RUN npm install

EXPOSE 8080

CMD ["npm", "run", "build"]
