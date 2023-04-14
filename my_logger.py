import logging

logger_parser = logging.getLogger('parser')
cons_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f'logs/parser_log.txt', mode='a')
cons_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)
cons_format = logging.Formatter(
    '%(levelname)s||| %(message)s')
file_format = logging.Formatter(
    '%(asctime)s||| %(message)s', datefmt='%H:%M:%S')
cons_handler.setFormatter(cons_format)
file_handler.setFormatter(file_format)

logger_parser.addHandler(cons_handler)
logger_parser.addHandler(file_handler)

logger_view = logging.getLogger('dj_view')
cons_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f'logs/view_log.txt', mode='a')
cons_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)
cons_format = logging.Formatter(
    '%(levelname)s : %(relativeCreated)d ms %(message)s')
file_format = logging.Formatter(
    '%(asctime)s PID - %(process)d. %(relativeCreated)d ms %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
cons_handler.setFormatter(cons_format)
file_handler.setFormatter(file_format)

logger_view.addHandler(cons_handler)
logger_view.addHandler(file_handler)