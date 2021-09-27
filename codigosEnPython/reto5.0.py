def open_file():
    """Open the file and save values to a list

    Returns:
        [list]: returns a list with the values of the file
    """

    data = []
    
    try:
        with open('data.csv') as file:
            row = file.readline()

            while row != '':
                row = file.readline()
                aux = row.strip().split(',')
                data.append(aux)
                
            file.close()

    except FileNotFoundError as fnf_error:
        print(fnf_error)

    return data


def sort_data(city):
    """Receive the name of a city and order the values ​​of alerts and treatments from highest to lowest, finally, it prints those values

    Args:
        city (str): Name of the city to looking for it
    """

    alert = [0, 0, 0, 0, 0]
    treatment = [0, 0, 0]
    
    data = open_file()

    for row in range(len(data)-1):
        if data[row][2].lower() == city.lower():
            if data[row][13] == 'sin riesgo':
                alert[0] += 1
            elif data[row][13] == 'alerta azul':
                alert[1] += 1
            elif data[row][13] == 'alerta verde':
                alert[2] += 1
            elif data[row][13] == 'alerta amarilla':    
                alert[3] += 1
            elif data[row][13] == 'alerta roja':
                alert[4] += 1

            if data[row][14] == 'no aaf':
                treatment[0] += 1
            elif data[row][14] == 'seguimiento':
                treatment[1] += 1
            elif data[row][14] == 'aaf':
                treatment[2] += 1

    alert = sorted(alert, reverse=True)
    treatment = sorted(treatment, reverse=True)

    print('alerta roja', alert[0])
    print('alerta amarilla', alert[1])
    print('alerta verde', alert[2])
    print('alerta azul', alert[3])
    print('sin riesgo', alert[4])
    print('aaf', treatment[0])
    print('seguimiento', treatment[1])
    print('no aaf', treatment[2])


def run():

    city = input("Ingrese el nombre de la ciudad: ")

    sort_data(city)


if __name__ == '__main__':
    run()