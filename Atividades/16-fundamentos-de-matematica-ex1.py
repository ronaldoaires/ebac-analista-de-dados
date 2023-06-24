# Módulo | Análise de dados: Fundamentos de Matemática

# 1. Python nativo - Quantidade de incidentes por dia

data = None

with open(file='./arquivos/16/traffic.csv', mode='r', encoding='utf8') as fp:
    fp.readline()
    data = fp.read()

day = 14
incidents = 0
incident_by_day = dict()

for timebox in data.split(sep='\n'):

    timebox_data = timebox.split(sep=';')

    for incident in timebox_data[1: len(timebox_data)-1]:
        incidents = incidents + int(incident)

    try:
        half_hour = int(timebox_data[0])

        if half_hour == 27:
            incident_by_day[day] = incidents
            day = day + 1
            incidents = 0
    except ValueError:
        continue

for day in incident_by_day:

    print(f'{day}: {incident_by_day[day]}')
