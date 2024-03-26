import json
import os

notes = []


def add_note(note):
    notes.append(note)


def show_notes():
    for note in notes:
        print(note)


def delete_note(index):
    del notes[index]


def save_notes(file_name):
    with open(file_name, 'w') as file:
        json.dump(notes, file)


def load_notes(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            notes = json.load(file)
    else:
        print("Файл не найден")


def add_note_with_save(note, file_name):
    add_note(note)
    save_notes(file_name)


def delete_note_with_save(index, file_name):
    delete_note(index)
    save_notes(file_name)


def show_notes_with_save(file_name):
    show_notes()
    save_notes(file_name)


def load_notes_and_clear(file_name):
    load_notes(file_name)
    notes.clear()


def clear_notes():
    notes.clear()


def run():
    command = input("Введите команду: ")
    if command == 'add':
        note = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        add_note({'заголовок заметки': note, 'тело заметки': body})
        print("Заметка успешно сохранена")
    elif command == 'show':
        show_notes()
    elif command == 'delete':
        show_notes()
        index = int(input("Введите индекс заметки для удаления: "))
        delete_note(index)
    elif command == 'save':
        file_name = input("Введите имя файла для сохранения: ")
        save_notes(file_name)
    elif command == 'load':
        file_name = input("Введите имя файла для загрузки: ")
        load_notes(file_name)
    elif command == 'clear':
        clear_notes()
    else:
        print("Неверная команда. Попробуйте еще раз.")
    run()


run()
