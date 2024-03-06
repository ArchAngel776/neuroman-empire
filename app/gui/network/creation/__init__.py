from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QSizePolicy, QLayout

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui import LS
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
from app.network.neuron.linear import Linear
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network.creation.params import NeuronCreationParams


# Decorators

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

    @property
    def neuron_index(self):
        index, neuron = self._neuron_type.value
        return index

    @property
    def neuron_type(self):
        index, neuron = self._neuron_type.value
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
            network=self.dependencies["network"]
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
                            .Bind(self._neuron_type)
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
