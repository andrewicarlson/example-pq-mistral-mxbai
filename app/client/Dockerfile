FROM node:20
WORKDIR /app
COPY src public package.json package-lock.json ./
RUN npm install
CMD npm run start
