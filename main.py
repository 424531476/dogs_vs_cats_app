import sys
import os
import traceback
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import ui_mainwin
import neural_network

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class MainWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui_mainwin.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('cat or dog')
        self.nn = neural_network.NeuralNetwork()

    def on_click_button(self):
        try:
            file_head = r'file:///'
            file_path = self.ui.path_edit.toPlainText().strip()
            if file_path.startswith(file_head):
                file_path = file_path[len(file_head):]
            if os.path.isfile(file_path):
                file_path = [file_path]
            elif os.path.isdir(file_path):
                filenames = os.listdir(file_path)
                file_path = [os.path.join(file_path, filename) for filename in filenames]
            predict_res = self.nn.predict(file_path)
            predict_res = [i for i in predict_res]
            res_list = list()
            for i in range(len(file_path)):
                pred = '狗' if predict_res[i] > 0.5 else '猫'
                score = abs(predict_res[i] - 0.5) * 2
                res_list.append('%s是%s,自信度%0.3f' % (os.path.split(file_path[i])[1], pred, score))
            msg = '\n'.join(res_list)
            QMessageBox.information(None, 'cat or dog', msg, QMessageBox.Ok, QMessageBox.Ok)
            self.ui.path_edit.setText('')
        except Exception as e:
            print(traceback.format_exc())
            QMessageBox.information(None, 'error', str(e), QMessageBox.Ok, QMessageBox.Ok)


def main() -> int:
    try:
        app = QtWidgets.QApplication(sys.argv)
        win = MainWin()
        win.show()
        return app.exec_()
    except Exception as e:
        print(traceback.format_exc())
        QMessageBox.information(None, 'error', str(e), QMessageBox.Ok, QMessageBox.Ok)
        return 0


if __name__ == '__main__':
    main()
