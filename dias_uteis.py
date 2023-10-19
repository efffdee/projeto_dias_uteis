import datetime as dt
from workdays import networkdays
import holidays

print("\n")

print("++++++++++++++++++++++++++++++")
print("Seja bem vindo ao ConsultaMax!")
print("++++++++++++++++++++++++++++++")

print("\n")

# Função para formatar a entrada da data com barras
def format_date_input(input_date):
    return input_date[:2] + '/' + input_date[2:4] + '/' + input_date[4:]

while True:
    # Coleta a entrada para a data inicial no formato "DD/MM/AAAA"
    data_inicial_str = input("Insira a data inicial (por exemplo, 01/11/2023): ")
    data_final_str = input("Insira a data final (por exemplo, 26/11/2023): ")

    # Remove as barras se o usuário as incluiu
    data_inicial_str = data_inicial_str.replace('/', '')
    data_final_str = data_final_str.replace('/', '')

    # Use a função format_date_input para formatar as datas
    data_inicial_str = format_date_input(data_inicial_str)
    data_final_str = format_date_input(data_final_str)

    start_date = dt.datetime.strptime(data_inicial_str, "%d/%m/%Y").date()
    end_date = dt.datetime.strptime(data_final_str, "%d/%m/%Y").date()

    # Resto do código como antes
    state_holidays = holidays.BR(state='SP', years=range(start_date.year, end_date.year + 1))
    national_holidays = holidays.BR(years=range(start_date.year, end_date.year + 1))

    def is_holiday(date, holidays_list):
        return date in holidays_list

    workdays_count = networkdays(start_date, end_date)

    holidays_between_dates = []

    current_date = start_date
    while current_date <= end_date:
        if is_holiday(current_date, state_holidays) or is_holiday(current_date, national_holidays):
            workdays_count -= 1
            holiday_name = state_holidays.get(current_date) or national_holidays.get(current_date)
            holidays_between_dates.append((current_date, holiday_name))
        current_date += dt.timedelta(days=1)

    print("\nNúmero de dias úteis entre {} e {} é: {}".format(start_date, end_date, workdays_count))
    print("\n")

    list_holidays = input("Deseja listar o nome dos feriados? (S/N): ").strip().lower()
    if list_holidays == "s":
        for date, holiday_name in holidays_between_dates:
            print("\n{}: {}".format(date, holiday_name))
            print("\n")

    next_workday = end_date + dt.timedelta(days=1)
    while is_holiday(next_workday, state_holidays) or is_holiday(next_workday, national_holidays):
        next_workday += dt.timedelta(days=1)

    print("5º dia útil para pagamento: {}".format(next_workday.strftime("%d/%m/%y")))

    print("\n")

    continuar = input("Deseja realizar uma nova consulta? (S/N): ").strip().lower()
    if continuar != "s":
        break
print("")    
print("++++++++++++")
print("Ok Até mais!")
print("++++++++++++")
print("")   