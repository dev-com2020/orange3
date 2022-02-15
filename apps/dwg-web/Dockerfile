FROM nginx:1.21.6 
# Użyj obrazu bazowego nginx:1.21.6 z Docker Hub

LABEL maintainer="Damian Naprawa <damian@szkoladockera.pl>"
# Ustaw etykietę maintainer

# Podczas budowania obraz:
COPY index.html docker.png /usr/share/nginx/html/
# Skopiuj lokalne pliki index.html i docker.png do /usr/share/nginx/html

EXPOSE 80 443 	
# UWAGA: To tylko informacja w metadanych obrazu
# Powyższe NIE powoduje udostępnienia portów w kontenerze po uruchomieniu

CMD ["nginx", "-g", "daemon off;"]
# Polecenie jakie ma zostać wykonane przy starcie kontenera (można je nadpisać)
