import json
import sys

def load_data(filepath):
    """Открыть json файл, загрузить и передать данные"""
    try:
        file_handler = open(filepath,'r')
    except FileNotFoundError:
        print("Файл не найден!")
        exit(1)
    except OSError:
        print("Неожиданная ошибка!")
        exit(1)
    try:
        jsondata = json.load(file_handler)
    except:
        print("Это не json формат!")
        exit(1)
    file_handler.close()
    return jsondata

def pretty_print_json(json_data):
    """Выводить каждый параметром с отступом в два пробела, сортировать и учитывать UTF-8"""
    print(json.dumps(json_data, sort_keys=True, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ожидается параметр - путь к файлу json.(python3 pprint_json.py <path_to_file>)")
    else:
        pretty_print_json(load_data(sys.argv[1]))
