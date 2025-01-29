note = []
while True:
    title = input("Введите заголовок заметки или оставте пустым для завершения: ")
    if title  in ('', ' '):
        break
    if title in note:
        print("Такой заголовок уже есть, попробуйте другой")
        continue
    note.append(title)
print("Заголовки заметок:")
for index, title in enumerate(note, start=1):
    print(index, title)