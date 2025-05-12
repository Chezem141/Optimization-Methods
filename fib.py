import math
import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_search(f, a0, b0, l, epsilon):
    L0 = [a0, b0]
    F = []

    N = 0
    while fibonacci(N) < abs(b0 - a0) / l:
        N += 1
    print(f"Число N: {N}")

    for i in range(N + 2):
        F.append(fibonacci(i))
    print(f"Ряд чисел Фибоначчи до F({N+1}): {F}")

    k = 0

    y0 = a0 + F[N - 2] / F[N] * (b0 - a0)
    z0 = a0 + F[N - 1] / F[N] * (b0 - a0)

    while k <= N - 3:
        f_yk = f(y0)
        f_zk = f(z0)

        if f_yk <= f_zk:
            b0 = z0
            z0 = y0
            y0 = a0 + F[N - k - 3] / F[N - k - 1] * (b0 - a0)
        else:
            a0 = y0
            y0 = z0
            z0 = a0 + F[N - k - 2] / F[N - k - 1] * (b0 - a0)

        k += 1

    y_N2 = y0
    z_N2 = z0
    print(f"y_N-2, z_N-2: {y_N2, z_N2}")

    y_N1 = z_N2
    z_N1 = y_N1 + epsilon

    f_yN1 = f(y_N1)
    f_zN1 = f(z_N1)

    if f_yN1 < f_zN1:
        a_N1 = a0
        b_N1 = z_N1
    else:
        a_N1 = y_N1
        b_N1 = b0

    x_star = (a_N1 + b_N1) / 2
    f_star = f(x_star)
    L_final = [a_N1, b_N1]
    R_N = 1 / F[N]

    print(f"Точка минимума x*: {x_star}")
    print(f"Значение функции f(x*): {f_star}")
    print(f"Конечный интервал L: {L_final}")
    print(f"k: {k}")
    print(f"R(N): {R_N}")

    x_values = [-2 + i * 10 / 100 for i in range(101)]
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values, label="f(x)")
    plt.scatter(x_star, f_star, color="red", label="Минимум")
    plt.title("Метод Фибоначчи")
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
epsilon = 0.2

fibonacci_search(f, a0, b0, l, epsilon)