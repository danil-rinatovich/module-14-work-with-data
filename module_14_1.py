import sqlite3

# соединение с базой данных
connection = sqlite3.connect('not_telegram.db ')

# взаимодействие с базой данных
cursor = connection.cursor()

# создаем таблицу
cursor.execute('''                                  
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

# заполняем таблицу
for i in range(1, 11):
     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))
cursor.execute('UPDATE Users SET balance = 1000')

# изменяем таблицу
for i in range(1, 11):
    if i % 2:
        cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

# удаляем
for i in range(1, 11):
    if i % 3 == 1:
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# выводим в консоль
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for usr in users:
    print(usr)

# полностью очистить таблицу
#cursor.execute(f'DELETE FROM Users')

# сохраняем изминения в базе
connection.commit()

# закрываем соединение
connection.close()