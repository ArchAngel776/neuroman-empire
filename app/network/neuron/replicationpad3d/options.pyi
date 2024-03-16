from typing import Literal

from app.network.neuron.replicationpad3d.boundary.options import ReplicationPad3dBoundaryOptions

# Types

ReplicationPad3dOptionsKeyof = Literal["bounded"]


# Main

class ReplicationPad3dOptions(ReplicationPad3dBoundaryOptions):
    bounded: bool
