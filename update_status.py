from final import status

print('Текущий статус заметки: ',status)
status = ['Выполнено', 'В процессе', 'Отложено']
print('Измените текущий статус заметки: ')
for i in status:
    print(f'{status.index(i)+1}. {i}')
while True:
    new_status = input('Ваш выбор: ').capitalize()
    try:
        if int(new_status) < len(status)+1:
            print(f'Статус заметки успешно обновлен на: "{status[int(new_status) - 1]}"')
            break
        else:
            print('Введите корректное значение: ')
    except ValueError:
        if str(new_status) in status:
            print(f'Статус заметки успешно обновлен на: "{new_status}"')
            break
        else:
            print('Введите корректное значение: ')


