FROM node:latest

RUN mkdir /project
WORKDIR /project

COPY . .

RUN npm i -g @vue/cli
RUN npm i -g serve
RUN npm install
ENV HOST=0.0.0.0
CMD ["npm", "run", "build"]
