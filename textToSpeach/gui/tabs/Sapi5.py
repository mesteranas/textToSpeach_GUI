import os
import guiTools
import NBSapi
tts=NBSapi.NBSapi()
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
from settings import language
language.init_translation()
class SAPI5 (qt.QWidget):
    def __init__(self,p):
        super().__init__(p)
        self.p=p
        self.text=qt.QLineEdit()
        self.text.setAccessibleName(_("text"))
        self.rate=qt.QSlider()
        self.rate.setRange(-10,10)
        self.rate.setValue(getrate())
        self.rate.setAccessibleName(_("rate"))
        self.volume=qt.QSlider()
        self.volume.setRange(0,100)
        self.volume.setValue(getv())
        self.volume.setAccessibleName(_("volume"))
        self.lang=qt.QComboBox()
        self.lang.setAccessibleName(_("select voice"))
        self.lang.addItems(getvoicesL())
        self.save=qt.QPushButton(_("save"))
        self.save.setDefault(True)
        self.save.clicked.connect(self.fsave)
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.rate)
        layout.addWidget(self.volume)
        layout.addWidget(self.lang)
        layout.addWidget(self.save)
    def fsave(self):
        file=qt.QFileDialog(self)
        file.setDefaultSuffix("wav")
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptSave)
        file.setNameFilters(["audio files(*.wav)"])
        if file.exec() == qt.QFileDialog.DialogCode.Accepted:
            save(self.text.text(),self.rate.value(),self.volume.value(),self.lang.currentText(),file.selectedFiles()[0])
            m=qt.QMessageBox()
            m.setText(_("file saved successfully \n do you want to   open it ?"))
            m.setWindowTitle(_("done"))
            b1=m.addButton(qt.QMessageBox.StandardButton.Yes)
            b1.setText(_("open file"))
            b2=m.addButton(qt.QMessageBox.StandardButton.No)
            b2.setText(_("cloce"))
            m.exec()
            x=m.clickedButton()
            if x==b1:
                os.startfile(file.selectedFiles()[0])
def getrate():
    return tts.GetRate()
def getv():
    return tts.GetVolume()
def getvoicesL():
    l=[]
    v=tts.GetVoices()
    for voice in v:
        l.append(voice["Description"])
    return l
def save(text,rate,volume,voice,path):
    tts.SetRate(rate)
    tts.SetVolume(volume)
    tts.SetVoice(voice,"by_description")
    tts.SpeakToFile(text,path,0)
