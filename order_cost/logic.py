from .models import Offset_model, Riso_model, Solvent_model
from .parsers.parser import parce_m_grup


def check_in_db(order_info):  # функцию для проверки наличия в бд,
    # или декоратор, который сразу проверяет если есть отдает
    pass


def solvent_calc(order_info: dict):

    type_prod_sol, width, higth = order_info['type_prod'], order_info['width'], order_info['higth']

    if Solvent_model.objects.filter(type_prod=type_prod_sol):
        cost_per_m2 = Solvent_model.objects.filter(
            type_prod=type_prod_sol).order_by('-date')[0].cost
        result = cost_per_m2 * width * higth
    else:
        return f'Нет в таблице материала - {type_sol}'
    return result


def offset_calc(order_info: dict):
    formatX, formatY, density, pressrun, duplex = [
        i for i in list(order_info.values())[1:]]

    target_query = Offset_model.objects.filter(
        formatX=formatX, formatY=formatY, pressrun=pressrun, duplex=duplex)
    if target_query.exists():  # if query in db return result = cost
        return target_query.get().cost

    result_from_parce = parce_m_grup(
        formatX, formatY, density, pressrun, duplex)
    print(result_from_parce)
    if result_from_parce != 'not result':
        cost = int(''.join(result_from_parce.split(' '))) # to integer
    else: return 'Try again'

    save_to_db(order_info, cost=cost)

    return cost


def riso_calc(order_info: dict):
    if 'pressrun' not in order_info.keys():
        Riso_model.objects.create(paper_cost_80=order_info['paper_cost_80'],
                                  black_ink_cost=order_info['black_ink_cost'],
                                  master_list_cost=order_info['master_list_cost'])
    else:
        last_update = Riso_model.objects.order_by('-date')[0]
        one_list_cost = (last_update.paper_cost_80 / 500) + (last_update.black_ink_cost / 5000)
        result = int(order_info['pressrun']) * one_list_cost + (last_update.master_list_cost / 20)
        return round(result, 2)


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
    else:
        return None


def save_to_db(order_info, **kwargs):

    if order_info.get('type_order') == 'solvent':
        new_cost = Solvent_model(type_prod=order_info['type_prod'],
                                 cost=order_info['cost'])
    elif order_info.get('type_order') == 'offset':
        cost = kwargs.get('cost')
        new_cost = Offset_model(formatX=order_info['formatX'],
                                formatY=order_info['formatY'],
                                density=order_info['density'],
                                pressrun=order_info['pressrun'],
                                duplex=order_info['duplex'],
                                cost=cost)

    new_cost.save()


# https://django.fun/ru/docs/django/4.1/topics/db/queries/ - !!!
