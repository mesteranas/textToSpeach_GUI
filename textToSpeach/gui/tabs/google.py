import os
import guiTools
import gtts
from guiTools.dictionarys import languages
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
from settings import language
language.init_translation()
class Google (qt.QWidget):
    def __init__(self,p):
        super().__init__(p)
        self.p=p
        self.text=qt.QLineEdit()
        self.text.setAccessibleName(_("text"))
        self.lang=qt.QComboBox()
        self.lang.setAccessibleName(_("select language"))
        self.lang.addItems(['Albanian', 'Arabic', 'Bosnian', 'Bulgarian', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Finnish', 'French', 'German', 'Gujarati', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Khmer', 'Korean', 'Latvian', 'Lithuanian', 'Malay', 'Malayalam', 'Nepali', 'Norwegian', 'Polish', 'Portuguese', 'Russian', 'Slovak', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh'])
        self.save=qt.QPushButton(_("save"))
        self.save.setDefault(True)
        self.save.clicked.connect(self.fsave)
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.lang)
        layout.addWidget(self.save)
    def fsave(self):
        file=qt.QFileDialog(self)
        file.setDefaultSuffix("mp3")
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptSave)
        file.setNameFilters(["audio files(*.mp3)"])
        if file.exec() == qt.QFileDialog.DialogCode.Accepted:
            google(self.text.text(),file.selectedFiles()[0],languages[self.lang.currentText()])
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


def google(text,fileName,language):
    s=gtts.gTTS(text,lang=language)
    s.save(fileName)
