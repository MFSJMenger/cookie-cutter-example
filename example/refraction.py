# example/refraction.py

from __future__ import division

import numpy as np


def snell(theta_inc, n1, n2):
    """Compute the refraction angle using Snell's Law

    Parameters
    ----------
    theta_inc : float
        Incident angle in radians.
    n1, n2 : float
        The refraction index of medium of origin and destination medium.

    Returns
    -------
    theta : float
        refraction angle

    Examples
    --------
    A ray enters an air-water boundary at pi/4 radians (45 degrees)>
    Compute exit angle.

    >>> snell(np.pi/4, 1.00, 1.33)
    0.5605584137424605
    """
    return np.arcsin(n1 / n2 * np.sin(theta_inc))
