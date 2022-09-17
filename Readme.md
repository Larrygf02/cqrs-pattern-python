# Implement CQRS pattern with python

## Architecture
![Diagram](https://raw.githubusercontent.com/Larrygf02/cqrs-pattern-python/master/CQRS.pattern.drawio.png)

## Init DB postgres
```
create database sync-demo
create table products (
    id serial primary key,
    name varchar(50),
    cantidad int,
    precio numeric(5,1)
)
```

## Init mongodb (studio3T)

```
create database sync-demo
```

## Start rabbitmq
```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

## Creat environment
In directory sync-data
```
virtualenv .venv
source .venv/bin/activate (Mac)
pip install -r requirements.txt
```

## Start producer
In directory sync-data/producer
```
flask --app app run
```

## Start consumer
In directory sync-data/consumer 
```
python consumer.py
```

## Start client
In directory front, initialize server in index.html
![Diagram](https://raw.githubusercontent.com/Larrygf02/cqrs-pattern-python/master/client.png)