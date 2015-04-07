__author__ = 'gustavo'

class Corredor:
    def __init__(self, num):
        _num = int(num)
        assert _num > 0

        self._lamp_list_ = [False for _ in range(_num)]

    @property
    def lamps(self):
        return self._lamp_list_

    def _go_jose_once(self, current):
        for i in range(current, len(self.lamps)+1, current):
            self.lamps[i-1] = not self.lamps[i-1]

    def go_jose_go(self):
        for i in range(1, len(self.lamps)+1):
            self._go_jose_once(i)
