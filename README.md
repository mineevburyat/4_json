# Prettify JSON

Загружает данные из json файла и выводит в удобном для чтения виде.

# Quickstart

Example of script launch on Linux, Python 3.5:
Файл json.js имеет содержит строку вида:
[{"Id":"79742784-9ef3-4543-bc98-a219a8903c18","Number":1,"Cells":{"global_id":14371450,"Name":"Ароматный Мир","IsNetObject":"да","OperatingCompany":"Ароматный Мир", ...}]

```#!bash

$ python pprint_json.py json.js
[
  {
    "Cells": {
      "Address": "улица Академика Павлова, дом 10",
      "AdmArea": "Западный административный округ",
      "ClarificationOfWorkingHours": null,
...
  }
]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
