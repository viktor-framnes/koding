from geometri import *
import pytest
import math

def test_rektangel_areal():
    assert rektangel_areal(3,5) == 15
    assert rektangel_areal(4,6) == 24

def test_sirkel_areal():
    assert sirkel_areal(3) == math.pi*3**2

def test_trekant_areal():
    assert trekant_areal(2,4) == 4

def kube_volum():
    assert kube_volum(3) == 9