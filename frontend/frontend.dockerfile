# Stage 1 : Build
FROM node:lts-buster-slim as build-stage

WORKDIR /app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy rest of the files
COPY . .

# Build the project
RUN npm run build


FROM nginx:alpine as deploy-stage

COPY ./default.conf /etc/nginx/default.conf

# Remove default nginx index.html page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1
COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]