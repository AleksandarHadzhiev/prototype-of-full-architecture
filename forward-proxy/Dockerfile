FROM node:10-alpine

ARG $TARGETS
ARG $BASE_URL
ARG $ENV

ENV TARGETS=$TARGETS
ENV BASE_URL=$BASE_URL
ENV ENV=$ENV

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./

USER node

RUN npm install

COPY --chown=node:node . .

EXPOSE 5000

CMD [ "node", "server.js" ]