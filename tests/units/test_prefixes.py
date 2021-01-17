#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Tests for the hepunits.units.prefixes module.
"""

from pytest import approx

from math import log

from hepunits import mega, micro, yotta, yocto, kibi, tebi


def test_prefixes_e6():
    if 4 * mega != 1.0 / 0.25 / micro:
        raise AssertionError


def test_prefixes_e24():
    if yotta * yocto != approx(1.0):
        raise AssertionError


def test_prefixes_binary():
    if log(kibi, 2) != 10:
        raise AssertionError
    if log(tebi, 2) != 40:
        raise AssertionError
