import sys
from qt_material import apply_stylesheet, list_themes
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication,QFileDialog
from qrGenUi import Ui_MainWindow
import qrcode
from PyQt5.QtGui import QPixmap

class clsQrGen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.txt , self.filName = "" , ""
        self.ui.btnGen.clicked.connect(self.btnGenEvent)
        # self.ui.btnDowmload.clicked.connect(self.btnDowmload)
        self.ui.btnClose.clicked.connect(self.close)


    def qrGenCode(self , txt):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(txt)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('business_card_qr_with_location.png')
        print("QR code with location generated and saved as 'business_card_qr_with_location.png'")

    def btnGenEvent(self):
        # self.txt = f"""BEGIN:VCARD
        # VERSION:3.0
        # FN:{self.ui.txtName.text()}
        # ORG:{self.ui.txtBuisName.text()}
        # TITLE:{self.ui.txtTitel.text()}
        # TEL;TYPE=WORK,VOICE:+91 {self.ui.txtContact.text()}
        # ADR;TYPE=WORK:;;{self.ui.txtAddress.text()}
        # EMAIL:{self.ui.txtEmail.text()}
        # URL:{self.ui.txtUrl.text()}
        # END:VCARD"""
        self.txt = """BEGIN:VCARD
        VERSION:3.0
        FN:Paresh Jain
        ORG:LiefIndai Company
        TITLE:Clothing (brand)
        TEL;TYPE=WORK,VOICE:+91 98819 89786
        ADR;TYPE=WORK:;;Jain Dharmashala, Resham Oil, Shahid Chowk, Nagpur, India, Maharashtra
        EMAIL:info@liefindia.com
        URL:http://www.liefindia.in/
        X-INSTAGRAM:https://www.instagram.com/liefindia
        X-FACEBOOK:https://www.facebook.com/people/LiefIndiaLIEF-INDIA/61550840871376/
        GEO:21.155426025390625;79.11104583740234&
        END:VCARD"""
        self.qrGenCode(self.txt)



if __name__ == '__main__':
    app = QApplication([])
    f = clsQrGen()
    f.show()
    # print(list_themes())
    # apply_stylesheet(app, "dark_blue.xml")
    sys.exit(app.exec_())
