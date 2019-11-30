import matplotlib.pyplot as plt
import numpy as np

class AnimatedPlot():
    def __init__(self):
        self._plot_storage = dict()
        self._plot_key = ['x', 'y', 'fixed', 'c', 'marker', 'ls', 'lw', 'label', 'data_num']
        for key in self._plot_key:
            self._plot_storage[key] = list()

        self._scatter_storage = dict()
        self._scatter_key = ['x', 'y', 'fixed', 'c', 'marker', 'label', 'data_num']
        for key in self._scatter_key:
            self._scatter_storage[key] = list()

        self._min_x = np.inf
        self._max_x = -np.inf
        self._min_y = np.inf
        self._max_y = -np.inf
        self._max_data_num = 0
        self._has_label = False

    def plot(self, *xy_data, fixed=False, color=None, c=None, marker=None, linestyle=None, ls=None, linewidth=None, lw=None, label=None):
        if len(xy_data) == 2:
            x_data, y_data = xy_data
        elif len(xy_data) == 1:
            y_data = xy_data[0]
            x_data = list(range(len(y_data)))
        else:
            raise ValueError('Too many parameters given.')
        if not self._has_label:
            if isinstance(label, type(None)):
                self._has_label = True
        self._insert_plot(np.array(x_data), np.array(y_data), fixed, color, c, marker, linestyle, ls, linewidth, lw, label)

    def scatter(self, x_data, y_data, fixed=False, color=None, c=None, marker=None, label=None):
        if not self._has_label:
            if isinstance(label, type(None)):
                self._has_label = True
        self._insert_scatter(np.array(x_data), np.array(y_data), fixed, color, c, marker, label)

    def show(self, update_len=0.001, fixed_frame=True, frame_expand=0.2):
        plot_num = len(self._plot_storage['x'])
        scatter_num = len(self._scatter_storage['x'])
        for index_data in range(self._max_data_num):
            plt.clf()
            for p in range(plot_num):
                if self._plot_storage['fixed'][p]:
                    plt.plot(
                        self._plot_storage['x'][p],
                        self._plot_storage['y'][p],
                        c=self._plot_storage['c'][p],
                        marker=self._plot_storage['marker'][p],
                        ls=self._plot_storage['ls'][p],
                        lw=self._plot_storage['lw'][p],
                        label=self._plot_storage['label'][p]
                        )
                else:
                    if index_data < self._plot_storage['data_num'][p]:
                        plt.plot(
                            self._plot_storage['x'][p][:index_data+1],
                            self._plot_storage['y'][p][:index_data+1],
                            c=self._plot_storage['c'][p],
                            marker=self._plot_storage['marker'][p],
                            ls=self._plot_storage['ls'][p],
                            lw=self._plot_storage['lw'][p],
                            label=self._plot_storage['label'][p]
                            )
            for s in range(scatter_num):
                if self._scatter_storage['fixed'][s]:
                    plt.scatter(
                        self._scatter_storage['x'][s],
                        self._scatter_storage['y'][s],
                        c=self._scatter_storage['c'][s],
                        marker=self._scatter_storage['marker'][s],
                        label=self._scatter_storage['label'][s]
                        )
                else:
                    if index_data < self._scatter_storage['data_num'][s]:
                        plt.scatter(
                            self._scatter_storage['x'][s][:index_data+1],
                            self._scatter_storage['y'][s][:index_data+1],
                            c=self._scatter_storage['c'][s],
                            marker=self._scatter_storage['marker'][s],
                            label=self._scatter_storage['label'][s]
                            )
            if fixed_frame:
                min_x, max_x, min_y, max_y = self._get_frame_size(frame_expand)
                plt.xlim(min_x, max_x)
                plt.ylim(min_y, max_y)

            plt.grid()
            if self._has_label:
                plt.legend()
            plt.pause(update_len)

    def _insert_plot(self, x, y, fixed, color, c, marker, linestyle, ls, linewidth, lw, label):
        _c = c if isinstance(color, type(None)) else color
        _ls = ls if isinstance(linestyle, type(None)) else linestyle
        _lw = lw if isinstance(linewidth, type(None)) else linewidth
        insert_values = [x, y, fixed, _c, marker, _ls, _lw, label, x.shape[0]]

        self._update_min_max(x, y)

        for key, value in zip(self._plot_key, insert_values):
            self._plot_storage[key].append(value)

    def _insert_scatter(self, x, y, fixed, color, c, marker, label):
        _c = c if isinstance(color, type(None)) else color
        insert_values = [x, y, fixed, _c, marker, label, x.shape[0]]

        self._update_min_max(x, y)

        for key, value in zip(self._scatter_key, insert_values):
            self._scatter_storage[key].append(value)

    def _update_min_max(self, x, y):
        min_x, max_x = np.min(x), np.max(x)
        min_y, max_y = np.min(y), np.max(y)

        if min_x < self._min_x:
            self._min_x = min_x
        if max_x > self._max_x:
            self._max_x = max_x
        if min_y < self._min_y:
            self._min_y = min_y
        if max_y > self._max_y:
            self._max_y = max_y
        if x.shape[0] > self._max_data_num:
            self._max_data_num = x.shape[0]

    def _get_frame_size(self, frame_expand):
        min_x = (1 - frame_expand * np.sign(self._min_x)) * self._min_x
        max_x = (1 + frame_expand * np.sign(self._min_x)) * self._max_x
        min_y = (1 - frame_expand * np.sign(self._min_y)) * self._min_y
        max_y = (1 + frame_expand * np.sign(self._min_y)) * self._max_y

        return min_x, max_x, min_y, max_y
