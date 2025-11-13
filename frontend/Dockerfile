# Frontend Dockerfile - Multi-stage build

# Stage 1: Build
FROM node:20-alpine AS build

WORKDIR /app

# Kopiera package files
COPY package*.json ./

# Installera dependencies
RUN npm install

# Kopiera source code
COPY . .

# Bygg applikationen
RUN npm run build

# Stage 2: Serve med nginx
FROM nginx:alpine

# Kopiera built assets från build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Kopiera nginx config (valfritt, för API proxy)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
