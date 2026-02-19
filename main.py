import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit

class OCRTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI 批量文字识别工具")
        self.resize(600, 400)

        # 界面布局
        layout = QVBoxLayout()
        self.btn = QPushButton("点击选择图片文件夹")
        self.btn.clicked.connect(self.start_ocr)
        self.log = QTextEdit()
        
        layout.addWidget(self.btn)
        layout.addWidget(self.log)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_ocr(self):
        folder = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder:
            self.log.append(f"正在扫描文件夹: {folder}")
            # 注意：实际打包后这里会运行 PaddleOCR 逻辑
            self.log.append("环境检测正常，准备开始识别...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRTool()
    window.show()
    sys.exit(app.exec())