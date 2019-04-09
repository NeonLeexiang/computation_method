import lagrange_interpolation


"""
    created by neonleexiang
    date : 2019-4-09
"""


if __name__ == '__main__':
    fx = [1.6487, 2.7183, 4.4817]
    x = [1, 2, 3]

    # definition of the function x
    import math

    def function_test(_x):
        return math.exp(_x / 2)
    # fn(x) = 4.0735 P16 Example 1.1

    # test of the lagrange interpolation
    # init number of the number of interpolation n=3, 3-times interpolation
    test_lagrange_interpolation = lagrange_interpolation.LagrangeInterpolation(3)

    # fix the fx of the module
    test_lagrange_interpolation.fit_fx(fx)

    # fix the x of the module
    test_lagrange_interpolation.fit_x(x)

    # check all the self element
    # test_lagrange_interpolation.print_all()

    # print the consequence of 3-times interpolation
    print(test_lagrange_interpolation.function_n(2.8))
    # check the self element of w
    test_lagrange_interpolation.print_all()
    # end of test of lagrange_interpolation
    test_lagrange_interpolation.fn_plot(1, 3, partition=1000, function=function_test)
