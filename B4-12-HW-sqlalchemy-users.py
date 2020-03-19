# Задание 1
# Напишите модуль users.py, который регистрирует новых пользователей. Скрипт должен запрашивать следующие данные:

# имя
# фамилию
# пол
# адрес электронной почты
# дату рождения
# рост
# Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3.

# импортируем модули стандартной библиотеки datetime
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

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
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")

    # ищем записи в таблице User, у которых поле User.first_name совпадает с параметром name
    query = session.query(User).filter(User.first_name == first_name).first()
    if query:
        print("Пользователь "+first_name+" уже существует. Измените его данные")
        query.first_name = input("Имя: "+query.first_name+": ")
        query.last_name = input("Фамилия: "+query.last_name+": ")
        query.gender = input("Пол: "+query.gender+": ")
        query.email = input("Адрес электронной почты: "+query.email+": ")
        query.birthdate = input("Дата рождения: "+query.birthdate+": ")
        query.height = input("Рост: "+str(query.height)+": ")
        print(query)
    else:
        last_name = input("А теперь фамилию: ")
        gender = input("Пол: ")
        email = input("Мне еще понадобится адрес твоей электронной почты: ")
        birthdate = input("Дата рождения: ")
        height = input("Рост: ")
        # создаем нового пользователя
        user = User(
            # id=user_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,        
            email=email,
            birthdate=birthdate,
            height=height)
            # добавляем нового пользователя в сессию
        print(user)
        session.add(user)

    # сохраняем все изменения, накопленные в сессии
    session.commit()
    print("Спасибо, данные сохранены!")

if __name__ == "__main__":
    main()