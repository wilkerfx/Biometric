import csv
import os
path =  "/home/painkiller/PycharmProjects/Biometrico2/BioC Script/"
os.chdir(path)
ficheiro = open('output.txt', 'w')
with open('wilker.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(csv_file)
    for row in reader:
        if row[7] == 'Absence':
            row[7] = '0'
        else:
            row[7] = '1'
        ficheiro.write(str('F' + row[0] + '    ' + row[2] + 'F'+ row[7] + '301.00' + ' 10000' + '\n'))
ficheiro.close()
csv_file.close()
with open('wilker.csv', 'r') as x:
    leitura = csv.reader(x)
    next(x)
    for z in leitura:
        print('\n')
        print(f'A Processar {z[1:3]}...        .   .   .   .  . Concluído.\n')
x.close()
print('')
print ('... Os Dados Foram Processados com Sucesso.\n')
print('\n')
print('******   Copyright © 2020 Wilker Flores. ******\n')
print('\n')
print('\n')





'''import csv

BIOMETRIC_data = "wilker.csv"
OUTPUT_data = "output.txt"

with open(BIOMETRIC_data, 'r', newline='') as f, open(OUTPUT_data, 'w', newline='') as data:
    next(f)  # Skip over header in input file.
    writer = csv.writer(data, quoting=csv.QUOTE_ALL)
    writer.writerows(line.split() for line in f)'''
