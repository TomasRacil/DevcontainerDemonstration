# Development Stage
FROM  mcr.microsoft.com/devcontainers/typescript-node:1-20-bookworm AS development

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
# RUN npm run build

EXPOSE 8000

CMD ["npm", "start"]


# Production Stage
FROM node:20-slim AS production

WORKDIR /app
COPY --from=development /app/package.json /app/package-lock.json ./
RUN npm install --production 

COPY . .
# COPY --from=development /app/build /app/build 
RUN npm run build

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# # Change the working directory to the build folder
# WORKDIR /app/build

EXPOSE 80

CMD ["nginx", "-g", ""daemon off;"", "-c", "/app/nginx.conf"]