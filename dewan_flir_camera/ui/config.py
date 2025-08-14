# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QDialog,
)


class Ui_config_wizard(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirm_button.clicked.connect(self.accept)

    def setupUi(self, config_wizard):
        if not config_wizard.objectName():
            config_wizard.setObjectName("config_wizard")
        config_wizard.setWindowModality(Qt.WindowModality.WindowModal)
        config_wizard.resize(650, 185)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(config_wizard.sizePolicy().hasHeightForWidth())
        config_wizard.setSizePolicy(sizePolicy)
        config_wizard.setMinimumSize(QSize(650, 185))
        config_wizard.setMaximumSize(QSize(650, 185))
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        config_wizard.setFont(font)
        config_wizard.setWindowTitle("Experiment Configuration")
        config_wizard.setStyleSheet('font: 12pt "Arial";')
        self.main_layout = QGridLayout(config_wizard)
        self.main_layout.setObjectName("main_layout")
        self.main_layout.setContentsMargins(9, 3, 9, -1)
        self.header = QLabel(config_wizard)
        self.header.setObjectName("header")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies(["Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.header.setFont(font1)
        self.header.setStyleSheet(
            "border-bottom-width: 2px;\n"
            "border-bottom-style: solid;\n"
            "border-radius: 0px;\n"
            "border-color: grey;\n"
            "margin-bottom: 2px;\n"
            'font: 16pt "Arial";'
        )
        self.header.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.main_layout.addWidget(self.header, 1, 0, 1, 1)

        self.button_center_layout = QHBoxLayout()
        self.button_center_layout.setObjectName("button_center_layout")
        self.confirm_button = QPushButton(config_wizard)
        self.confirm_button.setObjectName("confirm_button")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.confirm_button.sizePolicy().hasHeightForWidth()
        )
        self.confirm_button.setSizePolicy(sizePolicy2)
        self.confirm_button.setMaximumSize(QSize(150, 16777215))
        self.confirm_button.setFont(font)

        self.button_center_layout.addWidget(self.confirm_button)

        self.main_layout.addLayout(self.button_center_layout, 3, 0, 1, 1)

        self.control_layout = QGridLayout()
        self.control_layout.setObjectName("control_layout")
        self.control_layout.setVerticalSpacing(6)
        self.mouse_ID_field = QLineEdit(config_wizard)
        self.mouse_ID_field.setObjectName("mouse_ID_field")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.mouse_ID_field.sizePolicy().hasHeightForWidth()
        )
        self.mouse_ID_field.setSizePolicy(sizePolicy3)

        self.control_layout.addWidget(self.mouse_ID_field, 0, 2, 1, 1)

        self.experiment_type_field = QLineEdit(config_wizard)
        self.experiment_type_field.setObjectName("experiment_type_field")
        sizePolicy3.setHeightForWidth(
            self.experiment_type_field.sizePolicy().hasHeightForWidth()
        )
        self.experiment_type_field.setSizePolicy(sizePolicy3)
        self.experiment_type_field.setInputMask("")
        self.experiment_type_field.setFrame(True)
        self.experiment_type_field.setPlaceholderText("Experiment Name")

        self.control_layout.addWidget(self.experiment_type_field, 1, 2, 1, 1)

        self.experiment_type_label = QLabel(config_wizard)
        self.experiment_type_label.setObjectName("experiment_type_label")
        sizePolicy1.setHeightForWidth(
            self.experiment_type_label.sizePolicy().hasHeightForWidth()
        )
        self.experiment_type_label.setSizePolicy(sizePolicy1)

        self.control_layout.addWidget(self.experiment_type_label, 1, 0, 1, 1)

        self.mouse_ID_label = QLabel(config_wizard)
        self.mouse_ID_label.setObjectName("mouse_ID_label")
        sizePolicy1.setHeightForWidth(
            self.mouse_ID_label.sizePolicy().hasHeightForWidth()
        )
        self.mouse_ID_label.setSizePolicy(sizePolicy1)
        # if QT_CONFIG(accessibility)
        self.mouse_ID_label.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.mouse_ID_label.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.mouse_ID_label.setAccessibleIdentifier("")

        self.control_layout.addWidget(self.mouse_ID_label, 0, 0, 1, 1)

        self.dir_input_layout = QHBoxLayout()
        self.dir_input_layout.setSpacing(0)
        self.dir_input_layout.setObjectName("dir_input_layout")
        self.save_path_field = QLineEdit(config_wizard)
        self.save_path_field.setObjectName("save_path_field")

        self.dir_input_layout.addWidget(self.save_path_field)

        self.open_dir_button = QPushButton(config_wizard)
        self.open_dir_button.setObjectName("open_dir_button")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.open_dir_button.sizePolicy().hasHeightForWidth()
        )
        self.open_dir_button.setSizePolicy(sizePolicy4)
        self.open_dir_button.setMaximumSize(QSize(50, 30))
        self.open_dir_button.setFont(font)
        self.open_dir_button.setStyleSheet("")
        # if QT_CONFIG(shortcut)
        self.open_dir_button.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.open_dir_button.setFlat(False)

        self.dir_input_layout.addWidget(self.open_dir_button)

        self.control_layout.addLayout(self.dir_input_layout, 2, 2, 1, 1)

        self.save_dir_label = QLabel(config_wizard)
        self.save_dir_label.setObjectName("save_dir_label")

        self.control_layout.addWidget(self.save_dir_label, 2, 0, 1, 1)

        self.main_layout.addLayout(self.control_layout, 2, 0, 1, 1)

        self.retranslateUi(config_wizard)

        QMetaObject.connectSlotsByName(config_wizard)

    # setupUi

    def retranslateUi(self):
        self.header.setText(
            QCoreApplication.translate("config_wizard", "Configure Experiment", None)
        )
        self.confirm_button.setText(
            QCoreApplication.translate("config_wizard", "Confirm", None)
        )
        self.mouse_ID_field.setPlaceholderText(
            QCoreApplication.translate("config_wizard", "Mouse ID", None)
        )
        self.experiment_type_label.setText(
            QCoreApplication.translate("config_wizard", "Experiment:", None)
        )
        self.mouse_ID_label.setText(
            QCoreApplication.translate("config_wizard", "Mouse ID:", None)
        )
        self.save_path_field.setPlaceholderText(
            QCoreApplication.translate("config_wizard", "Save Directory", None)
        )
        self.open_dir_button.setText(
            QCoreApplication.translate("config_wizard", "Open", None)
        )
        self.save_dir_label.setText(
            QCoreApplication.translate("config_wizard", "Save Directory:", None)
        )
        pass

    # retranslateUi
