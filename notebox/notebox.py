from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from krita import *

class NoteboxDocker(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notebox")
        
        # Create main widget and layout
        self.mainWidget = QWidget(self)
        self.layout = QVBoxLayout(self.mainWidget)
        
        # Create and setup text editor
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("Type your notes here...")
        self.editor.textChanged.connect(self.save_text)
        self.layout.addWidget(self.editor)
        
        # Create autosave indicator
        self.indicator = QLabel("All changes saved")
        self.indicator.setStyleSheet("color: gray;")
        self.indicator.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.indicator)
        
        # Setup autosave timer
        self.save_timer = QTimer()
        self.save_timer.setInterval(1000)  # 1 second
        self.save_timer.timeout.connect(self.handle_autosave)
        self.save_timer.start()
        
        # Load saved text
        self.load_text()
        
        # Set the main widget
        self.setWidget(self.mainWidget)

    def load_text(self):
        """Load the saved text when plugin starts"""
        saved_text = Krita.instance().readSetting('notebox', 'text', '')
        self.editor.setPlainText(saved_text)
        
    def save_text(self):
        """Called when text changes"""
        self.indicator.setText("Saving...")
        self.indicator.setStyleSheet("color: orange;")
        # Use the timer to avoid saving too frequently
        self.save_timer.start()

    def handle_autosave(self):
        """Actually save the text after timer expires"""
        current_text = self.editor.toPlainText()
        Krita.instance().writeSetting('notebox', 'text', current_text)
        self.indicator.setText("All changes saved")
        self.indicator.setStyleSheet("color: gray;")
        self.save_timer.stop()
        
    def canvasChanged(self, canvas):
        """Required method from DockWidget, but we don't need to do anything here"""
        pass