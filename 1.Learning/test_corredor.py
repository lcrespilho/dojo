from unittest import TestCase
import corredor

__author__ = 'carlos'


class TestCorredor(TestCase):
    def test_initial_state(self):
        corridor = corredor.Corredor(3)
        lamp_list = corridor.lamps

        self.assertEqual(3, len(lamp_list))

        for lamp in lamp_list:
            self.assertFalse(lamp)

    def test_negative_size_initial(self):
        try:
            cor = corredor.Corredor(-3)
        except AssertionError:
            return

        self.fail(msg=cor.lamps)

    def test_valid_initialization_with_string(self):
        cor = corredor.Corredor('3')
        lamp_list = cor.lamps
        self.assertEqual(3, len(lamp_list))

        for lamp in lamp_list:
            self.assertFalse(lamp)

    def test_invalid_initialization_with_string(self):
        try:
            cor = corredor.Corredor('abc')
        except ValueError:
            return

        self.fail(msg=cor.lamps)

    def test_valid_go_jose_go_3(self):
        cor = corredor.Corredor(3)
        expected_list = [True, False, False]
        cor.go_jose_go()
        lamps = cor.lamps

        self.assertEqual(expected_list, lamps)

    def test_valid_go_jose_go_1(self):
        cor = corredor.Corredor(1)
        expected_list = [True]
        cor.go_jose_go()
        lamps = cor.lamps

        self.assertEqual(expected_list, lamps)


    def test_valid_go_jose_go_10(self):
        cor = corredor.Corredor(10)
        expected_list = [True, False, False, True, False, False, False, False, True, False]
        cor.go_jose_go()
        lamps = cor.lamps

        self.assertEqual(expected_list, lamps)

