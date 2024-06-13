from model.note import Note
from view.console_view import ConsoleView
import logging

logging.basicConfig(level=logging.INFO)

class NoteController:
    def __init__(self):
        self.notes = []
        self.view = ConsoleView()

    def add_note(self):
        title = self.view.get_input("Введите название заметки: ")
        content = self.view.get_input("Введите текст заметки: ")
        note = Note(title, content)
        self.notes.append(note)
        logging.info(f'Добавлена заметка: {title}')
        self.view.display("Заметка успешно добавлена.")

    def view_notes(self):
        if not self.notes:
            self.view.display("Заметка не найдена.")
        else:
            for note in self.notes:
                self.view.display(str(note))

    def update_note(self):
        title = self.view.get_input("Введите название заметки для обновления: ")
        note = next((note for note in self.notes if note.title == title), None)
        if note:
            new_content = self.view.get_input("Введите новый текст заметки: ")
            note.update_content(new_content)
            self.view.display("Заметка успешно обновлена.")
        else:
            self.view.display("Заметка не найдена.")

    def delete_note(self):
        title = self.view.get_input("введите название заметки для удаления: ")
        self.notes = [note for note in self.notes if note.title != title]
        logging.info(f'Удалена заметка: {title}')
        self.view.display("Заметка удалена.")
