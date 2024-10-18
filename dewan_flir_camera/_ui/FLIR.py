# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FLIR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QAbstractSpinBox, QComboBox, QDoubleSpinBox,
                               QFrame, QGraphicsView, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QLayout, QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
                               QWidget)

class MainUI(object):
    def __init__(self, main_ui):
        self.main_ui = main_ui
        self.about_widget = []

        self.setupUi(main_ui)

    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.setWindowModality(Qt.WindowModality.WindowModal)
        main_window.resize(720, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(720, 550))
        main_window.setDocumentMode(False)
        main_window.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionExit = QAction(main_window)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpen = QAction(main_window)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(main_window)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(main_window)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.main_container = QWidget(main_window)
        self.main_container.setObjectName(u"main_container")
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_layout = QGridLayout(self.main_container)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setHorizontalSpacing(4)
        self.main_layout.setVerticalSpacing(0)
        self.main_layout.setContentsMargins(4, 4, 4, 4)
        self.viewport = QGraphicsView(self.main_container)
        self.viewport.setObjectName(u"viewport")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewport.sizePolicy().hasHeightForWidth())
        self.viewport.setSizePolicy(sizePolicy1)

        self.main_layout.addWidget(self.viewport, 0, 1, 1, 1)

        self.left_pane = QFrame(self.main_container)
        self.left_pane.setObjectName(u"left_pane")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_pane.sizePolicy().hasHeightForWidth())
        self.left_pane.setSizePolicy(sizePolicy2)
        self.left_pane.setFrameShape(QFrame.Shape.Box)
        self.left_pane.setFrameShadow(QFrame.Shadow.Raised)
        self.left_pane.setLineWidth(1)
        self.left_pane_layout = QVBoxLayout(self.left_pane)
        self.left_pane_layout.setSpacing(0)
        self.left_pane_layout.setObjectName(u"left_pane_layout")
        self.left_pane_layout.setContentsMargins(0, 0, 0, 0)
        self.param_disp = QWidget(self.left_pane)
        self.param_disp.setObjectName(u"param_disp")
        sizePolicy2.setHeightForWidth(self.param_disp.sizePolicy().hasHeightForWidth())
        self.param_disp.setSizePolicy(sizePolicy2)
        self.param_disp.setMinimumSize(QSize(0, 120))
        self.param_disp.setMaximumSize(QSize(228, 110))
#if QT_CONFIG(statustip)
        self.param_disp.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.param_disp.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.param_disp.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.param_disp.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.param_disp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.param_disp_layout = QVBoxLayout(self.param_disp)
        self.param_disp_layout.setObjectName(u"param_disp_layout")
        self.param_disp_layout.setContentsMargins(2, 2, 2, 2)
        self.current_exposure_widget = QWidget(self.param_disp)
        self.current_exposure_widget.setObjectName(u"current_exposure_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.current_exposure_widget.sizePolicy().hasHeightForWidth())
        self.current_exposure_widget.setSizePolicy(sizePolicy3)
        self.current_exposure_disp_layout = QHBoxLayout(self.current_exposure_widget)
        self.current_exposure_disp_layout.setObjectName(u"current_exposure_disp_layout")
        self.current_exposure_disp_layout.setContentsMargins(-1, 0, -1, 0)
        self.current_exposure_label = QLabel(self.current_exposure_widget)
        self.current_exposure_label.setObjectName(u"current_exposure_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.current_exposure_label.sizePolicy().hasHeightForWidth())
        self.current_exposure_label.setSizePolicy(sizePolicy4)

        self.current_exposure_disp_layout.addWidget(self.current_exposure_label)

        self.current_exposure_data = QLabel(self.current_exposure_widget)
        self.current_exposure_data.setObjectName(u"current_exposure_data")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.current_exposure_data.sizePolicy().hasHeightForWidth())
        self.current_exposure_data.setSizePolicy(sizePolicy5)

        self.current_exposure_disp_layout.addWidget(self.current_exposure_data)


        self.param_disp_layout.addWidget(self.current_exposure_widget)

        self.current_framerate_widget = QWidget(self.param_disp)
        self.current_framerate_widget.setObjectName(u"current_framerate_widget")
        sizePolicy3.setHeightForWidth(self.current_framerate_widget.sizePolicy().hasHeightForWidth())
        self.current_framerate_widget.setSizePolicy(sizePolicy3)
        self.current_FPS_disp_layout = QHBoxLayout(self.current_framerate_widget)
        self.current_FPS_disp_layout.setObjectName(u"current_FPS_disp_layout")
        self.current_FPS_disp_layout.setContentsMargins(-1, 0, -1, 0)
        self.current_fps_label = QLabel(self.current_framerate_widget)
        self.current_fps_label.setObjectName(u"current_fps_label")
        sizePolicy4.setHeightForWidth(self.current_fps_label.sizePolicy().hasHeightForWidth())
        self.current_fps_label.setSizePolicy(sizePolicy4)

        self.current_FPS_disp_layout.addWidget(self.current_fps_label)

        self.current_fps_data = QLabel(self.current_framerate_widget)
        self.current_fps_data.setObjectName(u"current_fps_data")
        sizePolicy5.setHeightForWidth(self.current_fps_data.sizePolicy().hasHeightForWidth())
        self.current_fps_data.setSizePolicy(sizePolicy5)

        self.current_FPS_disp_layout.addWidget(self.current_fps_data)


        self.param_disp_layout.addWidget(self.current_framerate_widget)

        self.max_framerate_widget = QWidget(self.param_disp)
        self.max_framerate_widget.setObjectName(u"max_framerate_widget")
        sizePolicy3.setHeightForWidth(self.max_framerate_widget.sizePolicy().hasHeightForWidth())
        self.max_framerate_widget.setSizePolicy(sizePolicy3)
        self.max_framerate_disp_layout = QHBoxLayout(self.max_framerate_widget)
        self.max_framerate_disp_layout.setObjectName(u"max_framerate_disp_layout")
        self.max_framerate_disp_layout.setContentsMargins(9, 0, -1, 0)
        self.max_fps_label = QLabel(self.max_framerate_widget)
        self.max_fps_label.setObjectName(u"max_fps_label")
        sizePolicy4.setHeightForWidth(self.max_fps_label.sizePolicy().hasHeightForWidth())
        self.max_fps_label.setSizePolicy(sizePolicy4)

        self.max_framerate_disp_layout.addWidget(self.max_fps_label)

        self.max_fps_data = QLabel(self.max_framerate_widget)
        self.max_fps_data.setObjectName(u"max_fps_data")
        sizePolicy5.setHeightForWidth(self.max_fps_data.sizePolicy().hasHeightForWidth())
        self.max_fps_data.setSizePolicy(sizePolicy5)

        self.max_framerate_disp_layout.addWidget(self.max_fps_data)


        self.param_disp_layout.addWidget(self.max_framerate_widget)

        self.s_per_trial_widget = QWidget(self.param_disp)
        self.s_per_trial_widget.setObjectName(u"s_per_trial_widget")
        sizePolicy3.setHeightForWidth(self.s_per_trial_widget.sizePolicy().hasHeightForWidth())
        self.s_per_trial_widget.setSizePolicy(sizePolicy3)
        self.s_per_trial_disp_layout = QHBoxLayout(self.s_per_trial_widget)
        self.s_per_trial_disp_layout.setObjectName(u"s_per_trial_disp_layout")
        self.s_per_trial_disp_layout.setContentsMargins(9, 0, -1, 0)
        self.s_per_trial_label = QLabel(self.s_per_trial_widget)
        self.s_per_trial_label.setObjectName(u"s_per_trial_label")
        sizePolicy4.setHeightForWidth(self.s_per_trial_label.sizePolicy().hasHeightForWidth())
        self.s_per_trial_label.setSizePolicy(sizePolicy4)

        self.s_per_trial_disp_layout.addWidget(self.s_per_trial_label)

        self.s_per_trial_data = QLabel(self.s_per_trial_widget)
        self.s_per_trial_data.setObjectName(u"s_per_trial_data")
        sizePolicy5.setHeightForWidth(self.s_per_trial_data.sizePolicy().hasHeightForWidth())
        self.s_per_trial_data.setSizePolicy(sizePolicy5)

        self.s_per_trial_disp_layout.addWidget(self.s_per_trial_data)


        self.param_disp_layout.addWidget(self.s_per_trial_widget)

        self.num_frames_widget = QWidget(self.param_disp)
        self.num_frames_widget.setObjectName(u"num_frames_widget")
        sizePolicy3.setHeightForWidth(self.num_frames_widget.sizePolicy().hasHeightForWidth())
        self.num_frames_widget.setSizePolicy(sizePolicy3)
        self.num_frames_layout = QHBoxLayout(self.num_frames_widget)
        self.num_frames_layout.setObjectName(u"num_frames_layout")
        self.num_frames_layout.setContentsMargins(9, 0, -1, 0)
        self.num_frames_label = QLabel(self.num_frames_widget)
        self.num_frames_label.setObjectName(u"num_frames_label")
        sizePolicy4.setHeightForWidth(self.num_frames_label.sizePolicy().hasHeightForWidth())
        self.num_frames_label.setSizePolicy(sizePolicy4)

        self.num_frames_layout.addWidget(self.num_frames_label)

        self.num_frames_data = QLabel(self.num_frames_widget)
        self.num_frames_data.setObjectName(u"num_frames_data")
        sizePolicy5.setHeightForWidth(self.num_frames_data.sizePolicy().hasHeightForWidth())
        self.num_frames_data.setSizePolicy(sizePolicy5)

        self.num_frames_layout.addWidget(self.num_frames_data)


        self.param_disp_layout.addWidget(self.num_frames_widget)


        self.left_pane_layout.addWidget(self.param_disp)

        self.controls = QWidget(self.left_pane)
        self.controls.setObjectName(u"controls")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.controls.sizePolicy().hasHeightForWidth())
        self.controls.setSizePolicy(sizePolicy6)
        self.controls_layout = QVBoxLayout(self.controls)
        self.controls_layout.setObjectName(u"controls_layout")
        self.controls_layout.setContentsMargins(2, 2, 2, 2)
        self.acquisition_mode = QGroupBox(self.controls)
        self.acquisition_mode.setObjectName(u"acquisition_mode")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.acquisition_mode.sizePolicy().hasHeightForWidth())
        self.acquisition_mode.setSizePolicy(sizePolicy7)
        font = QFont()
        font.setBold(True)
        self.acquisition_mode.setFont(font)
        self.acquisition_mode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.acquisition_mode_layout = QVBoxLayout(self.acquisition_mode)
        self.acquisition_mode_layout.setSpacing(0)
        self.acquisition_mode_layout.setObjectName(u"acquisition_mode_layout")
        self.acquisition_mode_layout.setContentsMargins(0, 2, 0, 2)
        self.acquisition_mode_data = QComboBox(self.acquisition_mode)
        self.acquisition_mode_data.addItem("")
        self.acquisition_mode_data.addItem("")
        self.acquisition_mode_data.addItem("")
        self.acquisition_mode_data.setObjectName(u"acquisition_mode_data")

        self.acquisition_mode_layout.addWidget(self.acquisition_mode_data)


        self.controls_layout.addWidget(self.acquisition_mode)

        self.exposure_control = QGroupBox(self.controls)
        self.exposure_control.setObjectName(u"exposure_control")
        sizePolicy7.setHeightForWidth(self.exposure_control.sizePolicy().hasHeightForWidth())
        self.exposure_control.setSizePolicy(sizePolicy7)
        self.exposure_control.setFont(font)
        self.exposure_control.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exposure_layout = QVBoxLayout(self.exposure_control)
        self.exposure_layout.setSpacing(6)
        self.exposure_layout.setObjectName(u"exposure_layout")
        self.exposure_layout.setContentsMargins(0, 2, 0, 2)
        self.exposure_mode = QComboBox(self.exposure_control)
        self.exposure_mode.addItem("")
        self.exposure_mode.addItem("")
        self.exposure_mode.addItem("")
        self.exposure_mode.setObjectName(u"exposure_mode")
        self.exposure_mode.setEditable(False)

        self.exposure_layout.addWidget(self.exposure_mode)

        self.exposure_value = QSpinBox(self.exposure_control)
        self.exposure_value.setObjectName(u"exposure_value")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.exposure_value.setFont(font1)
        self.exposure_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.exposure_value.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.exposure_value.setAccelerated(True)
        self.exposure_value.setProperty(u"showGroupSeparator", False)
        self.exposure_value.setMinimum(1)
        self.exposure_value.setMaximum(99999999)
        self.exposure_value.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.exposure_value.setDisplayIntegerBase(10)

        self.exposure_layout.addWidget(self.exposure_value)

        self.center_apply_button = QWidget(self.exposure_control)
        self.center_apply_button.setObjectName(u"center_apply_button")
        sizePolicy5.setHeightForWidth(self.center_apply_button.sizePolicy().hasHeightForWidth())
        self.center_apply_button.setSizePolicy(sizePolicy5)
        self.center_apply_button_layout = QHBoxLayout(self.center_apply_button)
        self.center_apply_button_layout.setSpacing(0)
        self.center_apply_button_layout.setObjectName(u"center_apply_button_layout")
        self.center_apply_button_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.center_apply_button_layout.setContentsMargins(2, 2, 2, 0)
        self.exposure_apply = QPushButton(self.center_apply_button)
        self.exposure_apply.setObjectName(u"exposure_apply")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.exposure_apply.sizePolicy().hasHeightForWidth())
        self.exposure_apply.setSizePolicy(sizePolicy8)

        self.center_apply_button_layout.addWidget(self.exposure_apply)


        self.exposure_layout.addWidget(self.center_apply_button)


        self.controls_layout.addWidget(self.exposure_control)

        self.s_per_trial = QGroupBox(self.controls)
        self.s_per_trial.setObjectName(u"s_per_trial")
        sizePolicy7.setHeightForWidth(self.s_per_trial.sizePolicy().hasHeightForWidth())
        self.s_per_trial.setSizePolicy(sizePolicy7)
        self.s_per_trial.setFont(font)
        self.s_per_trial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.secondsper_trial_layout = QHBoxLayout(self.s_per_trial)
        self.secondsper_trial_layout.setSpacing(6)
        self.secondsper_trial_layout.setObjectName(u"secondsper_trial_layout")
        self.secondsper_trial_layout.setContentsMargins(0, 2, 0, 2)
        self.s_per_trial_val = QDoubleSpinBox(self.s_per_trial)
        self.s_per_trial_val.setObjectName(u"s_per_trial_val")
        self.s_per_trial_val.setFont(font1)
        self.s_per_trial_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.s_per_trial_val.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.s_per_trial_val.setAccelerated(True)
        self.s_per_trial_val.setProperty(u"showGroupSeparator", False)
        self.s_per_trial_val.setSuffix(u"(s)")
        self.s_per_trial_val.setDecimals(2)
        self.s_per_trial_val.setMinimum(1.000000000000000)
        self.s_per_trial_val.setMaximum(999999.000000000000000)
        self.s_per_trial_val.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.s_per_trial_val.setValue(2.000000000000000)

        self.secondsper_trial_layout.addWidget(self.s_per_trial_val)


        self.controls_layout.addWidget(self.s_per_trial)

        self.buttons = QFrame(self.controls)
        self.buttons.setObjectName(u"buttons")
        sizePolicy6.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy6)
        self.buttons.setMinimumSize(QSize(0, 50))
        self.buttons.setMaximumSize(QSize(16777215, 150))
        self.buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.buttons_layout = QGridLayout(self.buttons)
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.start_button = QPushButton(self.buttons)
        self.start_button.setObjectName(u"start_button")
        sizePolicy7.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy7)
        self.start_button.setMinimumSize(QSize(50, 40))
        self.start_button.setMaximumSize(QSize(16777215, 150))
        self.start_button.setBaseSize(QSize(30, 30))
        self.start_button.setFont(font)
        self.start_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.start_button.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.start_button.setFlat(False)

        self.buttons_layout.addWidget(self.start_button, 1, 0, 1, 1)

        self.arm_button = QPushButton(self.buttons)
        self.arm_button.setObjectName(u"arm_button")
        self.arm_button.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.arm_button.sizePolicy().hasHeightForWidth())
        self.arm_button.setSizePolicy(sizePolicy7)
        self.arm_button.setMinimumSize(QSize(50, 40))
        self.arm_button.setMaximumSize(QSize(16777215, 150))
        self.arm_button.setBaseSize(QSize(30, 30))
        self.arm_button.setFont(font)
        self.arm_button.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color:rgb(0, 0, 0);")
        self.arm_button.setFlat(False)

        self.buttons_layout.addWidget(self.arm_button, 0, 1, 1, 1)

        self.stop_button = QPushButton(self.buttons)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy7)
        self.stop_button.setMinimumSize(QSize(50, 40))
        self.stop_button.setMaximumSize(QSize(16777215, 150))
        self.stop_button.setBaseSize(QSize(30, 30))
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet(u"background-color:rgb(129, 0, 0);\n"
"")
        self.stop_button.setFlat(False)

        self.buttons_layout.addWidget(self.stop_button, 1, 1, 1, 1)

        self.capture_button = QPushButton(self.buttons)
        self.capture_button.setObjectName(u"capture_button")
        sizePolicy7.setHeightForWidth(self.capture_button.sizePolicy().hasHeightForWidth())
        self.capture_button.setSizePolicy(sizePolicy7)
        self.capture_button.setMinimumSize(QSize(50, 40))
        self.capture_button.setMaximumSize(QSize(16777215, 150))
        self.capture_button.setBaseSize(QSize(30, 30))
        self.capture_button.setFont(font)
        self.capture_button.setStyleSheet(u"background-color: rgb(179, 179, 0);\n"
"color: rgb(0, 0, 0);")
        self.capture_button.setFlat(False)

        self.buttons_layout.addWidget(self.capture_button, 0, 0, 1, 1)


        self.controls_layout.addWidget(self.buttons)


        self.left_pane_layout.addWidget(self.controls)


        self.main_layout.addWidget(self.left_pane, 0, 0, 1, 1)

        main_window.setCentralWidget(self.main_container)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuCamera_Info = QMenu(self.menubar)
        self.menuCamera_Info.setObjectName(u"menuCamera_Info")
        self.menuCamera_Info.setEnabled(False)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
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
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Dewan Lab FLIR Blackfly S Camera Acquisition", None))
        self.actionExit.setText(QCoreApplication.translate("main_window", u"Exit", None))
        self.actionOpen.setText(QCoreApplication.translate("main_window", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("main_window", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("main_window", u"Save As", None))
        self.actionAbout.setText(QCoreApplication.translate("main_window", u"About", None))
        self.current_exposure_label.setText(QCoreApplication.translate("main_window", u"Current Exposure Time (\u03bcS):", None))
        self.current_exposure_data.setText(QCoreApplication.translate("main_window", u"0", None))
        self.current_fps_label.setText(QCoreApplication.translate("main_window", u"Current Framerate (FPS):", None))
        self.current_fps_data.setText(QCoreApplication.translate("main_window", u"0", None))
        self.max_fps_label.setText(QCoreApplication.translate("main_window", u"Max Framerate (FPS):", None))
        self.max_fps_data.setText(QCoreApplication.translate("main_window", u"0", None))
        self.s_per_trial_label.setText(QCoreApplication.translate("main_window", u"Seconds per Trial:", None))
        self.s_per_trial_data.setText(QCoreApplication.translate("main_window", u"0", None))
        self.num_frames_label.setText(QCoreApplication.translate("main_window", u"Number of Frames:", None))
        self.num_frames_data.setText(QCoreApplication.translate("main_window", u"0", None))
        self.acquisition_mode.setTitle(QCoreApplication.translate("main_window", u"Acquisition Mode", None))
        self.acquisition_mode_data.setItemText(0, QCoreApplication.translate("main_window", u"Frame Burst", None))
        self.acquisition_mode_data.setItemText(1, QCoreApplication.translate("main_window", u"Continuous", None))
        self.acquisition_mode_data.setItemText(2, QCoreApplication.translate("main_window", u"Single Frame", None))

        self.exposure_control.setTitle(QCoreApplication.translate("main_window", u"Exposure", None))
        self.exposure_mode.setItemText(0, QCoreApplication.translate("main_window", u"Automatic Single Shot", None))
        self.exposure_mode.setItemText(1, QCoreApplication.translate("main_window", u"Manual Exposure", None))
        self.exposure_mode.setItemText(2, QCoreApplication.translate("main_window", u"Automatic Continuous (Variable FPS)", None))

        self.exposure_mode.setCurrentText(QCoreApplication.translate("main_window", u"Automatic Single Shot", None))
        self.exposure_value.setSuffix(QCoreApplication.translate("main_window", u"(\u03bcS)", None))
        self.exposure_apply.setText(QCoreApplication.translate("main_window", u"Apply", None))
        self.s_per_trial.setTitle(QCoreApplication.translate("main_window", u"Seconds per Trial", None))
        self.start_button.setText(QCoreApplication.translate("main_window", u"START", None))
        self.arm_button.setText(QCoreApplication.translate("main_window", u"ARM", None))
        self.stop_button.setText(QCoreApplication.translate("main_window", u"STOP", None))
        self.capture_button.setText(QCoreApplication.translate("main_window", u"CAPTURE", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.menuCamera_Info.setTitle(QCoreApplication.translate("main_window", u"Camera Info", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"Help", None))
    # retranslateUi

