FROM nginx:1.21.6 

LABEL maintainer="Damian Naprawa <damian@szkoladockera.pl>"

COPY app /usr/share/nginx/html

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
