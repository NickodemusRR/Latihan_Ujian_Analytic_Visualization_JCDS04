# Membuat database menggunakan MySQL

Mengaktifkan sql.
```bash
cd C:\Program Files\MySQL\MySQL Server 8.0\bin
C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql -u guest -p
```

Membuat database sekolahku.
```bash
mysql> create database sekolahku;
```

1. Membuat tabel _users_
```bash
mysql> CREATE TABLE users(
    -> id int auto_increment,
    -> username varchar(50) NOT NULL,
    -> email varchar(50) NOT NULL,
    -> password varchar(50) NOT NULL,
    -> created_at timestamp default current_timestamp,
    -> updated_at timestamp default current_timestamp ON UPDATE current_timestamp,
    -> primary key(id)
    -> );
Query OK, 0 rows affected (0.04 sec)
```

   Memasukan data ke dalam tabel _users_
```bash
mysql> INSERT INTO users(username, email, password, created_at, updated_at) values
    -> ('Andi', 'andi@andi.com', '12345', current_timestamp, current_timestamp)
    -> ('Budi', 'budi@budi.com', '67890', current_timestamp, current_timestamp),
    -> ('Caca', 'caca@caca.com', 'abcde', current_timestamp, current_timestamp),
    -> ('Deni', 'deni@deni.com', 'fghij', current_timestamp, current_timestamp),
    -> ('Euis', 'euis@euis.com', 'klmno', current_timestamp, current_timestamp),
    -> ('Fafa', 'fafa@fafa.com', 'pqrst', current_timestamp, current_timestamp);
```

2. Membuat tabel _courses_
```bash
mysql> CREATE TABLE courses(
    -> id int auto_increment,
    -> course varchar(50) NOT NULL,
    -> mentor varchar(50) NOT NULL,
    -> title varchar(50) NOT NULL,
    -> primary key(id));
```

  Memasukkan data ke tabel _courses_
```bash
mysql> INSERT INTO courses (course, mentor, title) values
    -> ('C++', 'Ari', 'Dr.'),
    -> ('C#', 'Ari', 'Dr.'),
    -> ('C#', 'Ari', 'Dr.'),
    -> ('CSS', 'Cania', 'S.Kom'),
    -> ('HTML', 'Cania', 'S.Kom'),
    -> ('Javascript', 'Cania', 'S.Kom'),
    -> ('Python', 'Barry', 'S.T.'),
    -> ('Micropython', 'Barry', 'S.T.'),
    -> ('Java', 'Darren', 'M.T.'),
    -> ('Ruby', 'Darren', 'M.T.');
```

3. Membuat tabel _userCourse_
```bash
mysql> CREATE TABLE userCourse (
    -> id_user int,
    -> id_course int);
```

   Memasukkan data ke tabel _userCourse_
```bash
mysql> INSERT INTO userCourse (id_user, id_course) values
    -> (1, 1),
    -> (1, 2),
    -> (1, 3),
    -> (2, 4),
    -> (2, 5),
    -> (2, 6),
    -> (3, 7),
    -> (3, 8),
    -> (3, 9),
    -> (4, 1),
    -> (4, 3),
    -> (4, 5),
    -> (5, 2),
    -> (5, 4),
    -> (5, 6),
    -> (6, 7),
    -> (6, 8),
    -> (6, 9);
```

4. Menggunakan __INNER JOIN__ untuk menggabungkan peserta didik dengan kelas yang diambil beserta nama mentornya.
```bash
mysql> SELECT users.id, users.username, courses.course, courses.mentor, courses.title
    -> FROM users
    -> JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id;
```

5. Menampilkan daftar peserta didik beserta mata kuliah yang diikutinya, yang mentornya bergelar sarjana.
```bash
mysql> SELECT users.id, users.username, courses.course, courses.mentor, courses.title
    -> FROM users
    -> JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> WHERE courses.title LIKE 'S%';
```

6. Menampilkan daftar peserta didik beserta mata kuliah yang diikutinya, yang mentornya bergelar selain sarjana.
```bash
mysql> SELECT users.id, users.username, courses.course, courses.mentor, courses.title
    -> FROM users
    -> JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> WHERE courses.title NOT LIKE 'S%';
```

7. Menampilkan jumlah peserta didik untuk setiap mata kuliah.
```bash
mysql> SELECT courses.course, courses.mentor, courses.title, COUNT(users.username) AS jumlah_peserta
    FROM users
    JOIN userCourse
    ON users.id = userCourse.id_user
    JOIN courses
    ON userCourse.id_course = courses.id
    GROUP BY courses.course;
```

8. Menampilkan total fee untuk setiap mentor dengan besaran fee per peserta Rp. 2.000.000,-
```bash
mysql> SELECT courses.mentor, COUNT(users.username) AS 'jumlah_peserta', COUNT(users.username)*2000000 AS 'total_fee'
    -> FROM users
    -> JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> GROUP BY 1;
```