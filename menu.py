from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import pymysql.cursors
import datetime
total = 0
totalPem = 0
totalPeng = 0
totalDas = 0
def display():
    app = QApplication(sys.argv)
    mW = QMainWindow()
    menubar = mW.menuBar()
    menubar.setVisible(False)
    # exit
    exitAct = QAction('&EXIT')
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    logOut = QAction('&LOGOUT')
    aboutt = QAction('&ABOUT')
    dash = QAction('&DASHBOARD')
    ####
    menubar.addAction(dash)
    menubar.addAction(aboutt)
    menubar.addAction(logOut)
    menubar.addAction(exitAct)
    exitAct.triggered.connect(app.quit)

    def about():
        mess = QMessageBox()
        mess.setWindowTitle("About")
        mess.setText(
            "Nama:Muhammad fahmi ady susilo<br>Nim:190411100127<br>Kelas:Pemrogaman Dekstop (C)<br>Apps:Pencatatan Data Kas")
        mess.setFont(QFont('Arial Rounded MT Bold', 10))
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QMessageBox.Cancel)
        mess.exec_()
    aboutt.triggered.connect(about)

    def totalData():
        global totalPem
        global totalPeng
        global totalDas
        con = pymysql.connect(db='kas1', user='root',
                              passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        cur.execute("SELECT * FROM tbl_kas")
        data = cur.fetchall()
        record = list(data)
        Pem = 0
        Peng = 0
        totalDas = 0
        for i in range(len(record)):
            if str(record[i][4]) != "REKAPAN":
                hasil = (record[i][5])
                totalDas += hasil
            if str(record[i][4]) == "PEMASUKAN":
                Pem += 1
            elif str(record[i][4]) == "PENGELUARAN":
                Peng += 1
        totalPem = Pem
        totalPeng = Peng

    def menu():  # function
        vbox = QVBoxLayout()
        global totalPem
        global totalPeng

        def displayData():
            logOut.setVisible(False)
            win = QWidget()
            parent = QVBoxLayout()
            # label judul
            label1 = QLabel("<h2>KAS ORGANISASI</h2>")
            # label1.setStyleSheet("color:#78290f;")
            label1.setAlignment(Qt.AlignCenter)
            label2 = QLabel("Nama :")
            label2.setFont(QFont('Arial Rounded MT Bold', 8))
            label3 = QLabel("Tanggal :")
            label3.setFont(QFont('Arial Rounded MT Bold', 8))
            label4 = QLabel("Keterangan :")
            label4.setFont(QFont('Arial Rounded MT Bold', 8))
            label5 = QLabel("Transaksi :")
            label5.setFont(QFont('Arial Rounded MT Bold', 8))
            label10 = QLabel("Jumlah uang :")
            label10.setFont(QFont('Arial Rounded MT Bold', 8))
            ######################################
            x = datetime.datetime.now()
            ######################################
            nama = QLineEdit()
            nama.setFont(QFont('Arial Rounded MT Bold', 8))
            nama.setStyleSheet("background-color: #f0e4e1;")
            tanggal = QLineEdit()
            tanggal.setFont(QFont('Arial Rounded MT Bold', 8))
            tanggal.setStyleSheet("background-color: #f0e4e1;")
            ket = QLineEdit()
            ket.setFont(QFont('Arial Rounded MT Bold', 8))
            ket.setStyleSheet("background-color: #f0e4e1;")
            setTang = x.strftime("%d"), x.strftime("%b"), x.strftime("%Y")
            setData = ""
            for i in range(3):
                setData += setTang[i]+" "
            tanggal.setText(setData)
            pem = QRadioButton("Pemasukan")
            pem.setFont(QFont('Arial Rounded MT Bold', 8))
            peng = QRadioButton("Pengeluaran")
            peng.setFont(QFont('Arial Rounded MT Bold', 8))
            rek = QRadioButton("Rekapan")
            rek.setFont(QFont('Arial Rounded MT Bold', 8))
            jumlahUang = QLineEdit()
            jumlahUang.setFont(QFont('Arial Rounded MT Bold', 8))
            jumlahUang.setStyleSheet("background-color: #f0e4e1;")
            from1 = QFormLayout()
            from2 = QFormLayout()
            qv = QHBoxLayout()
            qv.addWidget(pem)
            qv.addWidget(peng)
            qv.addWidget(rek)
            from1.addRow(label2, nama)
            from1.addRow(label3, tanggal)
            from1.addRow(label4, ket)
            from1.addRow(label5, qv)
            from1.addRow(label10, jumlahUang)
            Qh = QHBoxLayout()
            Qh1 = QHBoxLayout()
            from2 = QFormLayout()
            from3 = QFormLayout()
            button1 = QPushButton("TAMBAH")
            button1.setFont(QFont('Arial Rounded MT Bold', 8))
            button1.setStyleSheet("background-color: #36f1cd;")
            button2 = QPushButton("TAMPILKAN SEMUA DATA")
            button2.setFont(QFont('Arial Rounded MT Bold', 8))
            button2.setStyleSheet("background-color: #36f1cd;")
            button3 = QPushButton("FILTER DATA")
            button3.setFont(QFont('Arial Rounded MT Bold', 8))
            button3.setStyleSheet("background-color: #36f1cd;")
            button4 = QPushButton("HAPUS DATA")
            button4.setFont(QFont('Arial Rounded MT Bold', 8))
            button4.setStyleSheet("background-color: #36f1cd;")
            button5 = QPushButton("UBAH DATA")
            button5.setFont(QFont('Arial Rounded MT Bold', 8))
            button5.setStyleSheet("background-color: #36f1cd;")
            #########
            lcd = QLCDNumber()
            lcd.setDigitCount(30)
            lcd.display(total)
            lcd.setStyleSheet("background-color: #13c4a3;")
            filter = QLineEdit()
            filter.setFont(QFont('Arial Rounded MT Bold', 8))
            filter.setStyleSheet("background-color: #f0e4e1;")
            id = QLineEdit()
            id.setFont(QFont('Arial Rounded MT Bold', 8))
            id.setStyleSheet("background-color: #f0e4e1;")
            Qh.addWidget(button1)
            Qh.addWidget(button2)
            label6 = QLabel("ID :")
            label6.setFont(QFont('Arial Rounded MT Bold', 8))
            label7 = QLabel("FILTER :")
            label7.setFont(QFont('Arial Rounded MT Bold', 8))
            from2.addRow(label6, id)
            Qh1.addWidget(button4)
            Qh1.addWidget(button5)
            from3.addRow(label7, filter)
            #########################
            tableData = QTableWidget()
            tableData.setStyleSheet("background-color:white;")
            tableData.verticalHeader().setVisible(False)
            tableData.horizontalHeader().setVisible(False)

            def messageBox(title, message):
                mess = QMessageBox()
                mess.setWindowTitle(title)
                mess.setText(message)
                mess.setFont(QFont('Arial Rounded MT Bold', 10))
                mess.setIcon(QMessageBox.Information)
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec_()

            def tampilData(filt=""):
                global total
                con = pymysql.connect(db='kas1', user='root',
                                      passwd='', host='localhost', port=3306, autocommit=True)
                cur = con.cursor()
                if filt == "":
                    cur.execute("SELECT * FROM tbl_kas")
                else:
                    cur.execute("SELECT * FROM tbl_kas WHERE id LIKE'%" +
                                str(filt)+"%' or nama LIKE '%" +
                                str(filt)+"%' or tanggal LIKE '%"+str(filt) +
                                "%' or keterangan LIKE '%"+str(filt)+"%' or transaksi LIKE '%"+str(filt)+"%' or jumlahuang LIKE '%"+str(filt)+"%'")
                data = cur.fetchall()
                record = list(data)
                tableData.setRowCount(len(record)+1)
                tableData.setColumnCount(6)
                tableData.setItem(0, 0, QTableWidgetItem("ID"))
                tableData.setItem(0, 1, QTableWidgetItem("NAMA"))
                tableData.setItem(0, 2, QTableWidgetItem("TANGGAL"))
                tableData.setItem(0, 3, QTableWidgetItem("KETERANGAN"))
                tableData.setItem(0, 4, QTableWidgetItem("TRANSAKSI"))
                tableData.setItem(0, 5, QTableWidgetItem("JUMLAH UANG"))
                total = 0
                for i in range(len(record)):
                    baris = i + 1
                    tableData.setItem(
                        baris, 0, QTableWidgetItem(str(record[i][0])))
                    tableData.setItem(
                        baris, 1, QTableWidgetItem(str(record[i][1])))
                    tableData.setItem(
                        baris, 2, QTableWidgetItem(str(record[i][2])))
                    tableData.setItem(
                        baris, 3, QTableWidgetItem(str(record[i][3])))
                    tableData.setItem(
                        baris, 4, QTableWidgetItem(str(record[i][4])))
                    tableData.setItem(
                        baris, 5, QTableWidgetItem(str(record[i][5])))
                    if record[i][4] != "REKAPAN":
                        hasil = record[i][5]
                        total += hasil
                tableData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                lcd.display(total)
                vbox.addWidget(tableData)
                return vbox

            def tambahData():
                global total
                nama1 = str(nama.text())
                tanggal1 = str(tanggal.text())
                ket1 = str(ket.text())
                if pem.isChecked() == True:
                    jumlahUang1 = str(jumlahUang.text())
                    transaksi1 = "PEMASUKAN"
                elif peng.isChecked() == True:
                    jumlahUang1 = str("-"+jumlahUang.text())
                    transaksi1 = "PENGELUARAN"
                elif rek.isChecked() == True:
                    jumlahUang1 = str(total)
                    transaksi1 = "REKAPAN"
                else:
                    jumlahUang1 = str(total)
                    transaksi1 = ""
                con = pymysql.connect(db='kas1', user='root',
                                      passwd='', host='localhost', port=3306, autocommit=True)
                cur = con.cursor()
                id = con.cursor()
                id.execute("SELECT id FROM tbl_kas ORDER BY id DESC LIMIT 1")
                id1 = id.fetchone()
                id1 = id1[0] + 1
                sql = "INSERT INTO tbl_kas(id,nama,tanggal,keterangan,transaksi,jumlahuang) VALUES ('%s','%s','%s','%s','%s','%s')" % (
                    id1, nama1, tanggal1, ket1, transaksi1, jumlahUang1)
                data = cur.execute(sql)
                if(data):
                    tampilData()
                    messageBox("BERHASIL", "Data KAS Tersimpan")
                else:
                    messageBox("GAGAL", "Data KAS Gagal Tersimpan")
                nama.setText("")
                tanggal.setText(setData)
                ket.setText("")
                jumlahUang.setText("")

            def ubahData():
                global total
                nama1 = str(nama.text())
                tanggal1 = str(tanggal.text())
                ket1 = str(ket.text())
                id1 = str(id.text())
                if pem.isChecked() == True:
                    jumlahUang1 = str(jumlahUang.text())
                    transaksi1 = "PEMASUKAN"
                elif peng.isChecked() == True:
                    jumlahUang1 = str("-"+jumlahUang.text())
                    transaksi1 = "PENGELUARAN"
                elif rek.isChecked() == True:
                    jumlahUang1 = str(total)
                    transaksi1 = "REKAPAN"
                else:
                    jumlahUang1 = str(total)
                    transaksi1 = ""
                con = pymysql.connect(db='kas1', user='root',
                                      passwd='', host='localhost', port=3306, autocommit=True)
                cur = con.cursor()
                sql = "UPDATE tbl_kas SET nama = '%s', tanggal = '%s', keterangan = '%s', transaksi = '%s', jumlahuang = '%s' WHERE id = '%s'" % (
                    nama1, tanggal1, ket1, transaksi1, jumlahUang1, id1)
                data = cur.execute(sql)
                if(data):
                    tampilData()
                    messageBox("BERHASIL", "Data KAS di Ubah")
                else:
                    messageBox("GAGAL", "Data KAS Gagal di Ubah")
                id.setText("")
                nama.setText("")
                tanggal.setText(setData)
                ket.setText("")
                jumlahUang.setText("")

            def deleteData():
                id1 = str(id.text())
                con = pymysql.connect(db='kas1', user='root',
                                      passwd='', host='localhost', port=3306, autocommit=True)
                cur = con.cursor()
                cur = con.cursor()
                sql = "DELETE FROM tbl_kas WHERE id = '%s' " % (id1)

                data = cur.execute(sql)
                if(data):
                    tampilData()
                    messageBox("BERHASIL", "Data KAS berhasil di hapus")
                else:
                    messageBox("GAGAL", "Data KAS berhasil di hapus")
                id.setText("")

            def filterData():
                filter1 = str(filter.text())
                con = pymysql.connect(db='kas1', user='root',
                                      passwd='', host='localhost', port=3306, autocommit=True)
                cur = con.cursor()
                cur = con.cursor()
                cur.execute("SELECT * FROM tbl_kas WHERE id ='" +
                            str(filter1)+"' or nama ='"+str(filter1)+"' or tanggal ='"+str(filter1)+"' or keterangan='"+str(filter1)+"' or transaksi='"+str(filter1)+"' or jumlahuang='"+str(filter1)+"'")
                try:
                    tampilData(filter1)
                except:
                    messageBox("GAGAL", "Data KAS tidak berhasil di filter")
                else:
                    messageBox("BERHASIL", "Data KAS berhasil di filter")
                filter.setText("")

            def tampilkanDataAll():
                tampilData()
            # Membuat Signal Dan Slot Saat Di Klik
            button1.clicked.connect(tambahData)
            button2.clicked.connect(tampilkanDataAll)
            button3.clicked.connect(filterData)
            button4.clicked.connect(deleteData)
            button5.clicked.connect(ubahData)
            #######################
            #######################
            parent.addWidget(label1)
            parent.addLayout(from1)
            parent.addLayout(Qh)
            parent.addLayout(from2)
            parent.addLayout(Qh1)
            parent.addLayout(from3)
            parent.addWidget(button3)
            parent.addWidget(lcd)
            parent.addLayout(vbox)
            win.setLayout(parent)
            win.setStyleSheet("color:black; background-color:#ff7d00;")
            mW.setCentralWidget(win)
            mW.setWindowTitle("Aplikasi Data Kas")
            mW.setGeometry(300, 100, 640, 600)
            tampilData()
        menubar.setVisible(True)
        parent = QVBoxLayout()
        cwin = QWidget()
        label = QLabel("<h3>SELAMAT DATANG PADA APLIKASI KAS ORGANISASI</h3>")
        label.setStyleSheet("color:#ff7d00;")
        label.setAlignment(Qt.AlignCenter)
        bt = QPushButton("Lanjut >")
        bt.setFont(QFont('Arial Rounded MT Bold', 8))
        bt.setStyleSheet("background-color:#ff7d00; color:white;")
        logOut.setVisible(True)
        #####################
        global totalPem
        global totalPeng
        global totalDas
        totalData()
        labell = QLabel("Data Rekapitulasi")
        labell.setFont(QFont('Arial Rounded MT Bold', 12))
        labelForm = QFormLayout()
        labelPem = QLabel("Total Data Pemasukan   :")
        labelPem.setFont(QFont('Arial Rounded MT Bold', 8))
        labelPem.setStyleSheet("color :white;")
        labelPeng = QLabel("Total Data Pengeluaran :")
        labelPeng.setFont(QFont('Arial Rounded MT Bold', 8))
        labelPeng.setStyleSheet("color :white;")
        labelUang = QLabel("Total Jumlah Uang          :")
        labelUang.setStyleSheet("color :white;")
        labelUang.setFont(QFont('Arial Rounded MT Bold', 8))
        totalPem = str(totalPem)
        totalPeng = str(totalPeng)
        totalUang = str(totalDas)
        Pem = QLabel(totalPem)
        Pem.setStyleSheet("color :white;")
        Pem.setFont(QFont('Arial Rounded MT Bold', 8))
        Peng = QLabel(totalPeng)
        Peng.setFont(QFont('Arial Rounded MT Bold', 8))
        Peng.setStyleSheet("color :white;")
        tot = QLabel(totalUang)
        tot.setFont(QFont('Arial Rounded MT Bold', 8))
        tot.setStyleSheet("color :white;")
        labelForm.addRow(labelPem, Pem)
        labelForm.addRow(labelPeng, Peng)
        labelForm.addRow(labelUang, tot)
        ######################
        parent.addWidget(label)
        parent.addWidget(labell)
        parent.addLayout(labelForm)
        parent.addWidget(bt)
        # connect
        bt.clicked.connect(displayData)

        cwin.setLayout(parent)
        cwin.setStyleSheet("background-color :#2d625f;")
        mW.setCentralWidget(cwin)
        mW.setWindowTitle("Dashboard")
        mW.setGeometry(500,250,300,200)

    def login():  # function
        win = QWidget()
        menubar.setVisible(False)
        parent = QVBoxLayout()
        label = QLabel("<h1><font color=blue>LOGIN</font></h1>")
        label.setAlignment(Qt.AlignCenter)
        labelpic = QLabel()
        pixmap = QPixmap('user.png')
        pixmap = pixmap.scaled(QSize(80, 80))
        labelpic.setPixmap(pixmap)
        labelpic.setAlignment(Qt.AlignCenter)
        label2 = QLabel("Username :")
        label2.setFont(QFont('Arial Rounded MT Bold', 8))
        label3 = QLabel("Password :")
        label3.setFont(QFont('Arial Rounded MT Bold', 8))
        labelPem = QLabel("")
        labelPem.setStyleSheet("color:red;")
        labelPem.setFont(QFont('Arial Rounded MT Bold', 8))
        button = QPushButton("Masuk")
        button.setFont(QFont('Arial Rounded MT Bold', 8))
        button.setStyleSheet("background-color:red; color:white;")
        user = QLineEdit()
        user.setFont(QFont('Arial Rounded MT Bold', 8))
        pwd = QLineEdit()
        pwd.setFont(QFont('Arial Rounded MT Bold', 8))
        pwd.setEchoMode(QLineEdit.Password)
        from1 = QFormLayout()
        from1.addRow(label2, user)
        from1.addRow(label3, pwd)

        def log():
            user1 = str(user.text())
            pwd1 = str(pwd.text())
            if user1 == "admin" and pwd1 == "admin":
                menu()
            else:
                user.setText("")
                pwd.setText("")
                labelPem.setText("Username / Password Salah")
        totalData()
        button.clicked.connect(log)
        parent.addWidget(labelpic)
        parent.addLayout(from1)
        parent.addWidget(labelPem)
        parent.addWidget(button)
        #######################
        win.setLayout(parent)
        win.setStyleSheet("background-color :#2d625f;")
        mW.setCentralWidget(win)
        mW.setGeometry(500, 250, 300, 200)
        mW.setWindowTitle("Login")
    logOut.triggered.connect(login)
    dash.triggered.connect(menu)
    login()
    mW.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    display()
