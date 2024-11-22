import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QTextEdit, QCheckBox, QSpinBox, QGroupBox, QScrollArea
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDateTime


class ApiKeyGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("API Key Generator")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black; color: white;")
        

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self.add_generator_section(left_layout)
        main_layout.addLayout(left_layout, 3)

        right_layout = QVBoxLayout()
        self.add_sidebar(right_layout)
        main_layout.addLayout(right_layout, 1)

        # Bottom Section (Logs)
        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.logs.setStyleSheet("background-color: black; color: green;")
        self.logs.setFont(QFont("Courier", 10))
        self.logs.append("Logs will appear here.")
        main_layout.addWidget(self.logs, 1)

        self.setLayout(main_layout)

    def add_generator_section(self, layout):
        title = QLabel("API Key Generator")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white;")
        layout.addWidget(title)


        filters_group = QGroupBox("API Key Filters")
        filters_layout = QVBoxLayout()

        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(8, 64)
        self.length_spinbox.setValue(32)
        self.length_spinbox.setStyleSheet("color: white;")
        filters_layout.addWidget(QLabel("Key Length:"))
        filters_layout.addWidget(self.length_spinbox)

        self.include_numbers = QCheckBox("Include Numbers")
        self.include_numbers.setChecked(True)
        filters_layout.addWidget(self.include_numbers)

        self.include_uppercase = QCheckBox("Include Uppercase Letters")
        self.include_uppercase.setChecked(True)
        filters_layout.addWidget(self.include_uppercase)

        self.include_lowercase = QCheckBox("Include Lowercase Letters")
        self.include_lowercase.setChecked(True)
        filters_layout.addWidget(self.include_lowercase)

        self.include_special = QCheckBox("Include Special Characters")
        self.include_special.setChecked(True)
        filters_layout.addWidget(self.include_special)

        filters_group.setLayout(filters_layout)
        layout.addWidget(filters_group)


        generate_button = QPushButton("Generate API Key")
        generate_button.clicked.connect(self.generate_api_key)
        generate_button.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        layout.addWidget(generate_button)

        self.generated_key = QLineEdit()
        self.generated_key.setReadOnly(True)
        self.generated_key.setStyleSheet("color: white; background-color: #333;")
        layout.addWidget(self.generated_key)

        copy_button = QPushButton("Copy Key")
        copy_button.clicked.connect(self.copy_key)
        layout.addWidget(copy_button)

    def add_sidebar(self, layout):
        details = QVBoxLayout()

        meta_data = [
            ("Developed on:", QDateTime.currentDateTime().toString("dd MMM yyyy")),
            ("Last Updated:", "20 Nov 2024"),
            ("Version:", "1.1"),
            ("Developed by:", "Mayank Chawdhari"),
            ("Special Thanks to:", "PyQt Community")
        ]
        
        for key, value in meta_data:
            lbl = QLabel(f"{key} {value}")
            lbl.setStyleSheet("color: white; font-size: 14px;")
            details.addWidget(lbl)

        how_to = QLabel("How to use:\n1. Select filters.\n2. Click Generate.\n3. Copy the key.")
        how_to.setWordWrap(True)
        how_to.setStyleSheet("color: white;")
        details.addWidget(how_to)

        layout.addLayout(details)

    def generate_api_key(self):
        length = self.length_spinbox.value()
        include_numbers = self.include_numbers.isChecked()
        include_uppercase = self.include_uppercase.isChecked()
        include_lowercase = self.include_lowercase.isChecked()
        include_special = self.include_special.isChecked()

        characters = ""
        if include_numbers:
            characters += string.digits
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_special:
            characters += "!@#$%^&*()_+"

        if not characters:
            self.logs.append("Error: No filters selected!")
            return

        api_key = ''.join(random.choices(characters, k=length))
        self.generated_key.setText(api_key)
        self.logs.append(f"API Key Generated: {api_key}")

    def copy_key(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.generated_key.text())
        self.logs.append("API Key copied to clipboard.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApiKeyGenerator()
    window.show()
    sys.exit(app.exec_())

