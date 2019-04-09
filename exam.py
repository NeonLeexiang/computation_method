import lagrange_interpolation
# import numpy as np

"""
    created by neonleexiang
    date : 2019-04-09
"""


def function_fx(_x):
    return 1/(1+(5*_x)**2)


def x_diff(x_left, x_right=0, partition=100):
    x_list = []
    if x_right != 0:
        for _i in range(x_left, x_right, partition):
            x_list.append(_i)
        return x_list

    for _i in range(0, partition+1):
        x_list.append(x_left + _i * (2/partition))
    return x_list


def function_fx_value(_x):
    rst = []
    for _c in _x:
        rst.append(function_fx(_c))
    return rst


def plot_interpolation(_n_list):
    for _num in _n_list:
        _x = x_diff(-1, partition=_num)
        _y = []
        for _c in _x:
            _y.append(function_fx(_c))

        # test the output
        print("the %dth interpolation,x is :" % _num, _x)
        print("the %dth interpolation,y is :" % _num, _y)

        rst_lagrange = lagrange_interpolation.LagrangeInterpolation(_num+1)

        # fit the x and fx
        rst_lagrange.fit_x(_x)
        rst_lagrange.fit_fx(_y)

        # plot
        rst_lagrange.fn_plot(-1, 1, function=function_fx)
        max_error = rst_lagrange.max_error(-1, 1, function=function_fx)
        print("the %dth interpolation max error is: %f" % (_num, max_error))


if __name__ == '__main__':
    """
    # ------------------- test ----------------------------
    x = x_diff(-1, partition=8)
    y = []
    for c in x:
        y.append(function_fx(c))

    # test the output
    print("the x is :", x)
    print("the y is :", y)

    test_lagrange = lagrange_interpolation.LagrangeInterpolation(9)

    # fit the x and fx
    test_lagrange.fit_x(x)
    test_lagrange.fit_fx(y)

    # plot
    test_lagrange.fn_plot(-1, 1, function=function_fx)
    # ---------------------- end of test ---------------------

    """

    n_list = [2, 4, 6, 8, 10]
    plot_interpolation(n_list)

