from lib.hooks import pairs, entities

from app.gui.graphics.variant import NetworkBuilderVariant


# Main

class NetworkBuilderNetworkVariant(NetworkBuilderVariant):
    def draw(self, painter):
        for index, neuron in entities(self.program.network):
            self.program.draw_neuron(painter, index, self.program.neuron_color(neuron))
            self.program.draw_neuron_name(painter, index, neuron.name)
            self.program.draw_neuron_label(painter, index, neuron.title())

        for index, neurons in entities(pairs(self.program.network)):
            self.program.draw_neuron_connection(painter, index, neurons)

    def get_height(self):
        return len(self.program.network) * (self.program.indent + self.program.neuron_size) + self.program.indent + 2 \
            * self.program.padding

    def mark_neuron(self, point):
        index = self.select_neuron_index(point)
        if index == -1:
            self.program.canvas.setCursor(self.program.cursor_default)
        else:
            self.program.canvas.setCursor(self.program.cursor_active)

    def click_neuron(self, point):
        index = self.select_neuron_index(point)
        if index == -1:
            return
        return self.program.network[index]

    def select_neuron_index(self, point):
        for i in range(len(self.program.network)):
            x = self.program.offset_x
            y = self.program.offset_y(i)
            if x < point.x() < x + self.program.neuron_size and y < point.y() < y + self.program.neuron_size:
                return i
        return -1
