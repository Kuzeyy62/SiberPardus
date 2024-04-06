import sys
import subprocess
import os
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
except:
    os.system("apt install python3-pyqt5")
    print("Yeniden Baslat")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CyberParDus")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_buttons()

    def create_buttons(self):
        programs = [
            ("Metasploit", "sudo apt-get install metasploit-framework -y"),
            ("Bettercap", "sudo apt-get install bettercap -y"),
            ("Airgeddon", "sudo apt-get install airgeddon -y"),
            ("Nmap", "sudo apt-get install nmap -y"),
            ("Sqlmap", "sudo apt-get install sqlmap -y"),
            ("Hydra", "sudo apt-get install hydra -y"),
            ("Wireshark", "sudo apt-get install wireshark -y"),
            ("Nessus", "sudo apt-get install nessus -y")
        ]

        for program_name, program_command in programs:
            button = QPushButton(program_name)
            button.clicked.connect(lambda _, cmd=program_command: self.install_and_run(cmd, program_name))
            self.layout.addWidget(button)

        slowloris_button = QPushButton("Slowloris")
        slowloris_button.clicked.connect(self.install_and_run_slowloris)
        self.layout.addWidget(slowloris_button)

    def install_and_run(self, program_command, program_name):
        try:
            subprocess.run(program_command.split())
            subprocess.Popen([program_name.lower()])
        except Exception as e:
            print("Hata:", e)

    def install_and_run_slowloris(self):
        try:
            os.chdir(os.path.expanduser("~/Desktop"))
            subprocess.run(["git", "clone", "https://github.com/gkbrk/slowloris.git"])

            os.chdir("slowloris")
            subprocess.Popen(["python3", "slowloris.py"])
        except Exception as e:
            print("Hata:", e)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
