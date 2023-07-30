FROM node:bullseye

WORKDIR /usr/src/app/frontnend

COPY package.json package.json

RUN npm i -g @vue/cli
RUN npm i -g serve
RUN npm install

COPY . .

ENV HOST=0.0.0.0

CMD ["npm", "run", "build"]
