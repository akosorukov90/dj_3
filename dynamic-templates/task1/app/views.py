import csv
from django.shortcuts import render
from django.conf import settings


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста

    inflation_list = []
    name_col = []
    with open(settings.INFLATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            for key, value in row.items():
                if value == '':
                    row[key] = '-'
                if key not in name_col:
                    name_col.append(key)

            inflation_list.append({'Год': row['Год'], 'Янв': row['Янв'], 'Фев': row['Фев'], 'Мар': row['Мар'],
                                   'Апр': row['Апр'], 'Май': row['Май'], 'Июн': row['Июн'], 'Июл': row['Июл'],
                                   'Авг': row['Авг'], 'Сен': row['Сен'], 'Окт': row['Окт'], 'Ноя': row['Ноя'],
                                   'Дек': row['Дек'], 'Сум': row['Суммарная']})
    context = {'inflation': inflation_list, 'name_col': name_col}
    return render(request, template_name,
                  context)