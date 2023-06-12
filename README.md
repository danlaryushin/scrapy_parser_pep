# Асинхронный парсер PEP


## Описание проекта

Проект содержит парсер документов PEP на базе фреймворка Scrapy

### Парсер выводит собранную информацию в два файла .csv:
1. Список всех PEP: номер, название и статус.
2. Сводка по статусам PEP 


## Инструкция по развёртыванию проекта

* клонировать проект на компьютер `git clone https://github.com/danlaryushin/scrapy_parser_pep.git`
* создание виртуального окружения `python -m venv venv`
* запуск виртуального окружения `source venv/Scripts/activate`
* установить зависимости из файла requirements.txt `pip install -r requirements.txt`
* запуск команды на старт проекта `scrapy startproject pep_parse .`
* создание паука `scrapy genspider pep peps.python.org`
* запуск паука `scrapy crawl pep`

## Автор

[Даниил Ларюшин](https://github.com/danlaryushin)