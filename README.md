# Виджет банковских операций клиента
#### *Проект находится на стадии разработки*
## Реализованы функции:
+ **Файл masks.py**
+ + *get_mask_card_number* - преобразует номер карты в маску карты
+ + *get_mask_account* - преобразует номер счета в маску счета
+ + Так же реализовано логирование файла в отдельной дериктории logs
+ **Файл widget.py**
+ + *mask_account_card* - возвращает имя карты или счет с их масками
+ + *get_data* - взвращает дату операции
+ **Файл processing.py**
+ + *filter_by_state* - возвращающая список операций с определенным состоянием
+ + *sort_by_date* - возвращает отсортированные операции по дате
+ **Файл generators.py**
+ + *filter_by_currency* - фильтрует транзакции по типу валюты
+ + *transaction_descriptions* - возвращает описание операции
+ + *generate_card_num* - генерирует номер карты с указанием интервала
+ **Файл decorators.py**
+ + *В модуле реализуются генераторы проекта для отслеживания работы системы и 
быстрого реагирования на ошибки*
+ **Файл external_api.py**
+ + *convert_exchange_rate* - Функция направляет запрос на конвертер валют и возращает актуальный курс
+ + *summ_amount* - Функция принимает на вход транзакцию и возвращает сумму транзакции (amount ) в рублях
+ **Файл utils.py**
+ + *get_transactions* - Возвращает список словарей, содержащих данные об транзакциях
+ + Так же реализовано логирование файла в отдельной дериктории logs
+  **Файл utils_csv_xlsx.py**
+ + Содержит в себе функции для чтения файлов определенного формата (csv, xlsx)
+ + *get_transactions_csv* - возвращает список словарей, содержащих данные об транзакциях из CSV файла
+ + *get_transactions_xlsx* - возвращает список словарей, содержащих данные об транзакциях из XLSX файла

## Команда проекта
+ Елена Черноталова - студент Skypro
+ Незаменимая поддержка-консультация - команда наставников Skypro

## **Тестирование**
### Пакет tests
#### В модулях расположены тесты разработанные с помощью pytest 
#### Запускать проверку соответствующих модулей нужно по отдельности
#### Добавлены тесты генераторов

## Для улыбки и заряда эмоций 
![Улыбнись](https://kaifolog.ru/uploads/posts/2020-06/1592383368_002.jpg)
