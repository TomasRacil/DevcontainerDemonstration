FROM node:23

WORKDIR /frontend

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# EXPOSE 8000/tcp

CMD [ "npm", "start" ]