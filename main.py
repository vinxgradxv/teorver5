import math
import matplotlib.pyplot as plt


def print_starting_array(arr):
    print("Исходный ряд:")
    for i in arr:
        print(i, end=' ')
    print("\n")


def get_variation_series(arr):
    arr.sort()
    print("Вариационный ряд:")
    for i in arr:
        print(i, end=' ')
    print("\n")
    print("min = {:.3f}".format(arr[0]))
    print("max = {:.3f}".format(arr[19]))
    print("Размах ряда = {:.3f}".format(arr[19] - arr[0]))
    return arr

def get_mathematical_expectation(arr):
    avg = 0
    for i in arr:
        avg += i
    me = avg / len(arr)
    print("Математическое ожидание = {:.3f}".format(me))
    return me

def get_standard_deviation(arr, me):
    d = 0
    for i in arr:
        d += (i - me) ** 2
    d = d / (len(arr) - 1)
    sd = math.sqrt(d)
    print("Среднеквадратическое отклонение = {:.3f}".format(sd))
    return sd

def print_graphs(dots):
    xi = []
    pi = []
    xi.append(dots[0])
    pi.append(1 / len(dots))
    pi_index = 0
    for i in range(1, len(dots)):
        if dots[i] != dots[i-1]:
            xi.append(dots[i])
            pi_index += 1
            pi.append(1 / len(dots))
        else:
            pi[pi_index] += 1 / len(dots)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    fig.suptitle('График эмперической функции')
    h = pi[0]
    plt.plot([xi[0] - 0.5, xi[0]], [0, 0])
    for i in range(len(xi) - 1):
        plt.plot([xi[i], xi[i + 1]], [h, h])
        h += pi[i + 1]
    plt.plot([xi[len(xi) - 1], xi[len(xi) - 1] + 1], [1, 1])
    plt.grid()
    plt.show()

    h = (dots[len(dots) - 1] - dots[0]) / (1 + (math.log(len(dots)) / math.log(2)))
    m = math.ceil(1 + math.log(len(dots)) / math.log(2))
    x = dots[0] - h / 2
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('pi')
    x1 = []
    y1 = []
    fig.suptitle('Полигон частот')
    for i in range(m):
        c = 0
        for k in dots:
            if (k >= x and k < (x + h)):
                c += 1
        x1.append(x + h / 2)
        y1.append(c / len(dots))
        x += h
    plt.plot(x1, y1, '--o')
    plt.show()

    h = (dots[len(dots) - 1] - dots[0]) / (1 + (math.log(len(dots)) / math.log(2)))
    m = math.ceil(1 + math.log(len(dots)) / math.log(2))
    x = dots[0] - h / 2
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('pi')

    fig.suptitle('Гистограмма частот')
    for i in range(m):
        c = 0
        for k in dots:
            if (k >= x and k < (x + h)):
                c += 1
        plt.plot([x, x + h], [c / len(dots) / h, c / len(dots) / h])
        plt.fill_between([x, x + h], [c / len(dots) / h, c / len(dots) / h])
        x += h
    plt.show()

    return xi, pi


if __name__ == '__main__':
    arr = []
    file = open("/Users/g.d.vinogradov/PycharmProjects/teorver5/input.txt", "r")
    for line in file:
        arr.append(float(line))
    print_starting_array(arr)
    arr = get_variation_series(arr)
    me = get_mathematical_expectation(arr)
    get_standard_deviation(arr, me)
    xi, pi = print_graphs(arr)
    h = pi[0]
    print("Выборка:")

    for i in range(len(xi)):
        print("{:.2f}  ".format(xi[i]), int(pi[i]*len(arr)), " {:.2f}".format(pi[i]))
    print("Эмперическая функция:")
    print("0 если -∞ < x <= {0}".format(xi[0]))
    for i in range(len(xi) - 1):
        print("%.2f" % h + " если {0} < x <= {1}".format(xi[i], xi[i + 1]))
        h += pi[i + 1]
    print("1 если {0} < x <= ∞".format(xi[len(xi) - 1]))





