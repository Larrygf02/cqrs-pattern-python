# Start rabbitmq
```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

# Start producer
```
flask --app app run
```

# Start consumer
```
python consumer.py
```

# Init DB postgres
```
create table products (
    id serial primary key,
    name varchar(50),
    cantidad int,
    precio numeric(5,1)
)
```

