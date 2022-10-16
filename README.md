# A Realtime ISS(International Space Station) Location Streaming App

A simple app to demonstrate using Apache Kafka and Pinot to ingest, process, and display realtime data on Streamlit.

## Tech stack

- [Python](https://www.python.org/): a programming language that lets you work quickly and integrate systems more effectively
- [SQL](https://en.wikipedia.org/wiki/SQL): a domain-specific language used in programming and designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS)
- [Apache Kafka](https://kafka.apache.org/): distributed event streaming platform
- [Apache Pinot](https://pinot.apache.org/): realtime distributed OLAP datastore, designed to answer OLAP queries with low latency
- [Streamlit](https://streamlit.io/): turns python scripts into web apps in a few minutes

## How to Install and Run the Project

Spin up all resources

```bash
docker-compose up
```

Add Pinot Table

```bash
docker exec -it pinot-controller-iss bin/pinot-admin.sh AddTable \
    -tableConfigFile /config/table.json \
    -schemaFile /config/iss-schema.json \
    -exec
```

Start ingesting ISS location data

```bash
run app.py
```

Check if data is being ingested

```bash
docker exec -it kafka-iss kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic iss-topic \
    --from-beginning
```

Check the Pinot UI here

```bash
http://localhost:9000/#/query
```

Run Streamlit App

```bash
streamlit run iss_app.py
```

## Credits

[Much thanks to Mark Needham's Conf42 Python 2022 video](https://www.youtube.com/watch?v=eXg9m2TM0dE)
