FROM nginx:alpine

# Remove the default Nginx web content
RUN rm -rf /usr/share/nginx/html/*

# Copy the frontend files
COPY index.html /usr/share/nginx/html/

# If you have CSS, JS, images, copy them as well
# COPY css /usr/share/nginx/html/css
# COPY js /usr/share/nginx/html/js
# COPY assets /usr/share/nginx/html/assets

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]