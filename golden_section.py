import math
import matplotlib.pyplot as plt

def golden_section_search(f, a0, b0, l):
    L0 = [a0, b0]
    k = 0
    N = 0

    phi = (3 - math.sqrt(5)) / 2
    y0 = a0 + phi * (b0 - a0)
    z0 = a0 + b0 - y0

    f_yk = f(y0)
    f_zk = f(z0)

    N += 1


    while abs(b0 - a0) > l:
        N += 1
        k += 1

        if f_yk <= f_zk:
            b0 = z0
            z0 = y0
            y0 = a0 + b0 - z0
            f_zk = f_yk
            f_yk = f(y0)
        else:
            a0 = y0
            y0 = z0
            z0 = a0 + b0 - y0
            f_yk = f_zk
            f_zk = f(z0)

    x_star = (a0 + b0) / 2
    f_star = f(x_star)
    L_final = [a0, b0]
    R_N = 0.618 ** (N - 1)

    print(f"Точка минимума x*: {x_star}")
    print(f"Значение функции f(x*): {f_star}")
    print(f"Конечный интервал L: {L_final}")
    print(f"N: {N}")
    print(f"k: {k}")
    print(f"R(N): {R_N}")

    x_values = [-2 + i * 10 / 100 for i in range(101)]
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values, label="f(x)")
    plt.scatter(x_star, f_star, color="red", label="Минимум")
    plt.title("Метод золотого сечения")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()


def f(x):
    return 2 * x ** 2 - 2 * x + 3/2

a0 = -2
b0 = 8
l = 0.5

golden_section_search(f, a0, b0, l)