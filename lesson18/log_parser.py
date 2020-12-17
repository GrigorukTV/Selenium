import argparse
import re
import json
import os

parser = argparse.ArgumentParser(description='access.log')
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()


#     "Топ 10 серверных ошибок": top_server_error_10()
#     "Топ 10 IP адресов": top_time_10(),
#     "Топ 10 клиентских ошибок": top_client_error_10(),
#     "Топ 10 серверных ошибок": top_server_error_10()
# "Количество записей":count_line()
# "Топ 10 IP адресов": top_time_10()

class LogProcessor:
    # записи
    count_rec = 0
    # ip адреса
    list_ip = []
    # Время
    top_time = []
    # клиентские ошибки
    code_info = []
    # серверные ошибки
    server_errors = []
    # подсчет методов
    method_dict = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}

    list_time = []
    time_info = {}
    file = ''
    result = []

    def __init__(self, file):
        self.file = file

    # запуск
    def run(self):
        if os.path.isdir(self.file):
            for f in os.listdir(self.file):
                r = self.proceed_file(os.path.join(self.file, f))
                if r is None:
                    return 'Ошибка чтения директории'
                self.result.append(r)
        else:
            r = self.proceed_file(self.file)
            if r is None:
                return 'Ошибка чтения файла'
            self.result = self.proceed_file(self.file)

        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=4)

        return 'Все хорошо'

    # обработка файла
    def proceed_file(self, f):
        with open(f) as file:
            try:
                next(file)
            except Exception:
                return None

            for line in file.readlines():
                self.count_line()
                self.top_ip_10(line)
                self.top_time_10(line)
                self.top_client_error_10(line)
                self.top_server_error_10(line)
                self.count_method_dict(line)

            self.proceed_top_time()
        return {
            "Топ 10 серверных ошибок": self.server_errors,
            "Топ 10 IP адресов": self.list_ip,
            "Подсчет методов": self.method_dict,
            "Топ 10 клиентских ошибок": self.code_info,
            "Количество записей": self.count_rec,
            "Топ 10 долгих запросов": self.top_time
        }

    # Подсчет строчек
    def count_line(self):
        self.count_rec += 1

    # Топ 10 IP
    def top_ip_10(self, line):
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
        if ip not in self.list_ip:
            self.list_ip.append(ip)
        if len(self.list_ip) == 10:
            return

    # Топ времени
    def top_time_10(self, line):
        result_list = []

        # correct
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
        methodSearch = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
        if (methodSearch is None):
            return

        method = methodSearch.groups()[0]
        line_list = line.split()
        time = int(line_list[-1])
        if time not in self.list_time:
            self.list_time.append(time)
        if time not in self.time_info:
            self.time_info[time] = []

        self.time_info[time].append({
            "method": method,
            "url": line_list[6],
            "ip": ip,
            "time": str(time)
        })

    # обработка результатов поиска времени выполнения
    def proceed_top_time(self):
        sorted_list = sorted(self.list_time, reverse=True)[:10]
        for time in sorted_list:
            for el in self.time_info[time]:
                if len(self.top_time) < 10:
                    self.top_time.append(el)
                else:
                    return

    # Ошибки клиента
    def top_client_error_10(self, line):
        if len(self.code_info) == 10:
            return
        code = re.search(r"\"\ (400|401|403|405|404)", line)
        if code is not None:
            code = code.groups()[0]
            line_list = line.split()
            self.code_info.append({
                "method": re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0],
                "url": line_list[6],
                "ip": re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group(),
                "code": str(code)
            })

    # Ошибки сервера
    def top_server_error_10(self, line):
        if len(self.server_errors) == 10:
            return
        code = re.search(r"\"\ (500|502|503|504|520)", line)
        if code is not None:
            code = code.groups()[0]
            line_list = line.split()
            self.server_errors.append({
                "method": re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0],
                "url": line_list[6],
                "ip": re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group(),
                "code": str(code)
            })

    # подсчет методов
    def count_method_dict(self, line):
        method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
        if method is not None:
            method = method.groups()[0]

            self.method_dict[method] += 1


cl = LogProcessor(args.file)
cl.run()

