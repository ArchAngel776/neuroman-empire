from app.gui.graphics.variant import NetworkBuilderVariant


# Main

class NetworkBuilderNeuronVariant(NetworkBuilderVariant):
    def draw(self, painter):
        pass

    def get_height(self) -> int:
        return self.program.indent + 2 * self.program.padding

    def mark_neuron(self, point):
        pass

    def click_neuron(self, point):
        return
