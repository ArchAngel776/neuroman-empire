from typing import Literal

from app.network.neuron.replicationpad1d.boundary.options import ReplicationPad1dBoundaryOptions

# Types

ReplicationPad1dOptionsKeyof = Literal["bounded"]


# Main

class ReplicationPad1dOptions(ReplicationPad1dBoundaryOptions):
    bounded: bool
