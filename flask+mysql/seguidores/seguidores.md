# Seguidores

## Crear 6 usuarios
``` 

insert into usuarios(nombre, apellido, email) values('user1', 'Apellido1', 'u1@gmail.com');
insert into usuarios(nombre, apellido, email) values('user2', 'Apellido2', 'u2@gmail.com');
insert into usuarios(nombre, apellido, email) values('user3', 'Apellido3', 'u3@gmail.com');
insert into usuarios(nombre, apellido, email) values('user4', 'Apellido4', 'u4@gmail.com');
insert into usuarios(nombre, apellido, email) values('user5', 'Apellido5', 'u5@gmail.com');
insert into usuarios(nombre, apellido, email) values('user6', 'Apellido6', 'u6@gmail.com');

```

### Consulta: Haz que el usuario 1 sea seguidor del usuario 3, 4 y 5
```
insert into seguidores(usuario_id, seguidor_id) values(3, 1);
insert into seguidores(usuario_id, seguidor_id) values(4, 1);
insert into seguidores(usuario_id, seguidor_id) values(5, 1);
```

### Consulta: Haz que el usuario 2 sea seguidor del usuario 1, 3 y 6
```
insert into seguidores(usuario_id, seguidor_id) values(1, 2);
insert into seguidores(usuario_id, seguidor_id) values(3, 2);
insert into seguidores(usuario_id, seguidor_id) values(6, 2);
```
### Consulta: Haz que el usuario 3 sea seguidor del usuario 2 y 6

```
insert into seguidores(usuario_id, seguidor_id) values(2, 3);
insert into seguidores(usuario_id, seguidor_id) values(6, 3);
```

### Consulta: Haz que el usuario 4 sea seguidor del usuario 2
```
insert into seguidores(usuario_id, seguidor_id) values(2, 4);
```
### Consulta: Haz que el usuario 5 sea seguidor del usuario 3 y 6
```
insert into seguidores(usuario_id, seguidor_id) values(3,5);
insert into seguidores(usuario_id, seguidor_id) values(6,5);
```
### Consulta: Haz que el usuario 6 sea seguidor del usuario 1
```	
insert into seguidores(usuario_id, seguidor_id) values(1,6);
```

### muestra las relaciones creadas en una tabla con las columnas: nombre_usuario, apellido_usuario, nombre_seguidor, apellido_seguidor
```
select u1.nombre as nombre_usuario, u1.apellido as apellido_usuario, u2.nombre as nombre_seguidor, u2.apellido as apellido_seguidor
from usuarios u1
inner join seguidores s on u1.id = s.usuario_id
left join usuarios u2 on s.seguidor_id = u2.id;


+----------------+------------------+-----------------+-------------------+
| nombre_usuario | apellido_usuario | nombre_seguidor | apellido_seguidor |
+----------------+------------------+-----------------+-------------------+
| user1          | Apellido1        | user2           | Apellido2         |
| user1          | Apellido1        | user6           | Apellido6         |
| user2          | Apellido2        | user3           | Apellido3         |
| user2          | Apellido2        | user4           | Apellido4         |
| user3          | Apellido3        | user1           | Apellido1         |
| user3          | Apellido3        | user2           | Apellido2         |
| user3          | Apellido3        | user5           | Apellido5         |
| user4          | Apellido4        | user1           | Apellido1         |
| user5          | Apellido5        | user1           | Apellido1         |
| user6          | Apellido6        | user2           | Apellido2         |
| user6          | Apellido6        | user3           | Apellido3         |
| user6          | Apellido6        | user5           | Apellido5         |
+----------------+------------------+-----------------+-------------------+
```
### Bonus: Devuelve todos los usuarios que son seguidores del primer usuario, mostrando sus nombres.
```
select u2.nombre as nombre_seguidor
from usuarios u1
inner join seguidores s on u1.id = s.usuario_id
left join usuarios u2 on s.seguidor_id = u2.id
where u1.id = 1;
```
### Devuelve la cantidad de seguidores que hay por usuario
```
select u.nombre, count(s.seguidor_id) as seguidores
from usuarios u
left join seguidores s on u.id = s.usuario_id
group by u.id;

+--------+------------+
| nombre | seguidores |
+--------+------------+
| user1  |          2 |
| user2  |          2 |
| user3  |          3 |
| user4  |          1 |
| user5  |          1 |
| user6  |          3 |
+--------+------------+
```


### Muestra qué usuario tiene más seguidores y muestra la cantidad de seguidores que tiene
```
select u.nombre, count(s.seguidor_id) as seguidores
from usuarios u
left join seguidores s on u.id = s.usuario_id
group by u.id
order by seguidores desc
limit 3;
```

### Devuelve los seguidores del usuario 3 en orden alfabético

``` 
select u2.nombre as nombre_seguidor
from usuarios u1
inner join seguidores s on u1.id = s.usuario_id
left join usuarios u2 on s.seguidor_id = u2.id
where u1.id = 3
order by u2.nombre asc;

+-----------------+
| nombre_seguidor |
+-----------------+
| user1           |
| user2           |
| user5           |
+-----------------+
```

