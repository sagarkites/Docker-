# Base Image
FROM nginx
# Copies the configuration file 
COPY nginx.conf /etc/nginx/nginx.conf
# port to expose outside 
EXPOSE 80
# Command
CMD ["nginx", "-g", "daemon off;"]
