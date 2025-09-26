# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FLIR.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QFont,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QGraphicsView,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class MainUI(object):
    def __init__(self, main_window):
        self.setupUi(main_window)

    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.setWindowModality(Qt.WindowModality.WindowModal)
        main_window.resize(1060, 736)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(720, 550))
        main_window.setStyleSheet('font: 12pt "Arial";')
        main_window.setDocumentMode(False)
        main_window.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionExit = QAction(main_window)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setEnabled(False)
        self.actionSave_As = QAction(main_window)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.setEnabled(False)
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName("actionAbout")
        self.main_container = QWidget(main_window)
        self.main_container.setObjectName("main_container")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.main_container.sizePolicy().hasHeightForWidth()
        )
        self.main_container.setSizePolicy(sizePolicy1)
        self.main_layout = QGridLayout(self.main_container)
        self.main_layout.setObjectName("main_layout")
        self.main_layout.setHorizontalSpacing(4)
        self.main_layout.setVerticalSpacing(0)
        self.main_layout.setContentsMargins(4, 4, 4, 0)
        self.viewport = QGraphicsView(self.main_container)
        self.viewport.setObjectName("viewport")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.viewport.sizePolicy().hasHeightForWidth())
        self.viewport.setSizePolicy(sizePolicy2)

        self.main_layout.addWidget(self.viewport, 0, 1, 1, 1)

        self.left_pane = QFrame(self.main_container)
        self.left_pane.setObjectName("left_pane")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_pane.sizePolicy().hasHeightForWidth())
        self.left_pane.setSizePolicy(sizePolicy3)
        self.left_pane.setFrameShape(QFrame.Shape.Box)
        self.left_pane.setFrameShadow(QFrame.Shadow.Raised)
        self.left_pane.setLineWidth(1)
        self.left_pane_layout = QVBoxLayout(self.left_pane)
        self.left_pane_layout.setSpacing(2)
        self.left_pane_layout.setObjectName("left_pane_layout")
        self.left_pane_layout.setContentsMargins(0, 0, 0, 0)
        self.param_header = QLabel(self.left_pane)
        self.param_header.setObjectName("param_header")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.param_header.sizePolicy().hasHeightForWidth()
        )
        self.param_header.setSizePolicy(sizePolicy4)
        self.param_header.setStyleSheet(
            "border-bottom-width: 2px;\n"
            "border-bottom-style: solid;\n"
            "border-radius: 0px;\n"
            "border-color: grey;\n"
            'font: 700 16pt "Arial";'
        )
        self.param_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.left_pane_layout.addWidget(self.param_header)

        self.param_disp = QWidget(self.left_pane)
        self.param_disp.setObjectName("param_disp")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.param_disp.sizePolicy().hasHeightForWidth())
        self.param_disp.setSizePolicy(sizePolicy5)
        self.param_disp.setMinimumSize(QSize(200, 120))
        self.param_disp.setMaximumSize(QSize(99999, 99999))
        self.param_disp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.param_disp_layout = QVBoxLayout(self.param_disp)
        self.param_disp_layout.setObjectName("param_disp_layout")
        self.param_disp_layout.setContentsMargins(2, 2, 10, 2)
        self.current_exposure_widget = QWidget(self.param_disp)
        self.current_exposure_widget.setObjectName("current_exposure_widget")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.current_exposure_widget.sizePolicy().hasHeightForWidth()
        )
        self.current_exposure_widget.setSizePolicy(sizePolicy6)
        self.current_exposure_disp_layout = QHBoxLayout(self.current_exposure_widget)
        self.current_exposure_disp_layout.setSpacing(6)
        self.current_exposure_disp_layout.setObjectName("current_exposure_disp_layout")
        self.current_exposure_disp_layout.setContentsMargins(-1, 0, 9, 0)
        self.current_exposure_label = QLabel(self.current_exposure_widget)
        self.current_exposure_label.setObjectName("current_exposure_label")
        sizePolicy7 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.current_exposure_label.sizePolicy().hasHeightForWidth()
        )
        self.current_exposure_label.setSizePolicy(sizePolicy7)

        self.current_exposure_disp_layout.addWidget(self.current_exposure_label)

        self.current_exposure_data = QLabel(self.current_exposure_widget)
        self.current_exposure_data.setObjectName("current_exposure_data")
        sizePolicy8 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(
            self.current_exposure_data.sizePolicy().hasHeightForWidth()
        )
        self.current_exposure_data.setSizePolicy(sizePolicy8)
        self.current_exposure_data.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.current_exposure_data.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.current_exposure_disp_layout.addWidget(self.current_exposure_data)

        self.param_disp_layout.addWidget(self.current_exposure_widget)

        self.current_framerate_widget = QWidget(self.param_disp)
        self.current_framerate_widget.setObjectName("current_framerate_widget")
        sizePolicy4.setHeightForWidth(
            self.current_framerate_widget.sizePolicy().hasHeightForWidth()
        )
        self.current_framerate_widget.setSizePolicy(sizePolicy4)
        self.current_FPS_disp_layout = QHBoxLayout(self.current_framerate_widget)
        self.current_FPS_disp_layout.setObjectName("current_FPS_disp_layout")
        self.current_FPS_disp_layout.setContentsMargins(-1, 0, -1, 0)
        self.current_fps_label = QLabel(self.current_framerate_widget)
        self.current_fps_label.setObjectName("current_fps_label")
        sizePolicy7.setHeightForWidth(
            self.current_fps_label.sizePolicy().hasHeightForWidth()
        )
        self.current_fps_label.setSizePolicy(sizePolicy7)

        self.current_FPS_disp_layout.addWidget(self.current_fps_label)

        self.current_fps_data = QLabel(self.current_framerate_widget)
        self.current_fps_data.setObjectName("current_fps_data")
        sizePolicy8.setHeightForWidth(
            self.current_fps_data.sizePolicy().hasHeightForWidth()
        )
        self.current_fps_data.setSizePolicy(sizePolicy8)
        self.current_fps_data.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.current_fps_data.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.current_FPS_disp_layout.addWidget(self.current_fps_data)

        self.param_disp_layout.addWidget(self.current_framerate_widget)

        self.max_framerate_widget = QWidget(self.param_disp)
        self.max_framerate_widget.setObjectName("max_framerate_widget")
        sizePolicy4.setHeightForWidth(
            self.max_framerate_widget.sizePolicy().hasHeightForWidth()
        )
        self.max_framerate_widget.setSizePolicy(sizePolicy4)
        self.max_framerate_disp_layout = QHBoxLayout(self.max_framerate_widget)
        self.max_framerate_disp_layout.setObjectName("max_framerate_disp_layout")
        self.max_framerate_disp_layout.setContentsMargins(9, 0, -1, 0)
        self.max_fps_label = QLabel(self.max_framerate_widget)
        self.max_fps_label.setObjectName("max_fps_label")
        sizePolicy7.setHeightForWidth(
            self.max_fps_label.sizePolicy().hasHeightForWidth()
        )
        self.max_fps_label.setSizePolicy(sizePolicy7)

        self.max_framerate_disp_layout.addWidget(self.max_fps_label)

        self.max_fps_data = QLabel(self.max_framerate_widget)
        self.max_fps_data.setObjectName("max_fps_data")
        sizePolicy8.setHeightForWidth(
            self.max_fps_data.sizePolicy().hasHeightForWidth()
        )
        self.max_fps_data.setSizePolicy(sizePolicy8)
        self.max_fps_data.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.max_framerate_disp_layout.addWidget(self.max_fps_data)

        self.param_disp_layout.addWidget(self.max_framerate_widget)

        self.s_per_trial_widget = QWidget(self.param_disp)
        self.s_per_trial_widget.setObjectName("s_per_trial_widget")
        sizePolicy4.setHeightForWidth(
            self.s_per_trial_widget.sizePolicy().hasHeightForWidth()
        )
        self.s_per_trial_widget.setSizePolicy(sizePolicy4)
        self.s_per_trial_disp_layout = QHBoxLayout(self.s_per_trial_widget)
        self.s_per_trial_disp_layout.setObjectName("s_per_trial_disp_layout")
        self.s_per_trial_disp_layout.setContentsMargins(9, 0, -1, 0)
        self.s_per_trial_label = QLabel(self.s_per_trial_widget)
        self.s_per_trial_label.setObjectName("s_per_trial_label")
        sizePolicy7.setHeightForWidth(
            self.s_per_trial_label.sizePolicy().hasHeightForWidth()
        )
        self.s_per_trial_label.setSizePolicy(sizePolicy7)

        self.s_per_trial_disp_layout.addWidget(self.s_per_trial_label)

        self.s_per_trial_data = QLabel(self.s_per_trial_widget)
        self.s_per_trial_data.setObjectName("s_per_trial_data")
        sizePolicy8.setHeightForWidth(
            self.s_per_trial_data.sizePolicy().hasHeightForWidth()
        )
        self.s_per_trial_data.setSizePolicy(sizePolicy8)
        self.s_per_trial_data.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.s_per_trial_disp_layout.addWidget(self.s_per_trial_data)

        self.param_disp_layout.addWidget(self.s_per_trial_widget)

        self.num_frames_widget = QWidget(self.param_disp)
        self.num_frames_widget.setObjectName("num_frames_widget")
        sizePolicy4.setHeightForWidth(
            self.num_frames_widget.sizePolicy().hasHeightForWidth()
        )
        self.num_frames_widget.setSizePolicy(sizePolicy4)
        self.num_frames_layout = QHBoxLayout(self.num_frames_widget)
        self.num_frames_layout.setObjectName("num_frames_layout")
        self.num_frames_layout.setContentsMargins(9, 0, -1, 0)
        self.num_frames_label = QLabel(self.num_frames_widget)
        self.num_frames_label.setObjectName("num_frames_label")
        sizePolicy7.setHeightForWidth(
            self.num_frames_label.sizePolicy().hasHeightForWidth()
        )
        self.num_frames_label.setSizePolicy(sizePolicy7)

        self.num_frames_layout.addWidget(self.num_frames_label)

        self.num_frames_data = QLabel(self.num_frames_widget)
        self.num_frames_data.setObjectName("num_frames_data")
        sizePolicy8.setHeightForWidth(
            self.num_frames_data.sizePolicy().hasHeightForWidth()
        )
        self.num_frames_data.setSizePolicy(sizePolicy8)
        self.num_frames_data.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.num_frames_layout.addWidget(self.num_frames_data)

        self.param_disp_layout.addWidget(self.num_frames_widget)

        self.left_pane_layout.addWidget(self.param_disp)

        self.controls = QWidget(self.left_pane)
        self.controls.setObjectName("controls")
        sizePolicy2.setHeightForWidth(self.controls.sizePolicy().hasHeightForWidth())
        self.controls.setSizePolicy(sizePolicy2)
        self.controls_layout = QVBoxLayout(self.controls)
        self.controls_layout.setObjectName("controls_layout")
        self.controls_layout.setContentsMargins(2, 2, 2, 2)
        self.controls_header = QLabel(self.controls)
        self.controls_header.setObjectName("controls_header")
        sizePolicy4.setHeightForWidth(
            self.controls_header.sizePolicy().hasHeightForWidth()
        )
        self.controls_header.setSizePolicy(sizePolicy4)
        self.controls_header.setStyleSheet(
            "border-top-width: 2px;\n"
            "border-top-style: solid;\n"
            "border-bottom-width: 2px;\n"
            "border-bottom-style: solid;\n"
            "border-radius: 0px;\n"
            "border-color: grey;\n"
            "\n"
            'font: 700 16pt "Arial";'
        )
        self.controls_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.controls_layout.addWidget(self.controls_header)

        self.acquisition_mode = QGroupBox(self.controls)
        self.acquisition_mode.setObjectName("acquisition_mode")
        sizePolicy6.setHeightForWidth(
            self.acquisition_mode.sizePolicy().hasHeightForWidth()
        )
        self.acquisition_mode.setSizePolicy(sizePolicy6)
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.acquisition_mode.setFont(font)
        self.acquisition_mode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.acquisition_mode_layout = QVBoxLayout(self.acquisition_mode)
        self.acquisition_mode_layout.setSpacing(0)
        self.acquisition_mode_layout.setObjectName("acquisition_mode_layout")
        self.acquisition_mode_layout.setContentsMargins(4, 2, 4, 4)
        self.acquisition_mode_data = QComboBox(self.acquisition_mode)
        self.acquisition_mode_data.addItem("")
        self.acquisition_mode_data.addItem("")
        self.acquisition_mode_data.addItem("")
        self.acquisition_mode_data.setObjectName("acquisition_mode_data")

        self.acquisition_mode_layout.addWidget(self.acquisition_mode_data)

        self.controls_layout.addWidget(self.acquisition_mode)

        self.exposure_control = QGroupBox(self.controls)
        self.exposure_control.setObjectName("exposure_control")
        sizePolicy6.setHeightForWidth(
            self.exposure_control.sizePolicy().hasHeightForWidth()
        )
        self.exposure_control.setSizePolicy(sizePolicy6)
        self.exposure_control.setFont(font)
        self.exposure_control.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exposure_layout = QVBoxLayout(self.exposure_control)
        self.exposure_layout.setSpacing(6)
        self.exposure_layout.setObjectName("exposure_layout")
        self.exposure_layout.setContentsMargins(4, 2, 4, 4)
        self.exposure_mode = QComboBox(self.exposure_control)
        self.exposure_mode.addItem("")
        self.exposure_mode.addItem("")
        self.exposure_mode.addItem("")
        self.exposure_mode.setObjectName("exposure_mode")
        self.exposure_mode.setEditable(False)

        self.exposure_layout.addWidget(self.exposure_mode)

        self.exposure_value = QSpinBox(self.exposure_control)
        self.exposure_value.setObjectName("exposure_value")
        self.exposure_value.setFont(font)
        self.exposure_value.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.exposure_value.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.exposure_value.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.exposure_value.setAccelerated(True)
        self.exposure_value.setProperty("showGroupSeparator", False)
        self.exposure_value.setMinimum(1)
        self.exposure_value.setMaximum(99999999)
        self.exposure_value.setStepType(
            QAbstractSpinBox.StepType.AdaptiveDecimalStepType
        )
        self.exposure_value.setDisplayIntegerBase(10)

        self.exposure_layout.addWidget(self.exposure_value)

        self.center_apply_button = QWidget(self.exposure_control)
        self.center_apply_button.setObjectName("center_apply_button")
        sizePolicy9 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(
            self.center_apply_button.sizePolicy().hasHeightForWidth()
        )
        self.center_apply_button.setSizePolicy(sizePolicy9)
        self.center_apply_button_layout = QHBoxLayout(self.center_apply_button)
        self.center_apply_button_layout.setSpacing(0)
        self.center_apply_button_layout.setObjectName("center_apply_button_layout")
        self.center_apply_button_layout.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.center_apply_button_layout.setContentsMargins(2, 2, 2, 0)
        self.exposure_apply = QPushButton(self.center_apply_button)
        self.exposure_apply.setObjectName("exposure_apply")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(
            self.exposure_apply.sizePolicy().hasHeightForWidth()
        )
        self.exposure_apply.setSizePolicy(sizePolicy10)

        self.center_apply_button_layout.addWidget(self.exposure_apply)

        self.exposure_layout.addWidget(self.center_apply_button)

        self.controls_layout.addWidget(self.exposure_control)

        self.s_per_trial = QGroupBox(self.controls)
        self.s_per_trial.setObjectName("s_per_trial")
        sizePolicy6.setHeightForWidth(self.s_per_trial.sizePolicy().hasHeightForWidth())
        self.s_per_trial.setSizePolicy(sizePolicy6)
        self.s_per_trial.setFont(font)
        self.s_per_trial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.secondsper_trial_layout = QHBoxLayout(self.s_per_trial)
        self.secondsper_trial_layout.setSpacing(6)
        self.secondsper_trial_layout.setObjectName("secondsper_trial_layout")
        self.secondsper_trial_layout.setContentsMargins(4, 2, 4, 4)
        self.s_per_trial_val = QDoubleSpinBox(self.s_per_trial)
        self.s_per_trial_val.setObjectName("s_per_trial_val")
        self.s_per_trial_val.setFont(font)
        self.s_per_trial_val.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.s_per_trial_val.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.s_per_trial_val.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.s_per_trial_val.setAccelerated(True)
        self.s_per_trial_val.setProperty("showGroupSeparator", False)
        self.s_per_trial_val.setSuffix("(s)")
        self.s_per_trial_val.setDecimals(2)
        self.s_per_trial_val.setMinimum(1.000000000000000)
        self.s_per_trial_val.setMaximum(999999.000000000000000)
        self.s_per_trial_val.setStepType(
            QAbstractSpinBox.StepType.AdaptiveDecimalStepType
        )
        self.s_per_trial_val.setValue(2.000000000000000)

        self.secondsper_trial_layout.addWidget(self.s_per_trial_val)

        self.controls_layout.addWidget(self.s_per_trial)

        self.trigger_control = QGroupBox(self.controls)
        self.trigger_control.setObjectName("trigger_control")
        sizePolicy4.setHeightForWidth(
            self.trigger_control.sizePolicy().hasHeightForWidth()
        )
        self.trigger_control.setSizePolicy(sizePolicy4)
        self.trigger_control.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.trigger_control)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("trigger_control_layout")
        self.verticalLayout.setContentsMargins(4, 2, 4, 4)
        self.trigger_source_selection = QComboBox(self.trigger_control)
        self.trigger_source_selection.addItem("")
        self.trigger_source_selection.addItem("")
        self.trigger_source_selection.addItem("")
        self.trigger_source_selection.addItem("")
        self.trigger_source_selection.setObjectName("trigger_source_selection")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(
            self.trigger_source_selection.sizePolicy().hasHeightForWidth()
        )
        self.trigger_source_selection.setSizePolicy(sizePolicy11)
        self.trigger_source_selection.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.trigger_source_selection)

        self.controls_layout.addWidget(self.trigger_control)

        self.buttons = QFrame(self.controls)
        self.buttons.setObjectName("buttons")
        sizePolicy12 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy12)
        self.buttons.setMinimumSize(QSize(0, 50))
        self.buttons.setMaximumSize(QSize(16777215, 150))
        self.buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.buttons_layout = QGridLayout(self.buttons)
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setObjectName("buttons_layout")
        self.buttons_layout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.arm_button = QPushButton(self.buttons)
        self.arm_button.setObjectName("arm_button")
        self.arm_button.setEnabled(True)
        self.arm_button.setSizePolicy(sizePolicy8)
        self.arm_button.setMinimumSize(QSize(30, 30))
        self.arm_button.setMaximumSize(QSize(16777215, 150))
        self.arm_button.setBaseSize(QSize(30, 30))
        self.arm_button.setFont(font)
        self.arm_button.setMouseTracking(True)
        self.arm_button.setTabletTracking(False)
        self.arm_button.setAutoFillBackground(False)
        self.arm_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(255, 85, 0);\n"
            "color:rgb(255,255,255);\n"
            "}\n"
            "QPushButton::hover{\n"
            "    background-color: rgb(255, 85, 0);\n"
            "    border-color: rgb(60, 231, 195);\n"
            "    border-style: outset;\n"
            "    color: rgb(255,255,255);\n"
            "    border-width: 2px;\n"
            "    border-radius: 12px;\n"
            "    padding: 6px;\n"
            "}\n"
            "QPushButton::pressed{\n"
            "    background-color:rgb(115, 38, 0);\n"
            "}"
        )
        self.arm_button.setFlat(False)

        self.buttons_layout.addWidget(self.arm_button, 1, 1, 1, 1)

        self.trigger_button = QPushButton(self.buttons)
        self.trigger_button.setObjectName("capture_button")
        self.trigger_button.setEnabled(True)
        self.trigger_button.setSizePolicy(sizePolicy8)
        self.trigger_button.setMinimumSize(QSize(50, 40))
        self.trigger_button.setMaximumSize(QSize(16777215, 150))
        self.trigger_button.setBaseSize(QSize(30, 30))
        self.trigger_button.setFont(font)
        self.trigger_button.setMouseTracking(True)
        self.trigger_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(179, 179, 0);\n"
            "}\n"
            "QPushButton::hover{\n"
            "    background-color: rgb(179, 179, 0);\n"
            "    border-color: rgb(60, 231, 195);\n"
            "    border-style: outset;\n"
            "    color: rgb(255,255,255);\n"
            "    border-width: 2px;\n"
            "    border-radius: 12px;\n"
            "    padding: 6px;\n"
            "}\n"
            "QPushButton::pressed{\n"
            "    background-color:rgb(74, 74, 0);\n"
            "}"
        )
        self.trigger_button.setFlat(False)

        self.buttons_layout.addWidget(self.trigger_button, 0, 0, 1, 1)

        self.start_button = QPushButton(self.buttons)
        self.start_button.setObjectName("start_button")
        self.start_button.setSizePolicy(sizePolicy8)
        self.start_button.setMinimumSize(QSize(30, 30))
        self.start_button.setMaximumSize(QSize(16777215, 150))
        self.start_button.setBaseSize(QSize(30, 30))
        self.start_button.setFont(font)
        self.start_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.start_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(0, 85, 0);\n"
            "color:rgb(255,255,255);\n"
            "}\n"
            "QPushButton::hover{\n"
            "background-color: rgb(0, 85, 0);\n"
            "    border-color: rgb(60, 231, 195);\n"
            "    border-style: outset;\n"
            "    color: rgb(255,255,255);\n"
            "    border-width: 2px;\n"
            "    border-radius: 12px;\n"
            "    padding: 6px;\n"
            "}\n"
            "QPushButton::pressed{\n"
            "background-color: rgb(0, 60, 0);\n"
            "color:rgb(255,255,255);\n"
            "}"
        )
        self.start_button.setFlat(False)
        self.buttons_layout.addWidget(self.start_button, 0, 1, 1, 1)

        self.preview_button = QPushButton(self.buttons)
        self.preview_button.setObjectName(u"preview_button")
        self.preview_button.setEnabled(True)
        self.preview_button.setSizePolicy(sizePolicy8)
        self.preview_button.setMinimumSize(QSize(30, 30))
        self.preview_button.setMaximumSize(QSize(16777215, 150))
        self.preview_button.setBaseSize(QSize(30, 30))
        self.preview_button.setFont(font)
        self.preview_button.setMouseTracking(True)
        self.preview_button.setTabletTracking(False)
        self.preview_button.setAutoFillBackground(False)
        self.preview_button.setStyleSheet(u"QPushButton{\n"
                                          "background-color: rgb(0, 170, 255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "}\n"
                                          "QPushButton::hover{\n"
                                          "    background-color:  rgb(0, 170, 255);\n"
                                          "    border-color: rgb(60, 231, 195);\n"
                                          "    border-style: outset;\n"
                                          "    color: rgb(255,255,255);\n"
                                          "    border-width: 2px;\n"
                                          "    border-radius: 12px;\n"
                                          "    padding: 6px;\n"
                                          "}\n"
                                          "QPushButton::pressed{\n"
                                          "    background-color:rgb(0, 75, 112);\n"
                                          "}")
        self.preview_button.setFlat(False)

        self.buttons_layout.addWidget(self.preview_button, 1, 0, 1, 1)

        self.controls_layout.addWidget(self.buttons)

        self.left_pane_layout.addWidget(self.controls)

        self.main_layout.addWidget(self.left_pane, 0, 0, 1, 1)

        main_window.setCentralWidget(self.main_container)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCamera_Info = QMenu(self.menubar)
        self.menuCamera_Info.setObjectName("menuCamera_Info")
        self.menuCamera_Info.setEnabled(False)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setMinimumSize(QSize(0, 0))
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCamera_Info.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(
            QCoreApplication.translate(
                "main_window", "Dewan Lab FLIR Blackfly S Camera Acquisition", None
            )
        )
        self.actionExit.setText(QCoreApplication.translate("main_window", "Exit", None))
        self.actionOpen.setText(QCoreApplication.translate("main_window", "Open", None))
        self.actionSave.setText(QCoreApplication.translate("main_window", "Save", None))
        self.actionSave_As.setText(
            QCoreApplication.translate("main_window", "Save As", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("main_window", "About", None)
        )
        self.param_header.setText(
            QCoreApplication.translate("main_window", "Parameters", None)
        )
        self.current_exposure_label.setText(
            QCoreApplication.translate(
                "main_window", "Current Exposure Time (\u03bcS):", None
            )
        )
        self.current_exposure_data.setText(
            QCoreApplication.translate("main_window", "0", None)
        )
        self.current_fps_label.setText(
            QCoreApplication.translate("main_window", "Current Framerate (FPS):", None)
        )
        self.current_fps_data.setText(
            QCoreApplication.translate("main_window", "0", None)
        )
        self.max_fps_label.setText(
            QCoreApplication.translate("main_window", "Max Framerate (FPS):", None)
        )
        self.max_fps_data.setText(QCoreApplication.translate("main_window", "0", None))
        self.s_per_trial_label.setText(
            QCoreApplication.translate("main_window", "Seconds per Trial:", None)
        )
        self.s_per_trial_data.setText(
            QCoreApplication.translate("main_window", "0", None)
        )
        self.num_frames_label.setText(
            QCoreApplication.translate("main_window", "Number of Frames:", None)
        )
        self.num_frames_data.setText(
            QCoreApplication.translate("main_window", "0", None)
        )
        self.controls_header.setText(
            QCoreApplication.translate("main_window", "Controls", None)
        )
        self.acquisition_mode.setTitle(
            QCoreApplication.translate("main_window", "Acquisition Mode", None)
        )
        self.acquisition_mode_data.setItemText(
            0, QCoreApplication.translate("main_window", "Continuous", None)
        )
        self.acquisition_mode_data.setItemText(
            1, QCoreApplication.translate("main_window", "Single Frame", None)
        )
        self.acquisition_mode_data.setItemText(
            2, QCoreApplication.translate("main_window", "Frame Burst", None)
        )
        self.exposure_control.setTitle(
            QCoreApplication.translate("main_window", "Exposure", None)
        )
        self.exposure_mode.setItemText(
            0, QCoreApplication.translate("main_window", "Manual Exposure", None)
        )
        self.exposure_mode.setItemText(
            1, QCoreApplication.translate("main_window", "Automatic Single Shot", None)
        )
        self.exposure_mode.setItemText(
            2,
            QCoreApplication.translate(
                "main_window", "Automatic Continuous (Variable FPS)", None
            ),
        )
        self.exposure_value.setSuffix(
            QCoreApplication.translate("main_window", "(\u03bcS)", None)
        )
        self.exposure_apply.setText(
            QCoreApplication.translate("main_window", "Apply", None)
        )
        self.s_per_trial.setTitle(
            QCoreApplication.translate("main_window", "Seconds per Trial", None)
        )
        self.trigger_control.setTitle(
            QCoreApplication.translate("main_window", "Trigger Selection", None)
        )
        self.trigger_source_selection.setItemText(
            0, QCoreApplication.translate("main_window", "Software", None)
        )
        self.trigger_source_selection.setItemText(
            1, QCoreApplication.translate("main_window", "Line 1", None)
        )
        self.trigger_source_selection.setItemText(
            2, QCoreApplication.translate("main_window", "Line 2", None)
        )
        self.trigger_source_selection.setItemText(
            3, QCoreApplication.translate("main_window", "Line 3", None)
        )

        self.preview_button.setText(
            QCoreApplication.translate("main_window", "LIVE\nPREVIEW", None)
        )
        self.trigger_button.setText(
            QCoreApplication.translate("main_window", "MANUAL\nTRIGGER", None)
        )
        self.start_button.setText(
            QCoreApplication.translate("main_window", "START\nACQUISITION", None)
        )
        self.arm_button.setText(
            QCoreApplication.translate("main_window", "ARM\nTRIGGER", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("main_window", "File", None))
        self.menuCamera_Info.setTitle(
            QCoreApplication.translate("main_window", "Camera Info", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", "Help", None))

    # retranslateUi
