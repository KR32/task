# # Stage 1: Build the frontend.

# FROM --platform=linux/amd64 node:17-bullseye-slim as build-stage

# WORKDIR /app

# COPY package*.json /app/

# # RUN if test -e package-lock.json; then echo "Package Lock file Exists" && rm package-lock.json; fi

# # RUN if test -d node_modules; then echo "Node Modules Exists" && rimraf node_modules; fi

# RUN npm install

# COPY ./ /app/

# ARG FRONTEND_ENV=local

# ENV VUE_APP_ENV=${FRONTEND_ENV}

# RUN npm run build --mode ${FRONTEND_ENV}


# # Stage 2 : Deploy the build using nginx

# FROM nginx:1.18.0-alpine

# COPY --from=build-stage /app/dist /usr/share/nginx/html

# RUN rm -v /etc/nginx/conf.d/default.conf

# COPY ./default.conf /etc/nginx/conf.d/default.conf

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]


FROM node:lts-buster-slim as build-stage

RUN mkdir -p /frontend/public /frontend/src
COPY ./public /frontend/public
COPY ./src /frontend/src
COPY ./*js /frontend/
COPY ./*.env* /frontend/
COPY ./package.json /frontend/package.json
COPY ./vue.config.js /frontend/vue.config.js
# set working directory
WORKDIR /frontend
RUN pwd
RUN ls

RUN npm install
ENV PORT=80
EXPOSE 80       
CMD ["npm", "i"]

# Stage 2 : Deploy the build using nginx

FROM nginx:1.18.0-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html

RUN rm -v /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]