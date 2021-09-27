def assignment(data_list):
    """Compare the values ​​in the list with those in the dictionary to get the final score

    Args:
        data_list (str): list containing the values of the codes entered

    Returns:
        (int): return the value of the score
    """

    composition     = {'C3': 2, 'C4': 4}
    echogenicity    = {'E2': 2, 'E3': 4, 'E4': 6}
    shape           = {'F2': 6}
    margin          = {'M3': 4, 'M4': 6}
    echogenic_focus = {'EF2': 2, 'EF3': 4, 'EF4': 6}
    score = 0

    if data_list[0] == 'C3':
        score += composition['C3']
    elif data_list[0] == 'C4':
        score += composition['C4']

    if data_list[1] == 'E2':
        score += echogenicity['E2']
    elif data_list[1] == 'E3':
        score += echogenicity['E3']
    elif data_list[1] == 'E4':
        score += echogenicity['E4']

    if data_list[2] == 'F2':
        score += shape['F2']

    if data_list[3] == 'M3':
        score += margin['M3']
    elif data_list[3] == 'M4':
        score += margin['M4']

    if data_list[5] == '1':
        score += echogenic_focus['EF2']
    if data_list[6] == '1':
        score += echogenic_focus['EF3']
    if data_list[7] == '1':
        score += echogenic_focus['EF4']

    return score


def evaluation(treatment, alert):
    """Give the number of specialists the patient needs to see

    Args:
        treatment (int): number of the treatment to looking for it in the matrix
        alert (int): number of the alert to looking for it in the matrix

    Returns:
        [str]: return the amoung of specialits the patient needs to see
    """
    
    table = [['NA', 'NA', 1, 2, 3], 
            ['NA', 'NA', 2, 3, 3], 
            ['NA', 'NA', 3, 3, 4]]

    specialist = str(table[treatment][alert])
    
    return specialist


def run():
    alert_type = ['sin riesgo', 'alerta azul', 'alerta verde', 'alerta amarilla', 'alerta roja']
    treatment_type = ['no aaf', 'seguimiento','aaf']
    alert = 0
    treatment = 0
    specialist = []
    message = []

    number_patient  = int(input())

    while number_patient != 0:
        data_list = input().split()

        score = assignment(data_list)
        
        nodule_size = float(data_list[8])

        if score >= 0 and score <= 3:
            message.append(f'{alert_type[0]},{treatment_type[0]}')
        elif score >= 4 and score <= 5:
            message.append(f'{alert_type[1]},{treatment_type[0]}')
            alert = 1
        elif score >= 6 and score <= 7:
            alert = 2  
            if nodule_size < 2.5:
                message.append(f'{alert_type[2]},{treatment_type[1]}')
                treatment = 1
            else:
                message.append(f'{alert_type[2]},{treatment_type[2]}')
                treatment = 2
        elif score >= 8 and score <= 12:
            alert = 3  
            if nodule_size < 1.5:
                message.append(f'{alert_type[3]},{treatment_type[1]}')
                treatment = 1
            else:
                message.append(f'{alert_type[3]},{treatment_type[2]}')
                treatment = 2
        elif score >= 13:
            alert = 4  
            if nodule_size < 1:
                message.append(f'{alert_type[4]},{treatment_type[1]}')
                treatment = 1
            else:
                message.append(f'{alert_type[4]},{treatment_type[2]}')
                treatment = 2

        specialist.append(evaluation(treatment, alert))

        score = 0
        alert = 0
        treatment = 0
        nodule_size = 0

        number_patient -= 1
    
    for i in range(len(message)):
        print(message[i])
    specialist = " ".join(specialist)
    print(specialist)


if __name__ == '__main__':
    run()