# Mars
Mars è un progetto universitario dello studente Rosario Pluchino che ha l'obiettivo di prevedere la temperatura massima di Marte acquisendo i dati meteo da api.nasa.gov elaborarli e confrontarli con i dati reali
# Struttura
![Mars.png](attachment:Mars.png)

Per maggiori dettagli sull'utilizzo delle tecnologie è consigliabile visionare la documentazione.
# Guida d'uso e requisiti
* Docker
* Python3

Prima di tutto bisogna clonare il repository del progetto https://github.com/rosariopluchino/Mars.git . Una volta fatto ciò spostarsi all'interno della cartella principale con il comando cd ed eseguire:
* ./build.sh
    che server per creare l'immagine docker dell'applicazione(bisogna farlo solamente la prima volta)
* docker-compose up

Infine aprire un browser web e digitare localhost:5601 per poter creare nuove visualizzazioni dei dati tramite Kibana.
