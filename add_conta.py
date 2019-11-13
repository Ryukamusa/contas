import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--nome', type=str,
                    choices = ['Helio', 'Natassia'],
                    help='O nome do comprador', required=True)
parser.add_argument('--data', type=str,
                    help='A data em que a compra foi efetuada')
parser.add_argument('--valor', type=float,
                    help='O valor da compra', required=True)

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
    with open(file, 'a') as f:
        f.write('{},{},{}\n'.format(args.data, args.nome, args.valor))
    update_backup(file, file_bkp)

if __name__ == "__main__":
    main()