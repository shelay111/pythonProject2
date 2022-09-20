import pytest


def inc(x):
    return x + 1


class TestInc:

    @pytest.mark.smoke
    @pytest.mark.unit
    @pytest.mark.function
    def test_zero(self):
        assert inc(0) == 1

    @pytest.mark.unit
    @pytest.mark.function
    def test_negative(self):
        assert inc(-1) == 0

    @pytest.mark.unit
    @pytest.mark.function
    def test_positive(self):
        assert inc(1) == 2

    @pytest.mark.unit
    @pytest.mark.illegalinput
    @pytest.mark.xfail(raises=TypeError, reason="illegal input")
    def test_character(self):
        assert inc('aaa') == "aaa1"

    @pytest.mark.unit
    @pytest.mark.function
    def test_max_positive(self):
        assert inc(9999999999999999999) == 10000000000000000000
