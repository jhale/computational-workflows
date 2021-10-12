import pytest
import numpy as np
from triangle import compute_angles

def test_angles_add_up():
    angles = compute_angles([3, 3])
    assert(np.allclose(angles[0] + angles[1] + angles[2], 180.0))

def test_one_angle_is_90():
    angles = compute_angles([3, 3])
    assert(np.allclose(angles[0], 90.0) or np.allclose(angles[1], 90.0) or np.allclose(angles[2], 90.0))
