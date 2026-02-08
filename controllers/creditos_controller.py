from PySide6.QtWidgets import QWidget
from views.ui.creditos_ui import Ui_Form


class CreditosController:
    def __init__(self, parent_controller=None):
        self.parent_controller = parent_controller
        self.widget = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.widget)
        
        # Configurar el texto de créditos si existe textEdit
        if hasattr(self.ui, 'textEdit'):
            self.configurar_creditos()
    
    def configurar_creditos(self):
        """Configura el contenido de los créditos"""
        creditos_html = """
        <!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body { 
                    font-family: 'Segoe UI', Arial, sans-serif;
                    color: #1B5A5A;
                }
                h1 { 
                    color: #267E7E;
                    text-align: center;
                    font-size: 24pt;
                    margin-bottom: 20px;
                }
                h2 { 
                    color: #FF9501;
                    font-size: 16pt;
                    margin-top: 15px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 12pt;
                    margin: 5px 0;
                    color: #FFFFFF;
                }
                .center {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>⚽ Torneo de Fútbol ⚽</h1>
            
            <h2>📋 Acerca de la Aplicación</h2>
            <p>Sistema de gestión de torneos de fútbol desarrollado para organizar y administrar competiciones deportivas.</p>
            <p>Permite el registro de equipos, participantes, gestión de partidos, calendario y estadísticas.</p>
            
            <h2>👨‍💻 Desarrollador</h2>
            <p><strong>Nombre:</strong>Boris Baldominos Gonzalez</p>
            <p><strong>Curso:</strong> DAM 2 - 2º 25-26</p>
            <p><strong>Módulo:</strong> Desarrollo de Interfaces (DI)</p>
            
            <h2>🛠️ Tecnologías Utilizadas</h2>
            <p>• <strong>Python:</strong> Lenguaje de programación</p>
            <p>• <strong>PySide6 (Qt):</strong> Framework de interfaz gráfica</p>
            <p>• <strong>MySQL:</strong> Base de datos</p>
            <p>• <strong>MVC:</strong> Patrón de arquitectura</p>
            
            <h2>📅 Versión</h2>
            <p><strong>Versión:</strong> 1.0</p>
            <p><strong>Fecha:</strong> Febrero 2026</p>
            
            <p class="center" style="margin-top: 30px;">
                <strong>Gracias por usar esta aplicación</strong>
            </p>
        </body>
        </html>
        """
        self.ui.textEdit.setHtml(creditos_html)
        self.ui.textEdit.setReadOnly(True)
    
    def mostrar(self):
        """Muestra la ventana de créditos"""
        self.widget.show()
    
    def ocultar(self):
        """Oculta la ventana de créditos"""
        self.widget.hide()
