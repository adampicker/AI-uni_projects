import sys
from PyQt4 import QtGui, QtCore

import os
from PyQt4.QtGui import *

#app = QtGui.QApplication(sys.argv)

#window = QtGui.QWidget()
#window.setGeometry(50,50,500,300)
#window.show()
#app.exec_()



class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,750,500)
        self.setWindowTitle("Pyqt tutaj bedaa")
        self.setWindowIcon(QtGui.QIcon('home/ab/Desktop/tensorflowlogo.png'))

        # quit in File menu
        extractAction = QtGui.QAction("&Quit",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.quit_function)

        # load image in Filemenu
        loadImage = QtGui.QAction("Load Image",self)
        loadImage.setShortcut("Ctrl+I")
        loadImage.setStatusTip('Load Image')
        loadImage.triggered.connect(self.load_image)

        # help in filemenu
        help = QtGui.QAction("Help",self)
        help.setShortcut("Ctrl+H")
        help.setStatusTip('Help')
        help.triggered.connect(self.help_function)

        #create filemenu
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(loadImage)
        fileMenu.addAction(help)
        fileMenu.addAction(extractAction)

        self.matching_textbox = QTextEdit(self)
        self.matching_textbox.move(10,300)
        self.matching_textbox.resize(250,175)

        self.steps_input = QTextEdit(self)
        self.steps_input.move(360,300)

        '''layout = QtGui.QVBoxLayout()

        layout.addWidget(self.matching_textbox)
        layout.addWidget(self.steps_input)'''


        self.home()


    def quit_function(self):
        sys.exit()

    def help_function(self):
        self.matching_textbox.setText("Please read README.txt")

    def home(self):
        #quit button
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.quit_function)
        btn.resize(70 , 70)
        btn.move(640,150)

        #start button
        start_btn = QtGui.QPushButton('Start',self)
        start_btn.clicked.connect(self.start_function)
        start_btn.resize(70,70)
        start_btn.move(640,80)



        #retrain button
        retrain_btn = QtGui.QPushButton('Retrain', self)
        retrain_btn.clicked.connect(self.retraining_function)
        retrain_btn.resize(140, 70)
        retrain_btn.move(600, 400)


        #steps sign
        self.steps = QLabel("Steps:", self)
        self.steps.move(280, 300)
        steps_font = QFont("Open Sans", 15)
        self.steps.setFont(steps_font)


        self.show()


    def retraining_function(self):
        os.system('IMAGE_SIZE=224')
        os.system('ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"')
        cmd = 'cd tensorflow-for-poets-2 && python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps={0} \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"mobilenet_0.50_224" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="mobilenet_0.50_224" \
  --image_dir=tf_files/flower_photos'.format(self.input)
        flag = os.system(cmd)


    def start_function(self):


        cmd = "cd tensorflow-for-poets-2 && python -m scripts.label_image" \
              "     --graph=tf_files/retrained_graph.pb      --image={0} ".format(self.name)
        os.system(cmd +" > /home/ab/PycharmProjects/tensorflow_image_recognize/log.txt")
        self.matching_textbox.setText("Results:")

        file = open("log.txt", "r")
        for line in file:
            self.matching_textbox.append(line.rstrip())

    def button_function(self):
        print("")
        print(self.name)
        os.system('ls -l')
        input = self.steps_input.toPlainText()
        print(input)

    def load_image(self):
        self.name = QtGui.QFileDialog.getOpenFileName(self,'Load Image')
        #file = open(name,'r')
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(self.name))
        pic.resize(224,224)
        pic.move(10,50)

        pic.show()  # You were missing this.



def main():
    app = QtGui.QApplication(sys.argv)



    GUI = Window()
    app.exec_()

main()

