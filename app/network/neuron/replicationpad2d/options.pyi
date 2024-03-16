from typing import Literal

from app.network.neuron.replicationpad2d.boundary.options import ReplicationPad2dBoundaryOptions

# Types

ReplicationPad2dOptionsKeyof = Literal["bounded"]


# Main

class ReplicationPad2dOptions(ReplicationPad2dBoundaryOptions):
    bounded: bool
