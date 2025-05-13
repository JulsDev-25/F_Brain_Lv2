FROM node:latest

WORKDIR /app

COPY package*.json vite.config.js .

RUN yarn install

COPY . .

EXPOSE 5173

CMD ["yarn", "run", "dev", "--", "--host"]
