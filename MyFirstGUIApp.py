# imports
from ui import *
from pytube import YouTube
from pytube import Playlist
import os
import sys


class Test(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.d_v.clicked.connect(self.download_video)
        self.d_pl.clicked.connect(self.download_playlist)

    def download_video(self):
        self.v_stat.setText('status')
        url = self.Vid_URL.text()
        print('Starting Download For', url)
        try:
            YouTube(url).streams.filter(resolution='720p').first().download()
            self.v_stat.setText('Downloaded!')
        except:
            self.v_stat.setText('Error')
            print("Error: Make Sure You Enter A Video URL")

    def download_playlist(self):
        self.pl_stat.setText('status')
        p = self.PL_URL.text()
        pl = Playlist(p)
        print('Starting Download For', p)
        for url in pl:
            YouTube(url).streams.filter(resolution='720p').first().download()
        self.pl_stat.setText('Downloaded!')



app = QtWidgets.QApplication(sys.argv)
mainwindow = QtWidgets.QMainWindow()

ui = Test(mainwindow)
mainwindow.show()
app.exec_()
