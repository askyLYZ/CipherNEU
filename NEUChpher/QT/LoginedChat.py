# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.9

from PyQt5 import QtCore, QtGui, QtWidgets
import Resource.LogedResource
import GlobalWindow
from QT import Login,Register,Setting,FilePath,LoginedChat,EnDecryptionSetting,LoginedChat
from Cipher import RSA #ECC
from Cipher import Caesar, Affine, Keyword, CA, ColumnPermutation, DES, DH, DoubleTransposition, AutokeyPlaintext, AutokeyCiphertext, MD5, Multiliteral, Permutation, Playfair, RC4, Vigenere#, AES
from Socket.Packet import *

class Ui_Dialog(object):
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 493)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 671, 453))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(800, 150))
        self.textEdit.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 1, 6)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(30, 30))
        self.graphicsView.setMaximumSize(QtCore.QSize(100, 100))
        self.graphicsView.setSizeIncrement(QtCore.QSize(0, 0))
        self.graphicsView.setBaseSize(QtCore.QSize(0, 0))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("border-image: url(:/images/user.png);\n"
"border-image: url(:/images/user1.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(200, 60))
        self.label_4.setText("")
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Lucida Handwriting\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        #self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        #self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        #self.pushButton.setObjectName("pushButton")
        #self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setSizeIncrement(QtCore.QSize(100, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 6, 1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 6, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_3 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_3.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet("border-image: url(:/images/lock1.png);")
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_2.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet("border-image: url(:/images/key1.png);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton_4 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_4.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet("border-image: url(:/images/export.png);")
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setMaximumSize(QtCore.QSize(25, 30))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("border-image: url(:/images/download1.png);")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 7, 1, 1)
        self.textEdit.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 721, 521))
        self.frame.setStyleSheet("background-image: url(:/images/background1.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #self.label_4.setText(_translate("Dialog", "Welcome!\n"))
        self.comboBox.setItemText(0, _translate("Dialog", "Plaintext"))
        self.comboBox.setItemText(1, _translate("Dialog", "Ciphertext"))
        self.label_3.setText(_translate("Dialog", "Messages:"))
        #self.pushButton.setText(_translate("Dialog", "Settings"))
        self.pushButton_2.setText(_translate("Dialog", "Logout"))
        self.label.setText(_translate("Dialog", "To:"))
        self.label_2.setText(_translate("Dialog", "My messages:"))
        self.toolButton_3.setText(_translate("Dialog", "   "))
        self.toolButton_2.setText(_translate("Dialog", "   "))
        self.toolButton_4.setText(_translate("Dialog", "   "))
        self.toolButton.setText(_translate("Dialog", "   "))
        self.pushButton_4.setText(_translate("Dialog", "Preview"))
        self.pushButton_8.setText(_translate("Dialog", "Send"))

#登陆窗口对象
class LoginedChatWindow(QtWidgets.QWidget,Ui_Dialog):  
    filetext = ''
    content = ''
    toPersonName = ''

    def __init__(self):    
        super(LoginedChatWindow,self).__init__()    
        self.logedWindow = None
        self.loginWindow=None
        self.setupUi(self) 
        self.DisplayTip()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint )        #只允许最小和关闭，不允许最大化,不允许调整大小
        #控件映射
        self.pushButton_8.clicked.connect(self.EncryptPrint)
        self.pushButton_4.clicked.connect(self.ShowMessage)
        #self.pushButton.clicked.connect(self.OpenSettingWindows)
        self.pushButton_2.clicked.connect(self.Logout)
        self.toolButton_3.clicked.connect(self.OpenEncryptionSettingWindows)
        self.toolButton_2.clicked.connect(self.OpenDecryptionSettingWindows)
        self.toolButton_4.clicked.connect(self.ReadFile)
        self.toolButton.clicked.connect(self.SaveFile) 
        
    #显示悬停提示
    def DisplayTip(self): 
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10)) 
        self.toolButton_3.setToolTip('encryption setting')
        self.toolButton_2.setToolTip('decryption setting')
        self.toolButton_4.setToolTip('export file')
        self.toolButton.setToolTip('download file')

    #读取文件
    def ReadFile(self):
        openFile = QtWidgets.QFileDialog()
        self.path, filetype = openFile.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "Text Files (*.txt)")   
        if self.path != '':
            document = open(self.path,"r")
            self.content = document.readlines()
            self.content = ''.join(self.content)
            self.textEdit.setText(self.content)
            GlobalWindow.isFile = True
            document.close()

    #保存文件
    def SaveFile(self):
        savefile = QtWidgets.QFileDialog()
        filepath,filetype= savefile.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",
                                    "Text Files (*.txt)")
        if filepath != '':
            document = open(filepath,"wb")
            document.write(self.filetext)
            document.close()

    #发送对象
    def GetToPersonName(self):
        self.toPersonName = self.lineEdit.text()

    #打印双机加密信息
    def ShowMessage(self):
        message = QtWidgets.QMessageBox()
        str = self.textEdit.toPlainText()
        length = len(self.textEdit.toPlainText())
        wideth = int(length * (3/5))
        for i in range(int(length/wideth)):
            str = str[:i*22+wideth]+'\n'+str[i*22+wideth:]
        message.about(self,"Ciphertext",str)
    #打印单机加解密信息
    def EncryptPrint(self):
        if(self.comboBox.currentText()=='Encryption'):
            self.Encryption()
        elif(self.comboBox.currentText()=='Decryption'):
            self.Decryption()

    #根据不同加解密类型加解密
    def DefineCipherType(self,text,endeMode):      #endeMode = 0 -> encryption/ endeMode = 1 -> decryption
        Text = ''
        if(endeMode==0):
            if(EnDecryptionSetting.enCipherType=='Caesar'):
                Text = Caesar.Encrypt(text,int(EnDecryptionSetting.encryptKey))
            elif(EnDecryptionSetting.enCipherType=='Affine'):
                Text = Affine.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Keyword'):
                Text = Keyword.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Multiliteral'):
                Text = Multiliteral.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Vigenere'):
                Text = Vigenere.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Autokey Ciphertext'):
                Text = AutokeyCiphertext.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Autokey Plaintext'):
                Text = AutokeyPlaintext.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Playfair'):
                Text = Playfair.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Permutation'):
                Text = Permutation.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Column Permutation'):
                Text = ColumnPermutation.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='Double Transposition'):
                Text = DoubleTransposition.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='RC4'):
                Text = RC4.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='CA'):
                Text = CA.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='DES'):
                Text = DES.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='AES-128'|EnDecryptionSetting.enCipherType=='AES-192'|EnDecryptionSetting.enCipherType=='AES-256'):
                Text = AES.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='RSA'):
                Text = RSA.Encrypt(text,EnDecryptionSetting.encryptKey)
            #elif(EnDecryptionSetting.enCipherType=='ECC'):
                #Text = ECC.Encrypt(text,EnDecryptionSetting.encryptKey)
            elif(EnDecryptionSetting.enCipherType=='MD5'):
                Text = MD5.Encrypt(text,EnDecryptionSetting.encryptKey)
            #elif(EnDecryptionSetting.enCipherType=='DSA'):
                #Text = DSA.Encrypt(text,EnDecryptionSetting.encryptKey)
            #elif(EnDecryptionSetting.enCipherType=='DH'):
                #Text = DH.Encrypt(text,EnDecryptionSetting.encryptKey)
        elif(endeMode==1):
            if(EnDecryptionSetting.deCipherType=='Caesar'):
                Text = Caesar.Decrypt(text,int(EnDecryptionSetting.decryptKey))
            elif(EnDecryptionSetting.deCipherType=='Affine'):
                Text = Affine.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Keyword'):
                Text = Keyword.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Multiliteral'):
                Text = Multiliteral.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Vigenere'):
                Text = Vigenere.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Autokey Ciphertext'):
                Text = AutokeyCiphertext.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Autokey Plaintext'):
                Text = AutokeyPlaintext.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Playfair'):
                Text = Playfair.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Permutation'):
                Text = Permutation.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Column Permutation'):
                Text = ColumnPermutation.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='Double Transposition'):
                Text = DoubleTransposition.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='RC4'):
                Text = RC4.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='CA'):
                Text = CA.Encrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='DES'):
                DES.DESDecryption(text,EnDecryptionSetting.decryptKey)
            #elif(EnDecryptionSetting.deCipherType=='AES'):
                #Text = AES.Ddecrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='RSA'):
                Text = RSA.Decrypt(text,EnDecryptionSetting.decryptKey)
            #elif(EnDecryptionSetting.deCipherType=='ECC'):
                #Text = ECC.Decrypt(text,EnDecryptionSetting.decryptKey)
            elif(EnDecryptionSetting.deCipherType=='MD5'):
                Text = MD5.Decrypt(text,EnDecryptionSetting.decryptKey)
            #elif(EnDecryptionSetting.deCipherType=='DSA'):
                #Text = DSA.Decrypt(text,EnDecryptionSetting.decryptKey)
            #elif(EnDecryptionSetting.deCipherType=='DH'):
                #Text = DH.Decrypt(text,EnDecryptionSetting.decryptKey)
        return Text 

    #加密
    def Encryption(self):
        plaintext = self.textEdit.toPlainText()
        ciphertext = self.DefineCipherType(plaintext,0)
        self.filetext = 'Plaintext: '+plaintext+'\n'+'Ciphertext: '+ciphertext
        self.textBrowser.setText(self.textBrowser.toPlainText()+'Plaintext: '+plaintext+'\n'+'Ciphertext: '+ciphertext+'\n\n')
    
    #解密
    def Decryption(self):
        ciphertext = self.textEdit.toPlainText()
        plaintext = self.DefineCipherType(ciphertext,1)
        filetext = plaintext
        self.textBrowser.setText(self.textBrowser.toPlainText()+'Ciphertext: '+ciphertext+'\n'+'Plaintext: '+plaintext+'\n\n')  


    #打开加密设置窗口
    def OpenEncryptionSettingWindows(self):
        self.EnSettingWindows = EnDecryptionSetting.EncryptionSettingWindow()
        self.EnSettingWindows.show()

    #打开解密设置窗口
    def OpenDecryptionSettingWindows(self):
        self.DeSettingWindows = EnDecryptionSetting.DecryptionSettingWindow()
        self.DeSettingWindows.show()

    #退出已登录窗口
    def Logout(self):
        GlobalWindow.s.sendall(PktToBytes(Packet(TYP_LOO, GlobalWindow.username, b'server', b'')))
        recv_tmp = GlobalWindow.s.recv(PKT_MAX_SIZE)
        pkt = BytesToPkt(recv_tmp)
        if pkt.typ != TYP_ACK:
            message = QtWidgets.QMessageBox()
            message.warning(self,"Error","登出失败！",QtWidgets.QMessageBox.Yes)
            return
        else:
            message = QtWidgets.QMessageBox()
            message.information(self,"Pass","登出成功！",QtWidgets.QMessageBox.Yes)
            GlobalWindow.s.close()
            GlobalWindow.globalWindow.chatwindow.show()
            self.close()
