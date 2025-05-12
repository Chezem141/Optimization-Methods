import matplotlib.pyplot as plt

def dichotoy_method(f, a0, b0, epsilon, l):
    ak, bk = a0, b0
    k = 0
    N = 0

    while abs(bk - ak) > l:
        yk = (ak + bk - epsilon) / 2
        zk = (ak + bk + epsilon) / 2

        f_yk = f(yk)
        f_zk = f(zk)

        if f_yk <= f_zk:
            ak_next, bk_next = ak, zk
        else:
            ak_next, bk_next = yk, bk

        ak, bk = ak_next, bk_next
        if abs(bk - ak) > l:
            k += 1
        N += 2

    x_star = (ak + bk) / 2
    L_final = [ak, bk]
    R_N = 1 / (2 ** (N / 2))

    print(f"Точка минимума x*: {x_star}")
    print(f"Значение функции f(x*): {f(x_star)}")
    print(f"Конечный интервал L: {L_final}")
    print(f"N: {N}")
    print(f"k: {k}")
    print(f"R(N): {R_N}")

    x_values = [a0 + i * (b0 - a0) / 100 for i in range(101)]
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values, label="f(x) = 2x^2 - 2x + 3/2")
    plt.scatter(x_star, f(x_star), color="red", label="Минимум")
    plt.title("График f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

def f(x):
    return 2 * x ** 2 - 2 * x + 3/2

print(dichotoy_method(f, -2, 8, 0.2, 0.5))