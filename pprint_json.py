import json
import sys

def load_data(filepath):
    try:
        fh = open(filepath,'r')
    except FileNotFoundError:
        print("Файл не найден!")
        exit(1)
    except OSError:
        print("Неожиданная ошибка!")
        exit(1)
    try:
        data = json.load(fh)
    except:
        print("Это не json формат!")
        exit(1)
    return data

def pretty_print_json(data):
    """Выводить каждый параметром с отступом в два пробела и сортировать, учитывать UTF-8"""
    print(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ожидается путь к файлу json.")
    else:
        pretty_print_json(load_data(sys.argv[1]))
