# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 694)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.room_name_label = QtWidgets.QLabel(self.centralwidget)
        self.room_name_label.setGeometry(QtCore.QRect(60, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.room_name_label.setFont(font)
        self.room_name_label.setObjectName("room_name_label")
        self.leave = QtWidgets.QPushButton(self.centralwidget)
        self.leave.setGeometry(QtCore.QRect(50, 560, 151, 51))
        self.leave.setObjectName("leave")
        self.guess = QtWidgets.QPushButton(self.centralwidget)
        self.guess.setEnabled(True)
        self.guess.setGeometry(QtCore.QRect(430, 560, 151, 51))
        self.guess.setObjectName("guess")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 60, 533, 483))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.word_6_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_6_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_6_5.sizePolicy().hasHeightForWidth())
        self.word_6_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_6_5.setFont(font)
        self.word_6_5.setTabletTracking(False)
        self.word_6_5.setAcceptDrops(False)
        self.word_6_5.setMaxLength(1)
        self.word_6_5.setFrame(False)
        self.word_6_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_6_5.setObjectName("word_6_5")
        self.gridLayout.addWidget(self.word_6_5, 6, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.word_5_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_5_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_5_1.sizePolicy().hasHeightForWidth())
        self.word_5_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_5_1.setFont(font)
        self.word_5_1.setTabletTracking(False)
        self.word_5_1.setAcceptDrops(False)
        self.word_5_1.setMaxLength(1)
        self.word_5_1.setFrame(False)
        self.word_5_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_5_1.setObjectName("word_5_1")
        self.gridLayout.addWidget(self.word_5_1, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.word_5_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_5_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_5_4.sizePolicy().hasHeightForWidth())
        self.word_5_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_5_4.setFont(font)
        self.word_5_4.setTabletTracking(False)
        self.word_5_4.setAcceptDrops(False)
        self.word_5_4.setMaxLength(1)
        self.word_5_4.setFrame(False)
        self.word_5_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_5_4.setObjectName("word_5_4")
        self.gridLayout.addWidget(self.word_5_4, 5, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.word_6_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_6_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_6_1.sizePolicy().hasHeightForWidth())
        self.word_6_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_6_1.setFont(font)
        self.word_6_1.setTabletTracking(False)
        self.word_6_1.setAcceptDrops(False)
        self.word_6_1.setMaxLength(1)
        self.word_6_1.setFrame(False)
        self.word_6_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_6_1.setObjectName("word_6_1")
        self.gridLayout.addWidget(self.word_6_1, 6, 1, 1, 1)
        self.word_6_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_6_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_6_3.sizePolicy().hasHeightForWidth())
        self.word_6_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_6_3.setFont(font)
        self.word_6_3.setTabletTracking(False)
        self.word_6_3.setAcceptDrops(False)
        self.word_6_3.setMaxLength(1)
        self.word_6_3.setFrame(False)
        self.word_6_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_6_3.setObjectName("word_6_3")
        self.gridLayout.addWidget(self.word_6_3, 6, 3, 1, 1)
        self.word_2_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_2_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_2_3.sizePolicy().hasHeightForWidth())
        self.word_2_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_2_3.setFont(font)
        self.word_2_3.setTabletTracking(False)
        self.word_2_3.setAcceptDrops(False)
        self.word_2_3.setMaxLength(1)
        self.word_2_3.setFrame(False)
        self.word_2_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_2_3.setObjectName("word_2_3")
        self.gridLayout.addWidget(self.word_2_3, 2, 3, 1, 1)
        self.word_2_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_2_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_2_1.sizePolicy().hasHeightForWidth())
        self.word_2_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_2_1.setFont(font)
        self.word_2_1.setTabletTracking(False)
        self.word_2_1.setAcceptDrops(False)
        self.word_2_1.setMaxLength(1)
        self.word_2_1.setFrame(False)
        self.word_2_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_2_1.setObjectName("word_2_1")
        self.gridLayout.addWidget(self.word_2_1, 2, 1, 1, 1)
        self.word_3_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_3_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_3_5.sizePolicy().hasHeightForWidth())
        self.word_3_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_3_5.setFont(font)
        self.word_3_5.setTabletTracking(False)
        self.word_3_5.setAcceptDrops(False)
        self.word_3_5.setMaxLength(1)
        self.word_3_5.setFrame(False)
        self.word_3_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_3_5.setObjectName("word_3_5")
        self.gridLayout.addWidget(self.word_3_5, 3, 5, 1, 1)
        self.word_1_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_1_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_1_4.sizePolicy().hasHeightForWidth())
        self.word_1_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_1_4.setFont(font)
        self.word_1_4.setTabletTracking(False)
        self.word_1_4.setAcceptDrops(False)
        self.word_1_4.setMaxLength(1)
        self.word_1_4.setFrame(False)
        self.word_1_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_1_4.setObjectName("word_1_4")
        self.gridLayout.addWidget(self.word_1_4, 1, 4, 1, 1)
        self.word_6_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_6_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_6_2.sizePolicy().hasHeightForWidth())
        self.word_6_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_6_2.setFont(font)
        self.word_6_2.setTabletTracking(False)
        self.word_6_2.setAcceptDrops(False)
        self.word_6_2.setMaxLength(1)
        self.word_6_2.setFrame(False)
        self.word_6_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_6_2.setObjectName("word_6_2")
        self.gridLayout.addWidget(self.word_6_2, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.word_4_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_4_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_4_1.sizePolicy().hasHeightForWidth())
        self.word_4_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_4_1.setFont(font)
        self.word_4_1.setTabletTracking(False)
        self.word_4_1.setAcceptDrops(False)
        self.word_4_1.setMaxLength(1)
        self.word_4_1.setFrame(False)
        self.word_4_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_4_1.setObjectName("word_4_1")
        self.gridLayout.addWidget(self.word_4_1, 4, 1, 1, 1)
        self.word_2_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_2_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_2_4.sizePolicy().hasHeightForWidth())
        self.word_2_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_2_4.setFont(font)
        self.word_2_4.setTabletTracking(False)
        self.word_2_4.setAcceptDrops(False)
        self.word_2_4.setMaxLength(1)
        self.word_2_4.setFrame(False)
        self.word_2_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_2_4.setObjectName("word_2_4")
        self.gridLayout.addWidget(self.word_2_4, 2, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.word_6_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_6_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_6_4.sizePolicy().hasHeightForWidth())
        self.word_6_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_6_4.setFont(font)
        self.word_6_4.setTabletTracking(False)
        self.word_6_4.setAcceptDrops(False)
        self.word_6_4.setMaxLength(1)
        self.word_6_4.setFrame(False)
        self.word_6_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_6_4.setObjectName("word_6_4")
        self.gridLayout.addWidget(self.word_6_4, 6, 4, 1, 1)
        self.word_1_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_1_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word_1_2.sizePolicy().hasHeightForWidth())
        self.word_1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_1_2.setFont(font)
        self.word_1_2.setTabletTracking(False)
        self.word_1_2.setAcceptDrops(False)
        self.word_1_2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.word_1_2.setMaxLength(1)
        self.word_1_2.setFrame(False)
        self.word_1_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_1_2.setObjectName("word_1_2")
        self.gridLayout.addWidget(self.word_1_2, 1, 2, 1, 1)
        self.word_4_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_4_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_4_3.sizePolicy().hasHeightForWidth())
        self.word_4_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_4_3.setFont(font)
        self.word_4_3.setTabletTracking(False)
        self.word_4_3.setAcceptDrops(False)
        self.word_4_3.setMaxLength(1)
        self.word_4_3.setFrame(False)
        self.word_4_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_4_3.setObjectName("word_4_3")
        self.gridLayout.addWidget(self.word_4_3, 4, 3, 1, 1)
        self.word_5_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_5_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_5_5.sizePolicy().hasHeightForWidth())
        self.word_5_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_5_5.setFont(font)
        self.word_5_5.setTabletTracking(False)
        self.word_5_5.setAcceptDrops(False)
        self.word_5_5.setMaxLength(1)
        self.word_5_5.setFrame(False)
        self.word_5_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_5_5.setObjectName("word_5_5")
        self.gridLayout.addWidget(self.word_5_5, 5, 5, 1, 1)
        self.word_3_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_3_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_3_3.sizePolicy().hasHeightForWidth())
        self.word_3_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_3_3.setFont(font)
        self.word_3_3.setTabletTracking(False)
        self.word_3_3.setAcceptDrops(False)
        self.word_3_3.setMaxLength(1)
        self.word_3_3.setFrame(False)
        self.word_3_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_3_3.setObjectName("word_3_3")
        self.gridLayout.addWidget(self.word_3_3, 3, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.word_2_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_2_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_2_5.sizePolicy().hasHeightForWidth())
        self.word_2_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_2_5.setFont(font)
        self.word_2_5.setTabletTracking(False)
        self.word_2_5.setAcceptDrops(False)
        self.word_2_5.setMaxLength(1)
        self.word_2_5.setFrame(False)
        self.word_2_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_2_5.setObjectName("word_2_5")
        self.gridLayout.addWidget(self.word_2_5, 2, 5, 1, 1)
        self.word_1_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_1_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_1_5.sizePolicy().hasHeightForWidth())
        self.word_1_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_1_5.setFont(font)
        self.word_1_5.setTabletTracking(False)
        self.word_1_5.setAcceptDrops(False)
        self.word_1_5.setMaxLength(1)
        self.word_1_5.setFrame(False)
        self.word_1_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_1_5.setObjectName("word_1_5")
        self.gridLayout.addWidget(self.word_1_5, 1, 5, 1, 1)
        self.word_1_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_1_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_1_1.sizePolicy().hasHeightForWidth())
        self.word_1_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_1_1.setFont(font)
        self.word_1_1.setTabletTracking(False)
        self.word_1_1.setAcceptDrops(False)
        self.word_1_1.setMaxLength(1)
        self.word_1_1.setFrame(False)
        self.word_1_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_1_1.setObjectName("word_1_1")
        self.gridLayout.addWidget(self.word_1_1, 1, 1, 1, 1)
        self.word_1_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_1_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_1_3.sizePolicy().hasHeightForWidth())
        self.word_1_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_1_3.setFont(font)
        self.word_1_3.setTabletTracking(False)
        self.word_1_3.setAcceptDrops(False)
        self.word_1_3.setMaxLength(1)
        self.word_1_3.setFrame(False)
        self.word_1_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_1_3.setObjectName("word_1_3")
        self.gridLayout.addWidget(self.word_1_3, 1, 3, 1, 1)
        self.word_3_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_3_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_3_2.sizePolicy().hasHeightForWidth())
        self.word_3_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_3_2.setFont(font)
        self.word_3_2.setTabletTracking(False)
        self.word_3_2.setAcceptDrops(False)
        self.word_3_2.setMaxLength(1)
        self.word_3_2.setFrame(False)
        self.word_3_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_3_2.setObjectName("word_3_2")
        self.gridLayout.addWidget(self.word_3_2, 3, 2, 1, 1)
        self.word_4_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_4_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_4_4.sizePolicy().hasHeightForWidth())
        self.word_4_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_4_4.setFont(font)
        self.word_4_4.setTabletTracking(False)
        self.word_4_4.setAcceptDrops(False)
        self.word_4_4.setMaxLength(1)
        self.word_4_4.setFrame(False)
        self.word_4_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_4_4.setObjectName("word_4_4")
        self.gridLayout.addWidget(self.word_4_4, 4, 4, 1, 1)
        self.word_2_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_2_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_2_2.sizePolicy().hasHeightForWidth())
        self.word_2_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_2_2.setFont(font)
        self.word_2_2.setTabletTracking(False)
        self.word_2_2.setAcceptDrops(False)
        self.word_2_2.setMaxLength(1)
        self.word_2_2.setFrame(False)
        self.word_2_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_2_2.setObjectName("word_2_2")
        self.gridLayout.addWidget(self.word_2_2, 2, 2, 1, 1)
        self.word_3_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_3_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_3_1.sizePolicy().hasHeightForWidth())
        self.word_3_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_3_1.setFont(font)
        self.word_3_1.setTabletTracking(False)
        self.word_3_1.setAcceptDrops(False)
        self.word_3_1.setMaxLength(1)
        self.word_3_1.setFrame(False)
        self.word_3_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_3_1.setObjectName("word_3_1")
        self.gridLayout.addWidget(self.word_3_1, 3, 1, 1, 1)
        self.word_4_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_4_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_4_2.sizePolicy().hasHeightForWidth())
        self.word_4_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_4_2.setFont(font)
        self.word_4_2.setTabletTracking(False)
        self.word_4_2.setAcceptDrops(False)
        self.word_4_2.setMaxLength(1)
        self.word_4_2.setFrame(False)
        self.word_4_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_4_2.setObjectName("word_4_2")
        self.gridLayout.addWidget(self.word_4_2, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 1)
        self.word_3_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_3_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_3_4.sizePolicy().hasHeightForWidth())
        self.word_3_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_3_4.setFont(font)
        self.word_3_4.setTabletTracking(False)
        self.word_3_4.setAcceptDrops(False)
        self.word_3_4.setMaxLength(1)
        self.word_3_4.setFrame(False)
        self.word_3_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_3_4.setObjectName("word_3_4")
        self.gridLayout.addWidget(self.word_3_4, 3, 4, 1, 1)
        self.word_5_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_5_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_5_3.sizePolicy().hasHeightForWidth())
        self.word_5_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_5_3.setFont(font)
        self.word_5_3.setTabletTracking(False)
        self.word_5_3.setAcceptDrops(False)
        self.word_5_3.setMaxLength(1)
        self.word_5_3.setFrame(False)
        self.word_5_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_5_3.setObjectName("word_5_3")
        self.gridLayout.addWidget(self.word_5_3, 5, 3, 1, 1)
        self.word_5_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_5_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_5_2.sizePolicy().hasHeightForWidth())
        self.word_5_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_5_2.setFont(font)
        self.word_5_2.setTabletTracking(False)
        self.word_5_2.setAcceptDrops(False)
        self.word_5_2.setMaxLength(1)
        self.word_5_2.setFrame(False)
        self.word_5_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_5_2.setObjectName("word_5_2")
        self.gridLayout.addWidget(self.word_5_2, 5, 2, 1, 1)
        self.word_4_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_4_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(61)
        sizePolicy.setHeightForWidth(self.word_4_5.sizePolicy().hasHeightForWidth())
        self.word_4_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word_4_5.setFont(font)
        self.word_4_5.setTabletTracking(False)
        self.word_4_5.setAcceptDrops(False)
        self.word_4_5.setMaxLength(1)
        self.word_4_5.setFrame(False)
        self.word_4_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_4_5.setObjectName("word_4_5")
        self.gridLayout.addWidget(self.word_4_5, 4, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(240, 570, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("status_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.word_1_1, self.word_1_2)
        MainWindow.setTabOrder(self.word_1_2, self.word_1_3)
        MainWindow.setTabOrder(self.word_1_3, self.word_1_4)
        MainWindow.setTabOrder(self.word_1_4, self.word_1_5)
        MainWindow.setTabOrder(self.word_1_5, self.word_2_1)
        MainWindow.setTabOrder(self.word_2_1, self.word_2_2)
        MainWindow.setTabOrder(self.word_2_2, self.word_2_3)
        MainWindow.setTabOrder(self.word_2_3, self.word_2_4)
        MainWindow.setTabOrder(self.word_2_4, self.word_2_5)
        MainWindow.setTabOrder(self.word_2_5, self.word_3_1)
        MainWindow.setTabOrder(self.word_3_1, self.word_3_2)
        MainWindow.setTabOrder(self.word_3_2, self.word_3_3)
        MainWindow.setTabOrder(self.word_3_3, self.word_3_4)
        MainWindow.setTabOrder(self.word_3_4, self.word_3_5)
        MainWindow.setTabOrder(self.word_3_5, self.word_4_1)
        MainWindow.setTabOrder(self.word_4_1, self.word_4_2)
        MainWindow.setTabOrder(self.word_4_2, self.word_4_3)
        MainWindow.setTabOrder(self.word_4_3, self.word_4_4)
        MainWindow.setTabOrder(self.word_4_4, self.word_4_5)
        MainWindow.setTabOrder(self.word_4_5, self.word_5_1)
        MainWindow.setTabOrder(self.word_5_1, self.word_5_2)
        MainWindow.setTabOrder(self.word_5_2, self.word_5_3)
        MainWindow.setTabOrder(self.word_5_3, self.word_5_4)
        MainWindow.setTabOrder(self.word_5_4, self.word_5_5)
        MainWindow.setTabOrder(self.word_5_5, self.word_6_1)
        MainWindow.setTabOrder(self.word_6_1, self.word_6_2)
        MainWindow.setTabOrder(self.word_6_2, self.word_6_3)
        MainWindow.setTabOrder(self.word_6_3, self.word_6_4)
        MainWindow.setTabOrder(self.word_6_4, self.word_6_5)
        MainWindow.setTabOrder(self.word_6_5, self.leave)
        MainWindow.setTabOrder(self.leave, self.guess)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.room_name_label.setText(_translate("MainWindow", "Room name:"))
        self.leave.setText(_translate("MainWindow", "Leave"))
        self.guess.setText(_translate("MainWindow", "Guess"))
        self.label_7.setText(_translate("MainWindow", "     2     "))
        self.label_5.setText(_translate("MainWindow", "     1     "))
        self.label_3.setText(_translate("MainWindow", "     4     "))
        self.label_12.setText(_translate("MainWindow", "     Try №4     "))
        self.label_11.setText(_translate("MainWindow", "     Try №3       "))
        self.label_6.setText(_translate("MainWindow", "     3     "))
        self.label_8.setText(_translate("MainWindow", "     Try №5      "))
        self.label_9.setText(_translate("MainWindow", "     Try №2     "))
        self.label_4.setText(_translate("MainWindow", "     Try №6       "))
        self.label_2.setText(_translate("MainWindow", "     5     "))
        self.label_10.setText(_translate("MainWindow", "     Try №1  "))
