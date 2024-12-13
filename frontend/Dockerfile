FROM mcr.microsoft.com/devcontainers/typescript-node:1-20-bookworm as development
CMD [ "npm", "start" ]

FROM node:23 as production

WORKDIR /frontend

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# EXPOSE 8000/tcp

CMD [ "npm", "start" ]