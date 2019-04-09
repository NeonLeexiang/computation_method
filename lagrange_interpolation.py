import numpy as np
from matplotlib import pyplot as plt


"""
    created by neonleexiang
    date : 2019-04-09
"""


class LagrangeInterpolation:

    # --------------------- __init__ -------------------------------
    def __init__(self, n):
        self._fx = None
        self._x_diff = None
        self._wx_q = None
        self._wx_d = None
        self._wx = None
        self._n = n

    # -------------------------------------------------------------

    # no useful function cause we have the fx to input the value
    def function(self, function, x_diff):
        rst = np.zeros(self._n)

        for i in range(len(x_diff)):
            rst[i] = function(x_diff[i])
        self._fx = rst

    # --------------------- counting for wx ---------------------
    """
        :param
        x_diff : the difference of certain interval with n
        x_input : the input x to output fn(x)
    """
    def wx_d_function(self, x_diff):
        rst = np.zeros(self._n)
        x_diff = x_diff.tolist()
        x_remember = x_diff[:]
        for i in range(len(x_remember)):
            in_come = 1
            x_diff.pop(i)
            for c in x_diff:
                in_come *= x_remember[i] - c
            rst[i] = in_come
            x_diff = x_remember[:]
        self._wx_d = rst

    def wx_q_function(self, x_input, x_diff):
        rst = np.zeros(self._n)
        x_diff = x_diff.tolist()
        x_remember = x_diff[:]
        for i in range(len(x_remember)):
            in_come = 1
            x_diff.pop(i)
            for c in x_diff:
                in_come *= x_input - c
            rst[i] = in_come
            x_diff = x_remember[:]
        self._wx_q = rst

    def wx_function(self):
        rst = self._wx_q / self._wx_d
        self._wx = rst

    # ---------------------------------------------------------

    # ----------------- fit method ----------------------------
    def fit_fx(self, _input):
        self._fx = np.array(_input)

    def fit_x(self, _input_x):
        self._x_diff = np.array(_input_x)

    def function_n(self, x):
        self.wx_d_function(self._x_diff)
        self.wx_q_function(x, self._x_diff)
        # print(self._wx_q)
        # print(self._wx_d)
        self.wx_function()
        return np.sum(self._wx * self._fx)

    # ---------------------------------------------------------

    # ---------------- test method ---------------------------
    def print_all(self):
        print("the fx is \n ", self._fx)
        print("the x is \n", self._x_diff)
        print("the wx is [wx_d] [wx_q] [wx] \n", self._wx_d, self._wx_q, self._wx)

    # -----------------------------------------------------------------

    # ------------------- plot method ---------------------------------
    def fn_plot(self, x_left, x_right, partition=1000, function=None):
        # method to plot the fn(x)

        x = np.linspace(start=x_left, stop=x_right, num=partition)
        y = []

        for c in x:
            y.append(self.function_n(c))

        y_fn = np.array(y)

        plt.plot(x, y_fn, label="function of interpolation")

        if function:
            y_f = []

            for c in x:
                y_f.append(function(c))

            y_f = np.array(y_f)
            plt.plot(x, y_f, label="function of fx")

        plt.grid(True)  # display the # net
        plt.axis("equal")
        plt.xlim(x_left, x_right)
        plt.title("the interpolation of n:"+str(self._n))
        plt.legend()

        plt.show()

    # -------------------------------------------------------------------

    # ------------------- max error method ------------------------------
    def max_error(self, x_left, x_right, partition=1000, function=None):
        x = np.linspace(start=x_left, stop=x_right, num=partition)
        y = []

        for c in x:
            y.append(self.function_n(c))

        y_fn = np.array(y)

        if function:
            y = []

            for c in x:
                y.append(function(c))

            y_fx = np.array(y)

            return max(y_fn - y_fx)
        else:
            print("please enter the original function")

    # -------------------------------------------------------------------



