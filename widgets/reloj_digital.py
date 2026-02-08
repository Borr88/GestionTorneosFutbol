import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QTimer, Property, Signal, QTime, Slot
from PySide6.QtGui import QFont, QFontMetrics
from enum import Enum

# Importamos la interfaz convertida
from widgets.ui_reloj import Ui_Form

# 1. Definición del Enum para el modo
class ClockMode(Enum):
    CLOCK = 0
    TIMER = 1

class RelojDigital(QWidget):
    # Señales (Eventos públicos)
    alarmTriggered = Signal() 
    timerFinished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Configuración de la Interfaz desde el archivo Python generado
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Ajustar proporciones del layout: dar más espacio al label de mensajes
        self.ui.verticalLayout.setStretch(0, 3)  # Label de mensajes (índice 0) - 3 partes
        self.ui.verticalLayout.setStretch(1, 7)  # LCD (índice 1) - 7 partes
        
        # --- VARIABLES INTERNAS ---
        self._mode = ClockMode.CLOCK
        self._is_24h = True
        
        # Variables de Alarma
        self._alarm_active = False 
        self._alarm_time = QTime(0, 0) 
        self._alarm_message = self.tr("ALARMA")
        self._alarm_triggered_flag = False 

        # Variables de Temporizador / Cronómetro
        self._timer_duration = 60  # Duración por defecto (segundos)
        self._current_time_val = 0 # Valor actual del contador
        self._timer_running = False 
        self._is_countdown = False # False = Cronómetro, True = Cuenta atrás

        # Timer interno (Tick de 1 segundo)
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_display)
        self._timer.start(1000)

        # Refrescamos la pantalla inicial
        self._update_display()
        
        # Ajustar fuente inicial del label
        self._ajustar_fuente_label()

    # ==========================================
    #           PROPIEDADES (GETTERS/SETTERS)
    # ==========================================

    # --- MODO (Reloj vs Timer) ---
    def get_mode(self): 
        return self._mode.value
    
    def set_mode(self, mode):
        if isinstance(mode, int):
            mode = ClockMode(mode)
        self._mode = mode
        self.ui.lbl_message.setText("") # Limpiar mensaje al cambiar modo
        self._update_display()          # Refrescar visualización
        self._ajustar_fuente_label()    # Ajustar fuente
    
    mode = Property(int, get_mode, set_mode)

    # --- FORMATO 24H ---
    def get_format24(self): return self._is_24h
    def set_format24(self, value): self._is_24h = value
    format24 = Property(bool, get_format24, set_format24)

    # --- ALARMA: ACTIVA ---
    def get_alarm_active(self): return self._alarm_active
    def set_alarm_active(self, active): self._alarm_active = active
    alarmActive = Property(bool, get_alarm_active, set_alarm_active)

    # --- ALARMA: MENSAJE ---
    def get_alarm_message(self): return self._alarm_message
    def set_alarm_message(self, message): self._alarm_message = message
    alarmMessage = Property(str, get_alarm_message, set_alarm_message)

    # --- ALARMA: HORA Y MINUTO ---
    def set_alarm_hour(self, h): 
        self._alarm_time.setHMS(h, self._alarm_time.minute(), 0)
        
    def set_alarm_minute(self, m): 
        self._alarm_time.setHMS(self._alarm_time.hour(), m, 0)

    # --- TIMER: DURACIÓN ---
    def get_timer_duration(self): return self._timer_duration
    def set_timer_duration(self, seconds): 
        self._timer_duration = int(seconds)
        if not self._timer_running:
            self.reset_timer() 
    timerDuration = Property(int, get_timer_duration, set_timer_duration)

    # --- TIMER: TIPO (CUENTA ATRÁS O NO) ---
    def get_is_countdown(self): return self._is_countdown
    def set_is_countdown(self, is_down):
        self._is_countdown = is_down
        self.reset_timer()
    isCountdown = Property(bool, get_is_countdown, set_is_countdown)


    # ==========================================
    #           MÉTODOS DE CONTROL (SLOTS)
    # ==========================================

    @Slot()
    def start_timer(self):
        self._timer_running = True
        if self._mode != ClockMode.TIMER:
            self.set_mode(ClockMode.TIMER)

    @Slot()
    def pause_timer(self):
        self._timer_running = False

    @Slot()
    def reset_timer(self):
        self._timer_running = False
        self.ui.lbl_message.setText("")
        if self._is_countdown:
            self._current_time_val = self._timer_duration
        else:
            self._current_time_val = 0
        self._update_display()
        self._ajustar_fuente_label()


    # ==========================================
    #           LÓGICA INTERNA (CORE)
    # ==========================================

    def _update_display(self):
        """Se ejecuta cada segundo"""
        
        # --- MODO RELOJ ---
        if self._mode == ClockMode.CLOCK:
            current_time = QTime.currentTime()
            format_str = "HH:mm:ss" if self._is_24h else "hh:mm:ss"
            self.ui.lcd_time.display(current_time.toString(format_str))

            # Comprobar Alarma
            if self._alarm_active and not self._alarm_triggered_flag:
                if (current_time.hour() == self._alarm_time.hour() and 
                    current_time.minute() == self._alarm_time.minute()):
                    self._trigger_alarm()

        # --- MODO TIMER ---
        elif self._mode == ClockMode.TIMER:
            if self._timer_running:
                if self._is_countdown:
                    # Restar
                    if self._current_time_val > 0:
                        self._current_time_val -= 1
                    else:
                        self._finish_timer()
                else:
                    # Sumar
                    if self._current_time_val < self._timer_duration:
                        self._current_time_val += 1
                    else:
                        self._finish_timer()

            # Mostrar MM:SS
            mins = self._current_time_val // 60
            secs = self._current_time_val % 60
            self.ui.lcd_time.display(f"{mins:02}:{secs:02}")

    def _trigger_alarm(self):
        self._alarm_triggered_flag = True
        self.ui.lbl_message.setText(self._alarm_message)
        self._ajustar_fuente_label()
        self.alarmTriggered.emit()
        # Resetear flag tras 60s
        QTimer.singleShot(60000, lambda: setattr(self, '_alarm_triggered_flag', False))

    def _finish_timer(self):
        self._timer_running = False
        self.ui.lbl_message.setText(self._alarm_message) # Mensaje de fin
        self._ajustar_fuente_label()
        self.timerFinished.emit()


    def resizeEvent(self, event):
        """Se ejecuta cuando el widget cambia de tamaño"""
        super().resizeEvent(event)
        self._ajustar_fuente_label()
    
    def _ajustar_fuente_label(self):
        """Ajusta el tamaño de la fuente del label para que se adapte al espacio disponible"""
        if not self.ui.lbl_message.text():
            return
        
        # Obtener el tamaño disponible del label
        label_width = self.ui.lbl_message.width() - 10  # Restar padding mínimo
        label_height = self.ui.lbl_message.height() - 5
        
        if label_width <= 0 or label_height <= 0:
            return
        
        # Comenzar con un tamaño de fuente grande (90% del alto del label) y reducir hasta que quepa
        font = QFont(self.ui.lbl_message.font())
        font_size = int(label_height * 0.9)  # Usar el 90% del alto del label como máximo
        
        for size in range(font_size, 8, -1):
            font.setPointSize(size)
            font.setBold(True)
            metrics = QFontMetrics(font)
            text_width = metrics.horizontalAdvance(self.ui.lbl_message.text())
            text_height = metrics.height()
            
            if text_width <= label_width and text_height <= label_height:
                self.ui.lbl_message.setFont(font)
                break

    def changeEvent(self, event):
        """Detecta si se cambia el idioma de la aplicación mientras está abierta"""
        if event.type() == event.Type.LanguageChange:
            # Aquí se refrescarían textos estáticos si los hubiera
            pass
        super().changeEvent(event)

# ==========================================
#           BLOQUE DE PRUEBAS (ENTREGABLE INDIVIDUAL)
# ==========================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RelojDigital()
    
    # 1. Establecemos un tamaño inicial decente para que no se vea pequeño
    window.resize(500, 250)
    
    window.show()

    # --- PRUEBAS ---
    # Por defecto inicia en modo RELOJ. 
    # Si quieres probar el TEMPORIZADOR, descomenta las líneas de abajo:

   
    print("Iniciando prueba de cronómetro...")
    window.set_mode(ClockMode.TIMER)   
    window.set_is_countdown(False)     
    window.set_timer_duration(5)
    window.set_alarm_message("¡TIEMPO!") 
    window.start_timer()
    window.timerFinished.connect(lambda: print("¡SEÑAL RECIBIDA: FIN DEL TIEMPO!"))


    sys.exit(app.exec())