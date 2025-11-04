import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from utils import load


def estimate_price(value, file, km: list):
    with open(file, 'r') as f:
        contenu = f.read()
    form = []
    if contenu:
        form = [float(val.strip()) for val in contenu.split('|')]
    b0 = form[0] if form else 0
    b1 = form[1] if len(form) > 1 else 0

    x_plot = np.linspace(min(km), max(km), len(km))
    y_plot = b0 + b1 * x_plot
    plt.plot(x_plot, y_plot, color='red', label='Régression linéaire')
    estimate_price = b0 + b1 * value
    print(f'Estimation du prix de la voiture : {estimate_price}')


def main():
    try:
        file = argv[1]
        assert file, "Vous devez mettre le fichier en argument:"
        " python3 predict.py brain.txt"
        data = load('data.csv')
        km = data['km']
        value = input("Entrez une valeur : ").replace(" ", "")
        estimate_price(float(value), file, km)
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
    main()
