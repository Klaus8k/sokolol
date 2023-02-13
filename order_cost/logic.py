from .models import Offset_model, Solvent_model
from .parsers.parser import parce_m_grup


def check_in_db(order_info):
    pass


def solvent_calc(order_info: dict):

    type_sol, width, higth = order_info['type'], order_info['width'], order_info['higth']

    if Solvent_model.objects.filter(type=type_sol):
        cost_per_m2 = Solvent_model.objects.filter(
            type=type_sol).order_by('-date')[0].cost
        result = cost_per_m2 * width * higth
    else:
        return f'Нет в таблице материала - {type_sol}'
    return result


def offset_calc(order_info: dict):
    formatX, formatY, density, pressrun, duplex = [
        i for i in list(order_info.values())[1:]]

    x = parce_m_grup(formatX, formatY, density, pressrun, duplex)
    order_info['cost'] = int(''.join(x.split(' '))) # Проверка на инт

    save_to_db(order_info)

    # Здесь проверка наличия в модели записи с такими же параметрами
    # если нет такого то идем в парсер
    return x


def riso_calc(order_info):
    pass


def stamp_calc(order_info):
    pass


def oki_calc(order_info):
    pass


def check_db_or_calc_and_save(order_info):
    # Можно сделать объект, который будет в базу ходить и аргументы в параметру разбирать
    type_order_request = order_info.get('type_order')

    # Возвращается результат из дб, что бы не парсить
    if type_order_request == 'offset':
        return offset_calc(order_info)
    elif type_order_request == 'solvent':
        return solvent_calc(order_info)
    elif type_order_request == 'riso':
        return riso_calc(order_info)
    elif type_order_request == 'stam':
        return stamp_calc(order_info)
    elif type_order_request == 'oki':
        return oki_calc(order_info)
    else:
        return None


def save_to_db(order_info):

    if order_info.get('type_order') == 'solvent':
        new_cost = Solvent_model(type=order_info['type'],
                                 cost=order_info['cost'])
    elif order_info.get('type_order') == 'offset':

        new_cost = Offset_model(formatX=order_info['formatX'],
                                 formatY=order_info['formatY'],
                                 density=order_info['density'],
                                 pressrun=order_info['pressrun'],
                                 duplex=order_info['duplex'],
                                 cost=order_info['cost'])

    new_cost.save()



# https://django.fun/ru/docs/django/4.1/topics/db/queries/ - !!!
