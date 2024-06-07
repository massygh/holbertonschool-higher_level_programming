# Use the Alpine base image
FROM alpine:latest

# Install curl package
RUN apk add --no-cache curl

# Set the working directory
WORKDIR /app

# Copy config.txt file to /app directory in the container
COPY config.txt /app/config.txt
