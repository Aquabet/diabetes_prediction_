'''
TODO A:
Change the value in the setText function from N/A to the output value of the corresponding model, such as YES or NO.
TODO B:
Drawing function. I used the random function to generate the image. Change it to the required image.
'''
import sys
from PyQt5.QtWidgets import *
from Ui_Widget import *
import numpy as np
import random
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
import induce


class mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Diabetes Prediction")
        # self.addToolBar(NavigationToolbar(self.plot.canvas, self))

    def predict_clicked(self):
        self.update_graph()
        if (self.lineEdit_Pregnancies.text() == '' or
           self.lineEdit_Glucose.text() == '' or
           self.lineEdit_BloodPressure.text() == '' or
           self.lineEdit_SkinThickness.text() == '' or
           self.lineEdit_Insulin.text() == '' or
           self.lineEdit_BMI.text() == '' or
           self.lineEdit_DiabetesPedigree.text() == '' or
           self.lineEdit_Age.text() == ''
            ):
            QMessageBox.about(self, 'Warning', 'Please enter data.')
            return

        if (self.checkBox_1.isChecked() == False and
                self.checkBox_2.isChecked() == False and
                self.checkBox_3.isChecked() == False and
                self.checkBox_4.isChecked() == False and
                self.checkBox_5.isChecked() == False and
                self.checkBox_6.isChecked() == False and
                self.checkBox_7.isChecked() == False
                ):
            QMessageBox.about(self, 'Warning', 'Please choose model.')
            return

        # init data field
        self.label_ans_dt.setText("N/A")
        self.label_ans_final.setText("N/A")
        self.label_ans_nb.setText("N/A")
        self.label_ans_lr.setText("N/A")
        self.label_ans_mlp.setText("N/A")
        self.label_ans_rf.setText("N/A")
        self.label_ans_knn.setText("N/A")
        self.label_ans_svm.setText("N/A")

        # run
        data = [float(self.lineEdit_Pregnancies.text()),
                float(self.lineEdit_Glucose.text()),
                float(self.lineEdit_BloodPressure.text()),
                float(self.lineEdit_SkinThickness.text()),
                float(self.lineEdit_Insulin.text()),
                float(self.lineEdit_BMI.text()),
                float(self.lineEdit_DiabetesPedigree.text()),
                float(self.lineEdit_Age.text())]
        data = np.array(data)
        modelList = ['svm', 'rf', 'mlp', 'logistic', 'nb', 'dt', 'knn']
        ans = induce.Induce(data, modelList)
        print(ans)
        if self.checkBox_1.isChecked() == True:
            self.label_ans_svm.setText(str(round(ans[0], 3)))

        if self.checkBox_2.isChecked() == True:
            self.label_ans_rf.setText(str(round(ans[1], 3)))

        if self.checkBox_3.isChecked() == True:
            self.label_ans_mlp.setText(str(round(ans[2], 3)))

        if self.checkBox_4.isChecked() == True:
            self.label_ans_lr.setText(str(round(ans[3], 3)))

        if self.checkBox_5.isChecked() == True:
            self.label_ans_nb.setText(str(round(ans[4], 3)))

        if self.checkBox_6.isChecked() == True:
            self.label_ans_dt.setText(str(round(ans[5], 3)))

        if self.checkBox_7.isChecked() == True:
            self.label_ans_knn.setText(str(round(ans[6], 3)))

        self.label_ans_final.setText(str(round(ans[7], 3)))

    def update_graph(self):
        pass

        # fs = 500
        # f = random.randint(1,  100)
        # ts = 1 / fs
        # length_of_signal = 100
        # t = np.linspace(0, 1, length_of_signal)

        # cosinus_signal = np.cos(2 * np.pi * f * t)
        # sinus_signal = np.sin(2 * np.pi * f * t)
        # # draw this signal
        # self.plot.canvas.axes.clear()
        # self.plot.canvas.axes.plot(t, cosinus_signal)
        # self.plot.canvas.axes.plot(t, sinus_signal)
        # self.plot.canvas.axes.legend(
        #     ('cosinus', 'sinus'), loc='upper right')
        # self.plot.canvas.axes.set_title('Cosinus - Sinus Signal')
        # self.plot.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
