from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui import LS
from lib.gui.element.button import Button
from lib.gui.element.font import Font
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.component.list import List
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType
from lib.hooks import mapping, merge
from lib.gui.element.form import FormInput

from app.hooks import i18n, form_to_value, value_to_form
from app.network.neuron.unfold import Unfold
from app.network.neuron.unfold.params import UnfoldParams
from app.network.neuron.unfold.options import UnfoldOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.unfold.helpers.dimension_remover import DimensionRemover


# Decorators

class UpdateOperation(Decorator):
    def method(self, target, *args, **kwargs):
        result = super().method(target, *args, **kwargs)
        target.make(
            NeuronBuilderUnfoldStrategy.Watch.LIST_ELEMENT,
            lambda element: element.update_view()
        )
        return result


# Main

class NeuronBuilderUnfoldStrategy(NeuronStrategy):
    class Watch(str):
        LIST_ELEMENT = "list_element"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._kernel_size = mapping(self.default_params["kernel_size"], value_to_form)
        self._stride = mapping(self.default_params["stride"], value_to_form)
        self._padding = mapping(self.default_params["padding"], value_to_form)
        self._dilation = mapping(self.default_params["dilation"], value_to_form)

        self._input_height = LS.rem(1.6)
        self._title_font = Font().Size(LS.rem(.9)).Bold()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=UnfoldParams(
                kernel_size=mapping(self._kernel_size, form_to_value),
                stride=mapping(self._stride, form_to_value),
                padding=mapping(self._padding, form_to_value),
                dilation=mapping(self._dilation, form_to_value),
            ),
            options=UnfoldOptions()
        )

    @property
    def default_params(self):
        return Unfold.default_params()

    @property
    def default_options(self):
        return Unfold.default_options()

    @method(UpdateOperation)
    def load(self, params, options):
        self._kernel_size = mapping(params["kernel_size"], value_to_form)
        self._stride = mapping(params["stride"], value_to_form)
        self._padding = mapping(params["padding"], value_to_form)
        self._dilation = mapping(params["dilation"], value_to_form)

    def data(self):
        return merge(
            kernel_size=self._kernel_size,
            stride=self._stride,
            padding=self._padding,
            dilation=self._dilation
        )

    @method(UpdateOperation)
    def add_dimension(self):
        self._kernel_size.append(FormInput(0))
        self._stride.append(FormInput(0))
        self._padding.append(FormInput(0))
        self._dilation.append(FormInput(0))
        return True

    @method(UpdateOperation)
    def remove_dimension(self, index):
        self._kernel_size.pop(index)
        self._stride.pop(index)
        self._padding.pop(index)
        self._dilation.pop(index)
        return True

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    self.watch(
                        NeuronBuilderUnfoldStrategy.Watch.LIST_ELEMENT,
                        List(root, self.data, LayoutType.VERTICAL)
                        .Sizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
                        .Render(
                            lambda item, index:
                            LayoutFactory(LayoutType.VERTICAL).create()
                            .margin_vertical(LS.rem(.6))
                            .add(
                                Text(
                                    root,
                                    i18n("window.screens.network.neurons.unfold.dimension", index + 1)
                                )
                                .Font(self._title_font)
                                .Align(Qt.AlignCenter)
                                .Margin(0, LS.rem(.6))
                            )
                            .append(
                                LayoutFactory(LayoutType.HORIZONTAL).create()
                                .append(
                                    LayoutFactory(LayoutType.VERTICAL).create()
                                    .weight(1)
                                    .add(
                                        Text(root, i18n("window.screens.network.neurons.unfold.labels.kernel"))
                                    )
                                    .add(
                                        IntegerInput(root, item["kernel_size"].value)
                                        .Bind(item["kernel_size"])
                                        .Height(self._input_height)
                                    )
                                )
                                .append(
                                    LayoutFactory(LayoutType.VERTICAL).create()
                                    .weight(1)
                                    .add(
                                        Text(root, i18n("window.screens.network.neurons.unfold.labels.stride"))
                                    )
                                    .add(
                                        IntegerInput(root, item["stride"].value)
                                        .Bind(item["stride"])
                                        .Height(self._input_height)
                                    )
                                )
                            )
                            .append(
                                LayoutFactory(LayoutType.HORIZONTAL).create()
                                .append(
                                    LayoutFactory(LayoutType.VERTICAL).create()
                                    .weight(1)
                                    .add(
                                        Text(root, i18n("window.screens.network.neurons.unfold.labels.padding"))
                                    )
                                    .add(
                                        IntegerInput(root, item["padding"].value)
                                        .Bind(item["padding"])
                                        .Height(self._input_height)
                                    )
                                )
                                .append(
                                    LayoutFactory(LayoutType.VERTICAL).create()
                                    .weight(1)
                                    .add(
                                        Text(root, i18n("window.screens.network.neurons.unfold.labels.dilation"))
                                    )
                                    .add(
                                        IntegerInput(root, item["dilation"].value)
                                        .Bind(item["dilation"])
                                        .Height(self._input_height)
                                    )
                                )
                            )
                            .add(
                                Button(root, i18n("window.screens.network.neurons.unfold.buttons.remove"))
                                .Height(LS.rem(2))
                                .On(
                                    Event.Type.Click, DimensionRemover(self, index).remove,
                                    with_target=False, with_event=False
                                ),
                                index > 0
                            )
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Button(root, i18n("window.screens.network.neurons.unfold.buttons.add"))
                    .Height(LS.rem(2))
                    .On(
                        Event.Type.Click, self.add_dimension,
                        with_target=False, with_event=False
                    )
                )
            )
        )
