# Core Canciones


## Consulta: Crea 5 usuarios nuevos
```
insert into usuarios(nombre, email, contrasena) values('user1', 'u1@gmail.com', 'contraseña1');
insert into usuarios(nombre, email, contrasena) values('user2', 'u2@gmail.com', 'contraseña2');
insert into usuarios(nombre, email, contrasena) values('user3', 'u3@gmail.com', 'contraseña3');
insert into usuarios(nombre, email, contrasena) values('user4', 'u4@gmail.com', 'contraseña4');
insert into usuarios(nombre, email, contrasena) values('user5', 'u5@gmail.com',  'contraseña5');

+----+--------+--------------+-------------+---------------------+---------------------+
| id | nombre | email        | contrasena  | created_at          | updated_at          |
+----+--------+--------------+-------------+---------------------+---------------------+
|  1 | user1  | u1@gmail.com | contraseña1 | 2024-11-15 17:52:38 | 2024-11-15 17:52:38 |
|  2 | user2  | u2@gmail.com | contraseña2 | 2024-11-15 17:52:38 | 2024-11-15 17:52:38 |
|  3 | Miyagi | u3@gmail.com | contraseña3 | 2024-11-15 17:52:38 | 2024-11-15 18:00:53 |
|  4 | user4  | u4@gmail.com | contraseña4 | 2024-11-15 17:52:38 | 2024-11-15 17:52:38 |
|  5 | user5  | u5@gmail.com | contraseña5 | 2024-11-15 17:52:39 | 2024-11-15 17:52:39 |
+----+--------+--------------+-------------+---------------------+---------------------+

```

## Consulta: Crea 5 canciones (¡usa los datos de tus canciones favoritas!) nuevas
```
insert into canciones(titulo, artista) values('Like Stone', 'Audioslave');
insert into canciones(titulo, artista) values('The Pretender', 'Foo Fighters');
insert into canciones(titulo, artista) values('The Real Slim Shady', 'Eminem');
insert into canciones(titulo, artista) values('KINTSUGI', 'Humbe');
insert into canciones(titulo, artista) values('Black diamond', 'Stratovarius');

+----+---------------------+--------------+---------------------+---------------------+
| id | titulo              | artista      | created_at          | updated_at          |
+----+---------------------+--------------+---------------------+---------------------+
|  7 | Like Stone          | Audioslave   | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
|  8 | The Pretender       | Foo Fighters | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
|  9 | The Real Slim Shady | Eminem       | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
| 10 | KINTSUGI            | Humbe        | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
| 11 | Black diamond       | Stratovarius | 2024-11-15 17:59:39 | 2024-11-15 17:59:39 |
+----+---------------------+--------------+---------------------+---------------------+
```
## Consulta: Cambia el nombre del tercer usuario a Miyagi

```
UPDATE usuarios SET nombre = 'Miyagi' WHERE id = 3;
```

## Consulta: Cambia el nombre de la primera canción a Macarena
```
UPDATE canciones SET titulo = 'Macarena' WHERE id = 7;
+----+---------------------+--------------+---------------------+---------------------+
| id | titulo              | artista      | created_at          | updated_at          |
+----+---------------------+--------------+---------------------+---------------------+
|  7 | Macarena            | Audioslave   | 2024-11-15 17:59:38 | 2024-11-15 18:03:26 |
|  8 | The Pretender       | Foo Fighters | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
|  9 | The Real Slim Shady | Eminem       | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
| 10 | KINTSUGI            | Humbe        | 2024-11-15 17:59:38 | 2024-11-15 17:59:38 |
| 11 | Black diamond       | Stratovarius | 2024-11-15 17:59:39 | 2024-11-15 17:59:39 |
+----+---------------------+--------------+---------------------+---------------------+
```
## Consulta: Haz que el primer usuario marque como favoritas las 3 primeras canciones

```
INSERT INTO favoritos(usuario_id, cancion_id) VALUES(1, 7), (1, 8), (1, 9);

```

## Consulta: Haz que el segundo usuario marque como favoritas las 2 primeras canciones
```
INSERT INTO favoritos(usuario_id, cancion_id) VALUES(2, 7), (2, 8);
```
## Consulta: Haz que el tercer usuario marque como favoritas las 4 primeras canciones
```
INSERT INTO favoritos(usuario_id, cancion_id) VALUES(3, 7), (3, 8), (3, 9), (3, 10);
```

## Consulta: Haz que el cuarto usuario marque como favoritas todas las canciones
```
INSERT INTO favoritos(usuario_id, cancion_id) VALUES(4, 7), (4, 8), (4, 9), (4, 10), (4, 11);

+------------+------------+
| usuario_id | cancion_id |
+------------+------------+
|          1 |          7 |
|          1 |          8 |
|          1 |          9 |
|          2 |          7 |
|          2 |          8 |
|          3 |          7 |
|          3 |          8 |
|          3 |          9 |
|          3 |         10 |
|          4 |          7 |
|          4 |          8 |
|          4 |          9 |
|          4 |         10 |
|          4 |         11 |
+------------+------------+
```
## Consulta: Haz que el quinto usuario marque como favorita la primera canción

```
INSERT INTO favoritos(usuario_id, cancion_id) VALUES(5, 7);
```
## Consulta: Recupera todos los usuarios que hayan marcado como favorita la tercera canción
```
select usuarios.id, usuarios.nombre, favoritos.cancion_id from usuarios
join favoritos on usuarios.id = usuario_id
join canciones on canciones.id = cancion_id
where favoritos.cancion_id = 9;
```

## Consulta: Recupera todas las canciones que el segundo usuario marcó como favoritas
```
mysql> select canciones.id, canciones.titulo, canciones.artista from canciones
    -> join favoritos on canciones.id = cancion_id
    -> join usuarios on usuarios.id = usuario_id
    -> where usuarios.id = 2;
+----+---------------+--------------+
| id | titulo        | artista      |
+----+---------------+--------------+
|  7 | Macarena      | Audioslave   |
|  8 | The Pretender | Foo Fighters |
+----+---------------+--------------+
```
