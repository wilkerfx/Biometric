import pandas as pd
import csv
data = pd.read_csv('/home/painkiller/PycharmProjects/Biometrico2/BioC Script/wilker.csv')
for index, row in data.iterrows():
    if row['Result'] == 'Absence':
        row['Result'] = '0'
    else:
        row['Result'] = '1'
    output = print ('F'+ row['Codigo'] + '    ' + str(row['Date']) + 'F' + row['Result'] + '301.00' + ' 1000')
    data['Total'] = data['First-In Time'] + data['Last-Out Time']
    data.to_csv('output_pandas.csv')


    #with open(BIOMETRIC_data, 'r', newline='') as f
    #next(f)  # Skip over header in input file.
    #writer = csv.writer(ficheiro_a_escrecer, quoting=csv.QUOTE_ALL)
    #writer.writerows(line.split() for line in f)