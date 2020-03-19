2 файла: ...///-users.py & ...-find_athlete.py + в текущий каталог положить базу sochi_athletes.sqlite3

1) используя ...-users.py можно добавить пользователя, но нужно учесть, что user.height в см (175.0), а user.birthdate в формате: "01.01.1994"
sqlite> select * from user;
1|n1|f1|Male|n1@mail.any||175.0
2|n2|f2|Male|n2@mail.any|02.01.01.01.19941998|182.0
3|n3|f3|Male|n3@mail.any|03.01.1995|185.0
4|n4|f4|Female|n4@mail.any|04.01.1996|170.0

2) используя ...-find_athlete.py можно найти ближайших к пользователю по росту и дате рождения атлетов:
PS C:\ESNdocs\edX-Py\B4-sqllite> python B4-12-HW-sqlalchemy-find_athlete.py
Привет!
Введи своё имя: n3
Пользователь n3 f3 185.0 1995-01-03 00:00:00
Атлет, ближайший по росту Aaron March 1.85 0.0 1986-05-14 Snowboard
Атлет, ближайший по дате рождения Je-yun Park 1.75 1994-12-30 -4 Alpine Skiing
