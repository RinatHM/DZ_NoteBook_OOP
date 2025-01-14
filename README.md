# Notebook Application

## Описание
Простое приложение записной книжки с использованием архитектурного паттерна MVC и соблюдением принципов SOLID.

## Установка

1. Убедитесь, что у вас установлен Python (версия 3.6 и выше). Скачать можно [здесь](https://www.python.org/downloads/).
2. Склонируйте репозиторий или загрузите архив с проектом.
3. Перейдите в директорию проекта в командной строке:
    ```
    cd notebook
    ```
4. Создайте виртуальное окружение:
    ```
    python -m venv venv
    ```
5. Активируйте виртуальное окружение:
    - Для Windows:
        ```
        venv\Scripts\activate
        ```
    - Для macOS и Linux:
        ```
        source venv/bin/activate
        ```
6. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```

## Запуск

1. Активируйте виртуальное окружение (если еще не активировано).
2. Запустите приложение:
    ```
    python main.py
    ```

## Использование

Следуйте инструкциям в меню для добавления, просмотра, обновления и удаления заметок.

## Логирование

Все ключевые действия (добавление, обновление, удаление заметок) логируются в консоль.
