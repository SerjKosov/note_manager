print('Добро пожаловатьв в "Менеджер заметок"!')
note = []
while True:
    name = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки: ')
    status = input('Введите статус заметки (новая, в процессе, выполнено): ')
    create_date = input('Введите дату создания заметки: ')
    issue_date = input('Введите дату дедлайна: ')
    remark = [name, title, content, create_date, issue_date]
    note.append(remark)
    if input('Хотите добавить новую заметку введите да, если нет просто нажми "Enter": ').lower() in 'да':
        continue
    else:
        break
for i in note:
    print(note.index(i)+1, end='. ' )
    print(f'Имя: {name}\n  Заголовок: {title}\n  Описание: {content}\n  Статус: {status}\n  Дата создания: {create_date}\n  Дата дедлайна: {issue_date}')
