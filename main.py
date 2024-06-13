from controller.note_controller import NoteController

def main():
    controller = NoteController()
    while True:
        print("\nЗаписная книжка:")
        print("1. Добавить заметку")
        print("2. Просмотр всех заметок")
        print("3. Изменить заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Сделайте выбор: ")

        if choice == '1':
            controller.add_note()
        elif choice == '2':
            controller.view_notes()
        elif choice == '3':
            controller.update_note()
        elif choice == '4':
            controller.delete_note()
        elif choice == '5':
            print("Выход...")
            break
        else:
            print("Неправильное число. Попробуйте ещё раз")

if __name__ == "__main__":
    main()
