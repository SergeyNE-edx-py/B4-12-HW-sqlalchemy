# Задание 2
# Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:

# запросить идентификатор пользователя;
# если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
# если пользователя с таким идентификатором нет, вывести соответствующее сообщение.

# импортируем модули стандартной библиотеки datetime
import datetime as dt

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

# CREATE TABLE athelete("id" integer primary key autoincrement, "age" integer,"birthdate" text,"gender" text,"height" real,"name" text,"weight" integer,"gold_medals" integer,"silver_medals" integer,"bronze_medals" integer,"total_medals" integer,"sport" text,"country" text);
class Athelete(Base):
    """
    Описывает структуру таблицы athelete 
    """
    # задаем название таблицы
    __tablename__ = 'athelete'
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True)
    # имя атлета
    name = sa.Column(sa.Text)
    # # фамилия пользователя
    sport = sa.Column(sa.Text)
    # # дата рождения
    birthdate = sa.Column(sa.Text)
    # # рост, м, float
    height = sa.Column(sa.Float)


# user — для хранения регистрационных данных пользователей
# CREATE TABLE user(
# "id" integer primary key autoincrement, 
# "first_name" text, 
# "last_name" text, 
# "gender" text, 
# "email" text, 
# "birthdate" text, 
# "height" real);
class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # # пол
    gender = sa.Column(sa.Text)
    # # адрес электронной почты пользователя
    email = sa.Column(sa.Text)
    # # дата рождения
    birthdate = sa.Column(sa.Text)
    # # рост, м, float 4.2
    height = sa.Column(sa.Float)

def main():
    engine = sa.create_engine(DB_PATH)
    Sessions = sessionmaker(engine)
    session = Sessions()

    # выводим приветствие
    print("Привет!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")

    # ищем записи в таблице User, у которых поле User.first_name совпадает с параметром name
    u = session.query(User).filter(User.first_name == first_name).first()
    if u:
        atheletes = session.query(Athelete).all()
        a1 = a2 = atheletes[0]
        u_birthdate = dt.datetime.strptime(u.birthdate, '%d.%m.%Y')
        for a in atheletes:
            if(a.height == None): a.height = 0
            if abs(a.height - u.height/100) < abs(a1.height - u.height/100): 
                a1 = a
            a2_birthdate = dt.datetime.strptime(a2.birthdate, '%Y-%m-%d')
            a_birthdate = dt.datetime.strptime(a.birthdate, '%Y-%m-%d')
            if abs((a_birthdate - u_birthdate).days) < abs((a2_birthdate - u_birthdate).days): 
                a2 = a

        print("Пользователь "+first_name, u.last_name, u.height, u_birthdate)
        print("Атлет, ближайший по росту "+a1.name, a1.height, a1.height - u.height/100, a1.birthdate, a1.sport)
        a2_birthdate = dt.datetime.strptime(a2.birthdate, '%Y-%m-%d')
        print("Атлет, ближайший по дате рождения "+a2.name, a2.height, a2.birthdate, (a2_birthdate - u_birthdate).days, a2.sport)

    else:
        print("Пользователь "+first_name+" не зарегистрирован")


if __name__ == "__main__":
    main()