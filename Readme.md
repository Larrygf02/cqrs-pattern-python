# Implement CQRS pattern with python

## Architecture


## Init DB postgres
```
create table products (
    id serial primary key,
    name varchar(50),
    cantidad int,
    precio numeric(5,1)
)
```

## Start rabbitmq
```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
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
