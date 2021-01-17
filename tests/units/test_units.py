#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Tests for the hepunits.units.units module.
"""

from pytest import approx

from hepunits import *
from hepunits import two_pi


def test_length():
    if 3 * mm != approx(m * 0.003):
        raise AssertionError
    if 3 * mm != approx(cm * 0.3):
        raise AssertionError
    if 3 * mm != approx(km * 0.000003):
        raise AssertionError
    if 3 * mm != approx(micrometer * 3000):
        raise AssertionError
    if 3 * mm != approx(nanometer * 3000000):
        raise AssertionError
    if 3 * mm != approx(angstrom * 30000000):
        raise AssertionError
    if 3 * mm != approx(fermi * 3e12):
        raise AssertionError


def test_area():
    if (3 * mm) ** 2 != approx(9 * mm2):
        raise AssertionError
    if (3 * cm) ** 2 != approx(9 * cm2):
        raise AssertionError
    if (3 * km) ** 2 != approx(9 * km2):
        raise AssertionError
    if 2e-28 * meter2 != approx(2 * barn):
        raise AssertionError


def test_crosssection():
    if 3e-31 * barn != approx(9 * millibarn):
        raise AssertionError
    if 3e-34 * barn != approx(9 * microbarn):
        raise AssertionError
    if 3e-37 * barn != approx(9 * nanobarn):
        raise AssertionError
    if 3e-40 * barn != approx(9 * picobarn):
        raise AssertionError
    if 1 * barn != approx(100 * fm2):
        raise AssertionError


def test_luminosity():
    if invpb / invfb != approx(1.0e-3):
        raise AssertionError


def test_volume():
    if (3 * mm) ** 3 != approx(27 * mm3):
        raise AssertionError
    if (3 * cm) ** 3 != approx(27 * cm3):
        raise AssertionError
    if (3 * m) ** 3 != approx(27 * m3):
        raise AssertionError


def test_time():
    if 3 * ns != approx(3e-9 * s):
        raise AssertionError
    if 3 * ns != approx(3e-6 * ms):
        raise AssertionError
    if 3 * ns != approx(3e-3 * microsecond):
        raise AssertionError
    if 3 * ns != approx(3000 * picosecond):
        raise AssertionError
    if 3 * ns != approx(3000000 * femtosecond):
        raise AssertionError
    if day != 24 * 60 * minute:
        raise AssertionError


def test_frequency():
    if second ** -1 != approx(Hz):
        raise AssertionError
    if 1000 * hertz != approx(kHz):
        raise AssertionError
    if 1000000 * hertz != approx(MHz):
        raise AssertionError
    if 1000000000 * hertz != approx(GHz):
        raise AssertionError


def test_energy():
    if 1e3 * eV != approx(keV):
        raise AssertionError
    if 1e6 * eV != approx(MeV):
        raise AssertionError
    if 1e9 * eV != approx(GeV):
        raise AssertionError
    if 1e12 * eV != approx(TeV):
        raise AssertionError
    if 1e15 * eV != approx(PeV):
        raise AssertionError
    if 1e18 * eV != approx(EeV):
        raise AssertionError


def test_angle():
    if 360.0 * degree != two_pi * radian:
        raise AssertionError


def test_magnetic_field():
    if 10 * gauss != approx(1 * milli * tesla):
        raise AssertionError


def test_electricity():
    if 1 * mega * joule / second != approx(1 * MW):
        raise AssertionError


def test_radiation_units():
    if gray != sievert:
        raise AssertionError
    if 1 * curie != 37 * giga * becquerel:
        raise AssertionError
