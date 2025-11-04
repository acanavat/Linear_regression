import matplotlib.pyplot as plt
import numpy as np
from utils import load
from sys import argv


def mean(ave: list):
    return (sum(ave) / len(ave))


def variance(numbers):
    gap = [number - mean(numbers) for number in numbers]
    square = sum(x**2 for x in gap)
    return (square / (len(numbers)))


def std(numbers):
    return pow(variance(numbers), 0.5)


def linear_regression(km: list, price: list, file):
    b0 = 0
    b1 = 0
    learning_rate = 0.1
    N = len(km)
    m = 200
    km_normalized = (km - mean(km)) / std(km)
    btest = 0
    price_normalized = (price - mean(price)) / std(price)
    for iteration in range(m):
        sum_errors = 0
        sum_errors_x = 0
        for x in range(N):
            prediction = b0 + b1 * km_normalized[x]
            err_rate = prediction - price_normalized[x]
            sum_errors += err_rate
            sum_errors_x += err_rate * km_normalized[x]
        
        gradient_b0 = 1 / N * sum_errors
        gradient_b1 = 1 / N * sum_errors_x
        b0 = b0 - (gradient_b0 * learning_rate)
        b1 = b1 - (gradient_b1 * learning_rate)

    print(f'{btest} compare {b0}')
    b1_real = b1 * (std(price) / std(km))
    b0_real = b0 * std(price) + mean(price) - b1_real * mean(km)
    with open(file, 'w') as f:
        f.write(f'{b0_real}|{b1_real}')


def estimate_price(value, km: list):
    with open('brain.txt', 'r') as f:
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
        print(file)
        data = load('data.csv')
        km = data['km']
        price = data['price']
        #value = input("Entrez une valeur : ")
        #estimate_price(150000, km)
        linear_regression(km, price, file)
        plt.scatter(tuple(km), tuple(price))
        plt.xlabel('km')
        plt.ylabel('Price')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
    main()
