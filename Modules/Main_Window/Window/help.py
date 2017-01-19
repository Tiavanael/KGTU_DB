import os

from PyQt5.QtWidgets import QTextBrowser


class Help(QTextBrowser):

    def __init__(self):
        super(Help, self).__init__()
        f = open('Help/index.html')
        text = f.read()
        f.close()

        self.setHtml(text)
        self.anchorClicked.connect(self.urlParser)

    def urlParser(self, url):
        text = url.toString()
        text = os.path.join('Help', text.strip())
        f = open(text)
        html = f.read()
        f.close()
        self.setHtml(html)
