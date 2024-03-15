from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QSizePolicy, QLayout, QMessageBox

from lib.hooks import find_one
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui import LS
from lib.gui.control.alert import Alert
from lib.gui.element.button import Button
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.container import FormContainer
from lib.gui.element.form.container.element import FormElement
from lib.gui.element.form.select.v2 import Select2Box
from lib.gui.element.form.text import TextInput
from lib.gui.element.form.validator.string import StringValidator
from lib.gui.element.form.validator.string.length import Length
from lib.gui.element.form.validator.string.length.data import LengthValidationData
from lib.gui.element.form.validator.string.regex import Regex
from lib.gui.element.form.validator.string.regex.data import RegexValidationData
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.type import NeuronType
from app.network.neuron.conv1d import Convolution1d
from app.network.neuron.conv2d import Convolution2d
from app.network.neuron.conv3d import Convolution3d
from app.network.neuron.convtranspose1d import TransposedConvolution1d
from app.network.neuron.convtranspose2d import TransposedConvolution2d
from app.network.neuron.convtranspose3d import TransposedConvolution3d
from app.network.neuron.unfold import Unfold
from app.network.neuron.fold import Fold
from app.network.neuron.maxpool1d import MaxPooling1d
from app.network.neuron.maxpool2d import MaxPooling2d
from app.network.neuron.maxpool3d import MaxPooling3d
from app.network.neuron.maxunpool1d import MaxUnpooling1d
from app.network.neuron.maxunpool2d import MaxUnpooling2d
from app.network.neuron.maxunpool3d import MaxUnpooling3d
from app.network.neuron.avgpool1d import AveragePooling1d
from app.network.neuron.avgpool2d import AveragePooling2d
from app.network.neuron.avgpool3d import AveragePooling3d
from app.network.neuron.fractionalmaxpool2d import FractionalMaxPooling2d
from app.network.neuron.fractionalmaxpool3d import FractionalMaxPooling3d
from app.network.neuron.lppool1d import LocalPooling1d
from app.network.neuron.lppool2d import LocalPooling2d
from app.network.neuron.adaptivemaxpool1d import AdaptiveMaxPooling1d
from app.network.neuron.adaptivemaxpool2d import AdaptiveMaxPooling2d
from app.network.neuron.adaptivemaxpool3d import AdaptiveMaxPooling3d
from app.network.neuron.adaptiveavgpool1d import AdaptiveAveragePooling1d
from app.network.neuron.adaptiveavgpool2d import AdaptiveAveragePooling2d
from app.network.neuron.adaptiveavgpool3d import AdaptiveAveragePooling3d
from app.network.neuron.linear import Linear
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network.creation.params import NeuronCreationParams


# Decorators

class PreventNeuron(Decorator):
    def method(self, target, event):
        if super().method(target, event):
            return True

        target.neuron_item.sync()
        return False


class CloseForm(Decorator):
    def method(self, target):
        target.form_container.close()
        return super().method(target)


# Main

class NeuronOperationCreationStrategy(SwitcherStrategy):
    class Watch(str):
        NEURON_SWITCHER_ELEMENT = "neuron_switcher_element"

    class NeuronGroup(str):
        CONV = "conv"
        POOL = "pool"
        LIN = "lin"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._neuron_name = FormInput("")
        self._neuron_type = FormInput((0, Convolution1d))

        self._form_container = FormContainer()

        self._form_title_font = Font().Size(LS.rem(1.2)).Bold().Underline()
        self._form_label_font = Font().Size(LS.rem(.8))

        self._button_cursor = QCursor(Qt.PointingHandCursor)

    @property
    def params(self):
        return NeuronCreationParams(
            name=self._neuron_name.value,
            params=self.switcher_program.params.params,
            options=self.switcher_program.params.options
        )

    def select_neuron(self, event):
        self.make(
            NeuronOperationCreationStrategy.Watch.NEURON_SWITCHER_ELEMENT,
            lambda switcher: switcher.change_strategy(event.data.type())
        )
        return True

    @method(PreventNeuron)
    def secure_unpooling_layers(self, event):
        match event.data.type():
            case NeuronType.MAXUNPOOL1D:
                if find_one(
                    self.network,
                    lambda neuron:
                    isinstance(neuron, (MaxPooling1d, AdaptiveMaxPooling1d)) and
                    neuron.params["return_indices"]
                ):
                    return True

                (
                    Alert(i18n("window.screens.network.creation.secure_pooling.message.maxunpool1d"))
                    .title(i18n("window.screens.network.creation.secure_pooling.title"))
                    .type(QMessageBox.Icon.Warning)
                    .show()
                )

                return False
            case NeuronType.MAXUNPOOL2D:
                if find_one(
                    self.network,
                    lambda neuron:
                    isinstance(neuron, (MaxPooling2d, FractionalMaxPooling2d, AdaptiveMaxPooling2d)) and
                    neuron.params["return_indices"]
                ):
                    return True

                (
                    Alert(i18n("window.screens.network.creation.secure_pooling.message.maxunpool2d"))
                    .title(i18n("window.screens.network.creation.secure_pooling.title"))
                    .type(QMessageBox.Icon.Warning)
                    .show()
                )

                return False
            case NeuronType.MAXUNPOOL3D:
                if find_one(
                    self.network,
                    lambda neuron:
                    isinstance(neuron, (MaxPooling3d, FractionalMaxPooling3d, AdaptiveMaxPooling3d)) and
                    neuron.params["return_indices"]
                ):
                    return True

                (
                    Alert(i18n("window.screens.network.creation.secure_pooling.message.maxunpool3d"))
                    .title(i18n("window.screens.network.creation.secure_pooling.title"))
                    .type(QMessageBox.Icon.Warning)
                    .show()
                )

                return False
            case _:
                return True

    @property
    def network(self):
        return self.dependencies["network"]

    @property
    def neuron_item(self):
        return self._neuron_type

    @property
    def neuron_index(self):
        index, neuron = self.neuron_item.value
        return index

    @property
    def neuron_type(self):
        index, neuron = self.neuron_item.value
        return neuron

    @property
    def create(self):
        return self.dependencies["create"]

    @property
    def action_entry(self):
        return self.dependencies["action_entry"]

    def validate_form(self):
        self.form_container.validate()
        return self.form_container.is_valid

    def create_neuron(self):
        self.create(self.neuron_type)
        return True

    @method(CloseForm)
    def cancel(self):
        self.action_entry()
        return True

    @property
    def switcher_program(self):
        return self.get(NeuronOperationCreationStrategy.Watch.NEURON_SWITCHER_ELEMENT).program

    @property
    def neuron_dependencies(self):
        return NeuronBuilderDependencies(
            network=self.network
        )

    @property
    def form_container(self):
        return self._form_container

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .weight(1)
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.creation.title"))
                    .Font(self._form_title_font)
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .constraint(QLayout.SizeConstraint.SetMinimumSize)
                    .margin_vertical(LS.rem(.2))
                    .add(
                        Text(root, i18n("window.screens.network.creation.labels.name"))
                        .Font(self._form_label_font)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .margin_vertical(LS.rem(.5))
                        .add(
                            FormElement(self._form_container)
                            .Control(
                                TextInput(root, self._neuron_name.value)
                                .Bind(self._neuron_name)
                            )
                            .Validator(
                                StringValidator(
                                    Length(
                                        LengthValidationData(
                                            min=4,
                                            message=i18n("window.screens.network.creation.form.name.message.min", 4)
                                        )
                                    ),
                                    Length(
                                        LengthValidationData(
                                            max=255,
                                            message=i18n("window.screens.network.creation.form.name.message.max", 255)
                                        )
                                    ),
                                    Regex(
                                        RegexValidationData(
                                            pattern="^([A-Za-z0-9_\\-\\s]+)$",
                                            message=i18n("window.screens.network.creation.form.name.message.signs")
                                        )
                                    ),
                                    Regex(
                                        RegexValidationData(
                                            pattern="^([A-Za-z0-9][A-Za-z0-9_\\-\\s]+[A-Za-z0-9])$",
                                            message=i18n("window.screens.network.creation.form.name.message.spaces")
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .margin_vertical(LS.rem(.2))
                    .add(
                        Text(root, i18n("window.screens.network.creation.labels.type"))
                        .Font(self._form_label_font)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Select2Box(root)
                            .Bind(self.neuron_item)
                            .On(
                                Event.Type.Select, self.secure_unpooling_layers,
                                with_target=False,
                                with_event=True
                            )
                            .On(
                                Event.Type.Select, self.select_neuron,
                                with_target=False,
                                with_event=True
                            )
                            .Group(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                "Convolution"
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                Convolution1d.title(),
                                Convolution1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                Convolution2d.title(),
                                Convolution2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                Convolution3d.title(),
                                Convolution3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                TransposedConvolution1d.title(),
                                TransposedConvolution1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                TransposedConvolution2d.title(),
                                TransposedConvolution2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                TransposedConvolution3d.title(),
                                TransposedConvolution3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                Unfold.title(),
                                Unfold
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.CONV,
                                Fold.title(),
                                Fold
                            )
                            .Group(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                "Pooling"
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                MaxPooling1d.title(),
                                MaxPooling1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                MaxPooling2d.title(),
                                MaxPooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                MaxPooling3d.title(),
                                MaxPooling3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                MaxUnpooling1d.title(),
                                MaxUnpooling1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                MaxUnpooling2d.title(),
                                MaxUnpooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                MaxUnpooling3d.title(),
                                MaxUnpooling3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AveragePooling1d.title(),
                                AveragePooling1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AveragePooling2d.title(),
                                AveragePooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AveragePooling3d.title(),
                                AveragePooling3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                FractionalMaxPooling2d.title(),
                                FractionalMaxPooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                FractionalMaxPooling3d.title(),
                                FractionalMaxPooling3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                LocalPooling1d.title(),
                                LocalPooling1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                LocalPooling2d.title(),
                                LocalPooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AdaptiveMaxPooling1d.title(),
                                AdaptiveMaxPooling1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AdaptiveMaxPooling2d.title(),
                                AdaptiveMaxPooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AdaptiveMaxPooling3d.title(),
                                AdaptiveMaxPooling3d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AdaptiveAveragePooling1d.title(),
                                AdaptiveAveragePooling1d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AdaptiveAveragePooling2d.title(),
                                AdaptiveAveragePooling2d
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.POOL,
                                AdaptiveAveragePooling3d.title(),
                                AdaptiveAveragePooling3d
                            )
                            .Group(
                                NeuronOperationCreationStrategy.NeuronGroup.LIN,
                                "Linear"
                            )
                            .Option(
                                NeuronOperationCreationStrategy.NeuronGroup.LIN,
                                Linear.title(),
                                Linear
                            )
                            .Active(self.neuron_index)
                        )
                    )
                )
                .add(
                    Scrollable(root)
                    .ScrollY(True, size=SCROLLBAR_SIZE)
                    .Content(
                        self.watch(
                            NeuronOperationCreationStrategy.Watch.NEURON_SWITCHER_ELEMENT,
                            Switcher(
                                root,
                                NeuronBuilderSwitcher(NeuronType.CONV1D, self.neuron_dependencies),
                                LayoutType.VERTICAL
                            )
                            .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Button(root, i18n("window.screens.network.creation.buttons.add"))
                        .Height(LS.rem(2))
                        .Cursor(self._button_cursor)
                        .On(
                            Event.Type.Click, self.validate_form,
                            with_target=False,
                            with_event=False
                        )
                        .On(
                            Event.Type.Click, self.create_neuron,
                            with_target=False,
                            with_event=False
                        )
                    )
                    .add(
                        Button(root, i18n("window.screens.network.creation.buttons.cancel"))
                        .Height(LS.rem(2))
                        .Cursor(self._button_cursor)
                        .On(
                            Event.Type.Click, self.cancel,
                            with_target=False,
                            with_event=False
                        )
                    )
                )
            )
        )
