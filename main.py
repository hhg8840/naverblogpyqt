import sys
from bs4 import BeautifulSoup
import urllib.request as req
from PyQt5.QtWidgets import *
from lib.BasicLayout import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.initSignal()

    # 화면 초기화
    def initUi(self):
        self.pb_sel.setEnabled(False)
        self.pte_idlist.clear()

    def initSignal(self):
        self.le_blogurl.textChanged.connect(self.chkUrlInput)
        self.pb_sel.clicked.connect(self.getblogid)

    def chkUrlInput(self):
        self.pb_sel.setEnabled(True)
        self.pte_idlist.clear()

    def getblogid(self):
        self.pb_sel.setEnabled(False)
        blogurl = self.le_blogurl.text()
        naverid = blogurl.split('/')[3]
        blognumber = blogurl.split('/')[4]
        url = "https://blog.naver.com/SympathyHistoryList.naver?blogId=" + naverid + "&logNo=" + blognumber + "&layoutWidthClassName=contw-966"

        res = req.urlopen(url).read()
        soup = BeautifulSoup(res, "html.parser")
        list_li = soup.select("div#post-area > ul.list_sympathy > li.item > div > div > span > a.link.pcol2")

        for li in list_li:
            title = li.attrs['title']
            href = li.attrs['href']
            # print(href.split('/')[3])
            self.pte_idlist.appendPlainText(href.split('/')[3])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
