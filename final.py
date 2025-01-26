name = input("Введите имя пользователя: ")
content = input("Название заметки: ")
status = input("определите статус заметки: ")
created_date = input("Введите дату создания: ")
issue_date = input("Введите дату изменения: ")
title1 = input("Введите заголовок 1: ")
title2 = input("Введите заголовок 2: ")
note = [ name, content, status, created_date, issue_date, [title1,  title2]]
print(f"Имя пользователя: {name}, \nдата создания: {created_date[0:5]}, \nдата завершения: {issue_date[0:5]},"
      f"\nстатус заметки: {status}, \nНазвание заметки: {content}, \n{title1}, {title2}")
