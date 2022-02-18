# Тестовое задание к проекту "Large Scale Analysis of Code Quality"
Овчаренко Анатолий, CSC
## Описание окружения
Используется `Python 3.9.10`. Установленные библиотеки включают в себя:
1. Библиотеки, описанные в файле [`requirements.txt`](https://github.com/hyperskill/hyperstyle-analyze/blob/main/requirements.txt) репозитория [`hyperstyle-analyze`](https://github.com/hyperskill/hyperstyle-analyze);
2. Библиотеки из аналогичного файла [`requirements-test.txt`](https://github.com/hyperskill/hyperstyle-analyze/blob/main/requirements-test.txt);
3. Библиотеки из файла [`requirements-roberta.txt`](https://github.com/hyperskill/hyperstyle-analyze/blob/main/requirements-roberta.txt);
4. Некоторые дополнительные библиотеки, использованные при анализе: `matplotlib`

Все указанные библиотеки с соответствующими версиями описаны в файле [`requirements.txt`](https://github.com/tolber01/code_quality_test_task/blob/main/requirements.txt) настоящего репозитория.

При извлечении данных активно использовался инструмент `hyperstyle-analyze`, а именно его [fork-версия](https://github.com/tolber01/hyperstyle-analyze) (см. ветку `hyperstyle-analysis-fixes`), в которой были выполнены минорные исправления формата возвращаемых из API Hyperskill данных по решениям.

## Описание извлеченных данных
Данные извлекались с использованием скрипта [`scrape_data.py`](https://github.com/tolber01/code_quality_test_task/blob/main/scrape_data.py). В качестве источника был выбран Hyperskill. В треке `Python for Beginners` выбраны 4 степа с базовыми задачами на программирование и алгоритмизацию:
1. [6818](https://hyperskill.org/learn/step/6818): `A mean of n.` -- задача на использование цикла `for`
2. [8443](https://hyperskill.org/learn/step/8443): `Coordinates` -- задача на использование условных конструкций (`elif` в частности)
3. [9480](https://hyperskill.org/learn/step/9480): `Tennis tournament` -- задача на использование вложенных списочных выражений
4. [7323](https://hyperskill.org/learn/step/7323): `The sum of numbers in a range` -- задача на реализацию простого алгоритма на Python

По техническим причинам инструмент `hyperstyle` для анализа кода не использовался, вместо этого все нужные описания ошибок/замечаний в решениях были получены прямо из API.

С помощью упомянутого скрипта в общей сложности была выгружена информация о 2272 решениях, а также описания рассматриваемых степов. Извлеченные данные в виде двух таблиц `.csv` и одного `.json` файла сохранялись в локальную папку `data`.

Структура таблиц:
1. `submissions.csv` -- файл с описанием решений:
1.1. `id` -- идентификатор решения (`int`)
1.2. `step` -- идентификатор степа (`int`)
1.3. `status` -- статус решения (`correct`, `wrong` и др.)
1.4. `time`
1.5. `lang` -- язык программирования, на котором реализовано решение (в нашем случае только `python3`)
1.6. `code` -- исходный код решения
2. `steps.csv` -- файл с описанием степов:
2.1. `id` -- идентификатор степа (`int`)
2.2. `seconds_to_complete` -- среднее время выполнения (`float`)
2.3. `solved_by` -- количество решивших степ
2.4. `success_rate` -- доля успешных решений
3. `submissions_feedbacks.json` -- файл с извлеченной для каждого решения информацией об ошибках и качестве кода

## Анализ собранных данных
См. Jupyter Notebook [`analysis.ipynb`](https://github.com/tolber01/code_quality_test_task/blob/main/analysis.ipynb) 
