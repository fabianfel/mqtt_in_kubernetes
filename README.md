# Data Warehouse Fallstudie: MQTT in Kubernetes

Dies ist das Code Repository für die Data Warehouse Seminararbeit von Fabian Feldherr

## Hinweis

In dieser README werden Platzhalter für Variablen in Befehlen verwendet.  
Um die Befehle ausführen zu können müssen diese Platzhalter (gekennzeichnet durch geschweifte Klammern _{Beschreibung}_) durch konkrete Werte ersetzt werden.

Beispiel:  
Vorher: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -e "MQTT_BROKER={mqtt-broker host}" \
Angepasst: &nbsp;&nbsp;&nbsp;&nbsp; -e "MQTT_BROKER=127.0.0.1" \

## Dockerisierung

### MQTT-Publisher

Bauen des Docker Containers

> docker build -t fabianfel/public:dwh_mqtt_publisher ./publisher

<br>
Beispiel zum Ausführen des gebauten Containers:

> docker run \
>  --network host \
>  -e "MQTT_BROKER={mqtt-broker host}" \
>  -e "MQTT_PORT={mqtt port}" \
>  -e "MQTT_TOPIC={mqtt topic}" \
>  fabianfel/public:dwh_mqtt_publisher

### MQTT-Subscriber

> docker build -t fabianfel/public:dwh_mqtt_subscriber ./subscriber

<br>
Beispiel zum Ausführen des gebauten Containers:

> docker run \
>  --network host \
>  -e "PG_HOST={postgres host}" \
>  -e "PG_PORT={postgres port}" \
>  -e "PG_DATABASE={database name}" \
>  -e "PG_USER={postgres user}" \
>  -e "PG_PASSWORD={postgres password}" \
>  -e "MQTT_BROKER={mqtt-broker host}" \
>  -e "MQTT_PORT={mqtt port}" \
>  -e "MQTT_TOPIC={mqtt topic}" \
>  fabianfel/public:dwh_mqtt_subscriber

## Kubernetes PostgreSQL secret

Bevor die Container in Kubernetes deployed werden können, müssen zunächst die secrets für die PostgreSQL DB erstellt werden.
Dies kann über direkte eine Texteingabe:

> kubectl create secret generic postgres-secret --from-literal="user={postgres user}"--from-literal="password={postgres password}"

oder über das Einlesen einer ENV Datei geschehen.

> kubectl create secret generic postgres-secret --from-env-file={path to env file}
