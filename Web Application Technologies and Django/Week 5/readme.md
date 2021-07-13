This week I learned about how database systems work and the basic operations in SQL.

Reference sources:
- https://www.dj4e.com/lectures/SQL-01-Basics.txt
- https://www.sqlite.org/cli.html

### Commands used in last activity

```console
$ cd ~
$ sqlite3 pitch.sqlite3
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.

$ sqlite> CREATE TABLE Ages ( 
   ...>   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
   ...>   name VARCHAR(128), 
   ...>   age INTEGER
   ...> );

$ sqlite> INSERT INTO Ages (name, age) VALUES ('Idun', 36);
$ sqlite> INSERT INTO Ages (name, age) VALUES ('Thirza', 13);
$ sqlite> INSERT INTO Ages (name, age) VALUES ('Jeni', 36);
$ sqlite> INSERT INTO Ages (name, age) VALUES ('Kylan', 31);
$ sqlite> INSERT INTO Ages (name, age) VALUES ('Suman', 39);
$ sqlite> INSERT INTO Ages (name, age) VALUES ('Paul', 14);

$ sqlite> .mode column
$ sqlite> select * from ages;
1           Idun        36        
2           Thirza      13        
3           Jeni        36        
4           Kylan       31        
5           Suman       39        
6           Paul        14
$ sqlite> SELECT hex(name || age) AS X FROM Ages ORDER BY X;
4964756E3336
4A656E693336
4B796C616E33
5061756C3134
53756D616E33
546869727A61
$ sqlite> .quit
```
