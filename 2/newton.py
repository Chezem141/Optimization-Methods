import math
import numpy as np

def func(x, y):
    return x ** 2 + 7 * y ** 2 - x * y + x

def grad(x, y):
    return 2 * x - y + 1, 14 * y - x

def check_positive(M):
    return M[0][0] > 0 and (M[0][0] * M[1][1] - M[0][1] * M[1][0]) > 0

def newton_method(x, y, eps1, eps2, M):
    xk = [x, y]
    k = 0

    k_checker = 0

    H = np.array([[2, -1],
                  [-1, 14]])
    rev_H = np.linalg.inv(H)

    while k <= M:
        print('k = ', k)

        gradf = grad(xk[0], xk[1])

        print('grad = ', gradf)
        print('||grad|| = ', np.linalg.norm(gradf))
        if np.linalg.norm(gradf) < eps1:
            return xk, k + 1, 'Условие 1: ||grad(f)|| < eps1', rev_H

        if check_positive(rev_H):
            t = 1.
            d = -1 * rev_H @ gradf
        else:
            d = -1 * gradf
            t = (-5 * xk[0] ** 2 + 32 * xk[0] * xk[1] - 4 * xk[0] - 197 * xk[1] ** 2 + 2 * xk[1] - 1) / (-26 * xk[0] ** 2 + 458 * xk[0] * xk[1] - 10 * xk[0] - 2774 * xk[1] ** 2 + 32 * xk[1] - 2)
        print(f"d = {d}\nt = {t}")

        xk_next = [xk[0] + t * d[0], xk[1] + t * d[1]]
        print(f"xk+1 = {xk_next}")

        print('||xk+1 - xk|| = ', np.linalg.norm([x - y for x, y in zip(xk_next, xk)]))
        print('|f(xk+1) - f(xk)| = ', abs(func(xk_next[0], xk_next[1]) - func(xk[0], xk[1])))

        if (np.linalg.norm([x - y for x, y in zip(xk_next, xk)]) < eps2) \
                and (abs(func(xk_next[0], xk_next[1]) - func(xk[0], xk[1])) < eps2):
            if (k_checker == 1):
                return xk_next, k+1, 'Условие 3: ||xk+1 - xk|| < eps2 & |f(xk+1) - f(xk)| < eps2', rev_H
            k_checker += 1
        else:
            k_checker = 0

        xk = xk_next
        k += 1

    return xk, k + 1, 'Условие 2: достигнуто предельное число итераций', rev_H

x0, y0 = 1.1, 1.1
eps1, eps2 = 0.1, 0.15
M = 10

xk, iter_count, cond, rev_H = newton_method(x0, y0, eps1, eps2, M)

print('-------------')
print(f"x* = ({xk[0]:.2f}, {xk[1]:.2f})\nf(x*) = {func(xk[0], xk[1])}\nКоличество итераций: {iter_count}\n{cond}"
      f"\nrev_H = \n{rev_H}")