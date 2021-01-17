#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Tests for the hepunits.constants.constants module.
"""

from pytest import approx

from hepunits import eV, nanometer, s, THz
from hepunits import *


def test_constants():
    if pi_sq != two_pi * half_pi:
        raise AssertionError
    if Avogadro != 6.02214076e23:
        raise AssertionError
    if c_light / (m / s) != 299792458:
        raise AssertionError
    if hbarc_sq / c_light_sq != approx((h_Planck / two_pi) ** 2):
        raise AssertionError
    if hbar / (eV * s) != hbar / 1.0e3:
        raise AssertionError
    # wavelength of 555-ish nanometres (green light) has a frequency of 540 THz
    if c_light / (555.17121851852 * nanometer) != approx(540 * THz):
        raise AssertionError
