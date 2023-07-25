FROM node:bullseye

WORKDIR /usr/src/app/frontnend

COPY . .

RUN npm i -g @vue/cli
RUN npm i -g serve
RUN npm install package.json
ENV HOST=0.0.0.0
CMD ["npm", "run", "build"]
