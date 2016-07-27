# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
from numpy.testing import assert_allclose
from .. import SkyMask
from ...utils.testing import requires_dependency


@requires_dependency('scipy')
def test_random_creation():
    exclusion = SkyMask.empty(nxpix=300, nypix=100)
    exclusion.fill_random_circles(n=6, max_rad=10)
    assert exclusion.data.shape[0] == 100

    excluded = np.where(exclusion.data == 0)
    assert excluded[0].size != 0


@requires_dependency('scipy')
def test_distance_image():
    mask = SkyMask.empty(nxpix=3, nypix=2)
    distance = mask.distance_image.data
    assert_allclose(distance, -1e10)

    mask = SkyMask.empty(nxpix=3, nypix=2, fill=1.)
    distance = mask.distance_image.data
    assert_allclose(distance, 1e10)

    data = np.array([[0., 0., 1.], [1., 1., 1.]])
    mask = SkyMask(data=data)
    distance = mask.distance_image.data
    expected = [[-1, -1, 1], [1, 1, 1.41421356]]
    assert_allclose(distance, expected)
