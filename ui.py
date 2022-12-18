from constants import ABILITIES
from checkers import check_menu_item as chk_menu
from checkers import checker_field
import csv

def get_action():
    """Ничего не принимает на вход
    Вовзращает выбранное действие"""

    print('Из списка ниже выберете желаемое действие: ')
    for item in ABILITIES:  
        print(item)
    check=False
    while check==False:
        choise=input('Ввыбор действия: ')
        check=chk_menu(choise)
        if check==False:
            print('Что-то невнятное. Попробуйте ввод ещё раз.')
    return choise

def agree():
    """Ничего не принимает, возращает решение о том, удалять или нет- True или False"""
    dec =''
    while dec not in ('Y','N'):
        dec = input('Введите решение: Y = да, N=нет')
        if dec not in ('Y','N'):
            print('Нераспознанное решение. Определись и ответь.')
    if dec in 'Y': return True
    if dec in 'N': return False

def add_row(db_name):
    """Добавление строки в БД. Принимает базу данных, куда нужно добавить строку, ничего не возвращает"""

    return 

def row_to_modify(list_of_availible_rows):
    """Принимает список ключей, из которых можно выбрать ключ нужной строки, возвращает ключ выбранной строки"""
    while dec not in list_of_availible_rows:
        dec = input('Введите ключ строки(порядковый номер из первого столбца: )')
        if dec not in list_of_availible_rows:
            print('Нераспознанное решение. Определись и ответь.')
    return dec

def field_to_correct(db_name):
    """Принимает адрес базы данных, строку, возвращает имя заголовка поля, которое выбрано пользователем"""
    choice=''
    with open(db_name) as f:
        reader = csv.reader(f,delimiter='|')
        headers = next(reader)
        print(headers)
    
    while choice not in headers:
        choice=input('Введите наименование поля, которое нужно изменить:  ')
        if choice not in headers:
            print('Нераспознанное поле. Определись и ответь.')
    return choice


def to_input(field):
    """Принимает имя поля, в которое будет внесено изменение строки, возвращает строку, которую нужно будет вставить вмест опредыдущего значения"""
    value=''
   
    if field=='phone_num':
        print('Формат ввода: до 11 целых чисел включительно в одну строку, без символов "+", скобок и проблелов.')
    elif field in ('first_name','last_name'):
        print('Формат ввода - строка длиной до 30 из буквенных символов')
    else:
        print('Формат ввода: строка длиной до 30 симолов, без цифр.')
    chk=False
    while chk ==False:
        value=input('Введите новое значение ячейки: ')
        chk=checker_field(field,value)
        if chk==False:
            print('Некорректный форамт ввода, пробуй ещё раз.')
    return value

print(to_input('first_name'))
