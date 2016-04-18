
import numpy as np
import SimPEG
import scipy.sparse as sp

from .maps import SquaredSlownessMap

class HelmBaseRegularization(SimPEG.Regularization.BaseRegularization):

    mapPair = SimPEG.Maps.IdentityMap

    @property
    def W(self):
        """Full regularization weighting matrix W."""
        return sp.identity(self.mesh.nN, dtype=np.complex128)
