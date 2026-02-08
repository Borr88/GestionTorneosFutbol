from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QPushButton, QHBoxLayout, QMessageBox
from PySide6.QtCore import QUrl
import os
import sys
import subprocess
import platform
from pathlib import Path


class GuiaController:
    def __init__(self, parent_controller=None):
        self.parent_controller = parent_controller
        self.widget = QWidget()
        
        # Crear layout principal
        main_layout = QVBoxLayout(self.widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Crear botón para abrir PDF
        button_layout = QHBoxLayout()
        self.btn_abrir_pdf = QPushButton("📄 Abrir Manual en PDF")
        self.btn_abrir_pdf.setStyleSheet("""
            QPushButton {
                font-size: 12pt;
                font-weight: bold;
                color: #267E7E;
                background-color: #FF9501;
                border-radius: 10px;
                border: 2px solid #A35F00;
                padding: 10px 20px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #FFA520;
            }
            QPushButton:pressed {
                background-color: #E88500;
            }
        """)
        self.btn_abrir_pdf.clicked.connect(self.abrir_pdf)
        button_layout.addStretch()
        button_layout.addWidget(self.btn_abrir_pdf)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        
        # Crear QTextBrowser para mostrar el HTML
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(False)
        self.text_browser.setStyleSheet("""
            QTextBrowser {
                background-color: rgb(27, 90, 90);
                border: none;
                color: rgb(255, 255, 255);
            }
        """)
        
        # Establecer stylesheet por defecto para el documento
        self.text_browser.document().setDefaultStyleSheet("""
            body { 
                background-color: rgb(27, 90, 90); 
                color: rgb(255, 255, 255); 
            }
            h1, h2, h3 { 
                color: rgb(255, 149, 1); 
            }
            p, li, ul, ol { 
                color: rgb(255, 255, 255); 
            }
        """)
        
        main_layout.addWidget(self.text_browser)
        
        # Cargar el HTML
        self.cargar_manual()
    
    def cargar_manual(self):
        """Carga el archivo HTML del manual"""
        try:
            # Determinar la ruta base (funciona tanto en desarrollo como en ejecutable)
            if getattr(sys, 'frozen', False):
                # Si está ejecutándose como ejecutable de PyInstaller
                base_dir = Path(sys._MEIPASS)
            else:
                # Si está ejecutándose como script normal
                base_dir = Path(__file__).resolve().parent.parent
            
            html_path = base_dir / 'documentacion' / 'manual.html'
            
            if html_path.exists():
                # Cargar el archivo HTML
                with open(html_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                self.text_browser.setHtml(html_content)
            else:
                self.text_browser.setHtml("""
                    <html>
                    <body style='background-color: #5ecfcf; color: white; font-family: Arial; padding: 20px;'>
                        <h1 style='color: #ff9501;'>Error</h1>
                        <p>No se pudo encontrar el archivo del manual.</p>
                        <p>Ruta esperada: {}</p>
                    </body>
                    </html>
                """.format(html_path))
        except Exception as e:
            self.text_browser.setHtml("""
                <html>
                <body style='background-color: #5ecfcf; color: white; font-family: Arial; padding: 20px;'>
                    <h1 style='color: #ff9501;'>Error</h1>
                    <p>Error al cargar el manual: {}</p>
                </body>
                </html>
            """.format(str(e)))
    
    def abrir_pdf(self):
        """Abre el PDF del manual con la aplicación predeterminada"""
        try:
            # Determinar la ruta base (funciona tanto en desarrollo como en ejecutable)
            if getattr(sys, 'frozen', False):
                # Si está ejecutándose como ejecutable de PyInstaller
                base_dir = Path(sys._MEIPASS)
            else:
                # Si está ejecutándose como script normal
                base_dir = Path(__file__).resolve().parent.parent
            
            pdf_path = base_dir / 'documentacion' / 'Manual de uso de aplicación.pdf'
            
            if not pdf_path.exists():
                QMessageBox.warning(
                    self.widget,
                    "Archivo no encontrado",
                    f"No se encontró el archivo PDF en:\n{pdf_path}"
                )
                return
            
            # Abrir el PDF con la aplicación predeterminada según el sistema operativo
            sistema = platform.system()
            
            if sistema == 'Windows':
                os.startfile(str(pdf_path))
            elif sistema == 'Darwin':  # macOS
                subprocess.run(['open', str(pdf_path)])
            else:  # Linux y otros
                subprocess.run(['xdg-open', str(pdf_path)])
                
        except Exception as e:
            QMessageBox.critical(
                self.widget,
                "Error",
                f"No se pudo abrir el archivo PDF:\n{str(e)}"
            )
    
    def mostrar(self):
        """Muestra la ventana de guía"""
        self.widget.show()
    
    def ocultar(self):
        """Oculta la ventana de guía"""
        self.widget.hide()
