# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
from dewan_flir_camera.UI import resources_rc

class ABOUT(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.setWindowModality(Qt.WindowModality.WindowModal)
        about.resize(549, 202)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(about.sizePolicy().hasHeightForWidth())
        about.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        about.setFont(font)
        self.main_layout = QGridLayout(about)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(2, 2, 2, 4)
        self.close = QDialogButtonBox(about)
        self.close.setObjectName(u"close")
        self.close.setOrientation(Qt.Orientation.Horizontal)
        self.close.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        self.close.setCenterButtons(True)

        self.main_layout.addWidget(self.close, 1, 0, 1, 1)

        self.container = QWidget(about)
        self.container.setObjectName(u"container")
        self.content_layout = QVBoxLayout(self.container)
        self.content_layout.setObjectName(u"content_layout")
        self.top_row = QWidget(self.container)
        self.top_row.setObjectName(u"top_row")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_row.sizePolicy().hasHeightForWidth())
        self.top_row.setSizePolicy(sizePolicy1)
        self.top_row.setMinimumSize(QSize(0, 48))
        self.top_row_layout = QHBoxLayout(self.top_row)
        self.top_row_layout.setSpacing(7)
        self.top_row_layout.setObjectName(u"top_row_layout")
        self.top_row_layout.setContentsMargins(0, 0, 0, 0)
        self.image = QLabel(self.top_row)
        self.image.setObjectName(u"image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy2)
        self.image.setMaximumSize(QSize(48, 48))
        self.image.setPixmap(QPixmap(u":/resources/images/mouse.jpg"))
        self.image.setScaledContents(True)

        self.top_row_layout.addWidget(self.image)

        self.name = QLabel(self.top_row)
        self.name.setObjectName(u"name")
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.name.setFont(font1)

        self.top_row_layout.addWidget(self.name)


        self.content_layout.addWidget(self.top_row)

        self.credits = QLabel(self.container)
        self.credits.setObjectName(u"credits")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.credits.sizePolicy().hasHeightForWidth())
        self.credits.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(12)
        self.credits.setFont(font2)

        self.content_layout.addWidget(self.credits)

        self.version = QLabel(self.container)
        self.version.setObjectName(u"version")
        sizePolicy3.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy3)
        self.version.setFont(font2)

        self.content_layout.addWidget(self.version)

        self.github_link = QLabel(self.container)
        self.github_link.setObjectName(u"github_link")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.github_link.sizePolicy().hasHeightForWidth())
        self.github_link.setSizePolicy(sizePolicy4)
        self.github_link.setFont(font)
        self.github_link.setStyleSheet(u"color: rgb(0, 85, 255)")
        self.github_link.setOpenExternalLinks(True)
        self.github_link.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.content_layout.addWidget(self.github_link)

        self.website_link = QLabel(self.container)
        self.website_link.setObjectName(u"website_link")
        sizePolicy4.setHeightForWidth(self.website_link.sizePolicy().hasHeightForWidth())
        self.website_link.setSizePolicy(sizePolicy4)
        self.website_link.setFont(font)
        self.website_link.setStyleSheet(u"color: rgb(0, 85, 255)")
        self.website_link.setOpenExternalLinks(True)
        self.website_link.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.content_layout.addWidget(self.website_link)


        self.main_layout.addWidget(self.container, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(about)
        self.close.accepted.connect(about.accept)
        self.close.rejected.connect(about.reject)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About", None))
        self.image.setText("")
        self.name.setText(QCoreApplication.translate("about", u"Dewan Lab FLIR Blackfly S Camera Acquisition Controller", None))
        self.credits.setText(QCoreApplication.translate("about", u"Austin Pauley, Dewan Lab, Florida State University, 2024", None))
        self.version.setText(QCoreApplication.translate("about", u"v 1.0", None))
        self.github_link.setText(QCoreApplication.translate("about", u"<html><head/><body><p><a href=\"htps://github.com/OlfactoryBehaviorLab/\"><span style=\" text-decoration: underline; color:#69fcff;\">htps://github.com/OlfactoryBehaviorLab/</span></a></p></body></html>", None))
        self.website_link.setText(QCoreApplication.translate("about", u"<html><head/><body><p><a href=\"https://dewanlab.neuro.fsu.edu/\"><span style=\" text-decoration: underline; color:#69fcff;\">https://dewanlab.neuro.fsu.edu/</span></a></p></body></html>", None))
    # retranslateUi

