import sqlite3
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

import connection as c
from UIs.main_ui import Ui_MainWindow



class View():
    def __init__(self, to, f, subject, txt, date):
        self.clck = None
        self.ui_file = QFile("UIs/view.ui")
        self.loader = QUiLoader()
        self.ui_file.open(QFile.ReadOnly)
        self.view_window = self.loader.load(self.ui_file)
        self.ui_file.close()
        self.view_window.tolabel.setText("To: " + to)
        self.view_window.fromlabel.setText("From: " + f)
        self.view_window.textlabel.setText(txt)
        self.view_window.datelabel.setText("Date: " + date)
        self.view_window.subjectlabel.setText("Subject: " + subject)
        self.view_window.setWindowTitle("Details")
        self.view_window.show()


class Mail:
    def __init__(self, to, f, txt, date):
        self.ui_file = QFile("UIs/mail.ui")
        self.loader = QUiLoader()
        self.ui_file.open(QFile.ReadOnly)
        self.widget = self.loader.load(self.ui_file)
        self.widget.tolabel.setText("To: " + to)
        self.widget.fromlabel.setText("From: " + f)
        self.widget.textlabel.setText(txt)
        self.widget.datelabel.setText(date)

    def get_widget(self):
        return self.widget


class Address:
    def __init__(self, address, checked, item):
        self.item = item
        self.ui_file = QFile("UIs/address.ui")
        self.loader = QUiLoader()
        self.ui_file.open(QFile.ReadOnly)
        self.widget = self.loader.load(self.ui_file)
        self.address = address
        self.widget.address.setText(address)
        self.widget.active.setChecked(checked)
        self.widget.delete_button.clicked.connect(lambda: MainWindow.remove_address(window, self.item, address))
        self.widget.active.clicked.connect(self.switch_active)

    def get_widget(self):
        return self.widget

    def switch_active(self):
        if self.widget.active.isChecked():
            inactive.remove(self.address)
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("UPDATE addresses SET active = 1 WHERE address = ?", (self.address,))
            con.commit()
            cur.close()
            con.close()
        else:
            inactive.append(self.address)
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("UPDATE addresses SET active = 0 WHERE address = ?", (self.address,))
            con.commit()
            cur.close()
            con.close()


mails = []
addresses = []
inactive = []


class MainWindow(QMainWindow):
    def new_view(self, item):
        for i in self.con.cursor().execute("SELECT * FROM mails WHERE id = ?", (str(item.whatsThis()),)):
            self.view = View(i[1], i[2], i[4], i[5], i[3])

    def close(self) -> bool:
        self.con.close()
        super().close()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)

        self.ui.menu_top_bar.mousePressEvent = self.mpe
        self.ui.menu_top_bar.mouseMoveEvent = self.mme


        self.view = None
        self.ui.mailList.itemActivated.connect(self.new_view)

        self.ui.side_menu.hide()

        self.ui.menu_button.clicked.connect(
            lambda: self.ui.side_menu.show() if self.ui.side_menu.isHidden() else self.ui.side_menu.hide())

        self.ui.random_button.clicked.connect(self.gen_random_mail)

        self.ui.add_button.clicked.connect(self.add_btn)

        self.ui.refresh_button.clicked.connect(self.get_mails)

        for i in c.get_domains():
            self.ui.combo_box.addItem("@" + i)

        self.con = sqlite3.connect('database.db')
        cur = self.con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS addresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT NOT NULL,
            active BOOLEAN NOT NULL
            );""")

        cur.execute("""CREATE TABLE IF NOT EXISTS mails (
                    id INTEGER PRIMARY KEY,
                    to_address TEXT NOT NULL,
                    from_address TEXT NOT NULL,
                    date TEXT NOT NULL,
                    subject TEXT,
                    content TEXT
                    );""")


        for row in cur.execute("SELECT * FROM addresses"):
            self.draw_address(row[1], row[2])
            if not bool(row[2]):
                inactive.append(row[1])

        for row in cur.execute("SELECT * FROM mails"):
            self.draw_mail(row[0], row[1], row[2], row[4], row[5], row[3])
            mails.append(str(row[0]))

        self.get_mails()

    def get_mails(self):
        for e in addresses:
            a = e.split("@")
            for i in c.get_mailbox(a[0], a[1]):
                if str(i['id']) not in inactive and not str(i['id']) in mails:
                    self.add_mail(int(i['id']), e, i['from'], i['subject'],
                                  c.fetch_msg(a[0], a[1], i['id'])['textBody'], i['date'])

    def remove_address(self, item, adr):
        self.ui.address_list.removeItemWidget(item)
        self.ui.address_list.takeItem(self.ui.address_list.indexFromItem(item).row())
        addresses.remove(adr)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("DELETE FROM addresses WHERE address=?", (adr,))
        con.commit()
        con.close()

    def draw_address(self, address, active):
        item = QtWidgets.QListWidgetItem()
        addresses.append(address)
        widget = Address(address, active, item).get_widget()
        item.setSizeHint(widget.size())
        self.ui.address_list.addItem(item)
        self.ui.address_list.setItemWidget(item, widget)

    def draw_mail(self, id, to, f, sub, txt, date):
        mail = Mail(to, f, "Subject: " + sub + "\n" + txt, date)
        item = QtWidgets.QListWidgetItem()
        item.setWhatsThis(str(id))
        widget = mail.get_widget()
        item.setSizeHint(widget.size())
        self.ui.mailList.addItem(item)
        self.ui.mailList.setItemWidget(item, widget)



    def add_mail(self, id, to, f, sub, txt, date):
        cur = self.con.cursor()
        cur.execute("INSERT INTO mails (id, to_address, from_address, date, subject, content) values (?,?,?,?,?,?)",
                    (id, to, f, date, sub, txt))
        self.con.commit()
        self.draw_mail(id, to, f, sub, txt, date)


    def add_address(self, email):
        cur = self.con.cursor()
        cur.execute("INSERT INTO addresses(address,active) values (?, ?)",
                    (email, 1))
        self.con.commit()
        self.draw_address(email, 1)

    def add_btn(self):
        if self.ui.email_edit.text() != "" and self.ui.email_edit.text() + self.ui.combo_box.currentText() not in addresses:
            self.add_address(self.ui.email_edit.text() + self.ui.combo_box.currentText())


    def gen_random_mail(self):
        cur = self.con.cursor()
        mail = c.gen_random()
        cur.execute("INSERT INTO addresses(address,active) values (?, ?)", (mail, 1))
        self.con.commit()
        self.draw_address(mail, 1)

    def mpe(self, event):
        self.click_pos = event.globalPosition().toPoint()

    def mme(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.click_pos)
            self.click_pos = event.globalPosition().toPoint()
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
