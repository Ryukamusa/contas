import os
import argparse
from datetime import datetime 
parser = argparse.ArgumentParser()

parser.add_argument('--comprou', type=str,
                    choices = ['Helio', 'Natassia'],
                    help='O nome do comprador', required=True)
parser.add_argument('--data', type=str,
                    help='A data em que a compra foi efetuada')
parser.add_argument('--valor', type=float,
                    help='O valor da compra', required=True)
parser.add_argument('--nota', type=str,
                    help='Uma nota sobre a compra')
parser.add_argument('--divide', type=bool)
args = parser.parse_args()


file = '.contas'
file_bkp = f'{file}.bkp'

def check_file(file):
    file_exists = os.path.isfile(file)
    if not file_exists:
        with open(file, 'w') as f:
            f.write('Data,Nome,Valor\n')
            
def update_backup(file, file_bkp):
    with open(file, 'r') as f:
        l = f.read()

    with open(file_bkp, 'w') as f2:
        f2.write(l)

def main():
    check_file(file)
    if args.divide:
        valor = args.valor / 2
    else:
        valor = args.valor

    if args.data == 'hoje':
        data = datetime.now().strftime("%d/%m/%Y")
    else:
        data = args.data
    with open(file, 'a') as f:
        f.write('{},{},{},{}\n'.format(data, args.comprou, valor, args.nota))
    update_backup(file, file_bkp)

if __name__ == "__main__":
    main()
