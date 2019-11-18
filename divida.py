import pandas as pd
import argparse
from datetime import datetime

devedor = {'Helio':'Natassia', 'Natassia':'Helio'}

file = '.contas'

parser = argparse.ArgumentParser()
parser.add_argument('--nome', type=str,
                    choices = ['Helio', 'Natassia'],
                    help='O nome do comprador', required=True)
parser.add_argument('--fecho', type=bool,
                    help='O valor da compra')
args = parser.parse_args()

def fecha(nome):
    current_time = datetime.now().strftime("%d/%m/%Y")
    with open(file, 'a') as f:
        f.write('{},{},-1\n'.format(current_time, nome))

def get_positions(contas, nome):
    fecho = contas.query("Nome == '{}' and Valor == -1".format(nome))
    positions = fecho.index.values
    if positions.size == 0:
        return 0
    else:
        return positions[-1]

def main():
    if args.fecho:
        fecha(args.nome)
    else:
        contas = pd.read_csv(file)
        position = get_positions(contas, args.nome)
        contas_to_check = contas.iloc[position:]
        contas_devido = contas_to_check.query("Nome == '{}' and Valor != -1".format(devedor[args.nome]))
        print('Pessoa: {} | Deve: {}'.format(args.nome, contas_devido.Valor.sum().round(2)))

if __name__ == "__main__":
    main()
