# Copyright 2017 Diamond Light Source
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

# Utility imports
import unittest

# Test imports
import h5py
import pandas as pd
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import mpi4py
import jax.numpy as jnp
import radia as rad

# Test import to trigger code coverage
import optidenvtest


class RadiaSmokeTest(unittest.TestCase):
    """
    Tests the Radia is available and gives sensible results.
    """

    def test_radia_version_string(self):
        
        self.assertEqual(type(rad.UtiVer()), float)

    def test_radia_simple_magnet(self):
        
        rad.UtiDelAll()
        magnet   = rad.ObjRecMag([0,0,0], [1,1,1], [0,1,0])
        observed = np.array(rad.Fld(magnet, 'b', [1,2,3]), dtype=np.float32)

        expected = np.array([0.0006504201540729257, -0.00021819974895862903, 0.0019537852236147252], dtype=np.float32)

        self.assertTrue(np.allclose(observed, expected))
