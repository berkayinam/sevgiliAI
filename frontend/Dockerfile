FROM node:18-alpine

WORKDIR /app

# Add node user and set permissions
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /app

COPY package*.json ./
RUN npm install

COPY . .

# Set correct permissions
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 2301

CMD ["npm", "start"] 