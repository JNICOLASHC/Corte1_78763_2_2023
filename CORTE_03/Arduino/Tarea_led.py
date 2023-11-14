import serial,time

# Configura el puerto serial
arduino = serial.Serial('COM8', 9600)  # Reemplaza 'COM3' con el puerto serial correspondiente

# Hace que el LED titile cada segundo
while True:
    arduino.write(b'H')  # Enciende el LED
    time.sleep(1)
    arduino.write(b'L')  # Apaga el LED
    time.sleep(1)