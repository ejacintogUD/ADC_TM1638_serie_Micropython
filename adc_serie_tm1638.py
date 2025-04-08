from machine import Pin, ADC
import time
from TM1638 import TM1638

# Define los pines que uses para el módulo TM1638
stb_pin = 8    # Pin de STB
clk_pin = 21   # Pin de CLK
dio_pin = 20   # Pin de DIO


#Crea una instancia del objeto TM1638
tm1638 = TM1638(stb_pin, clk_pin, dio_pin)

# Inicializa el display
tm1638.init()
print("Arranque del programa")


# Initialize ADC (analog pin for ESP32-C3)
adc = ADC(Pin(0))              # Connect analog input to GPIO 0
adc.width(ADC.WIDTH_12BIT)     # Set resolution to 12 bits
adc.atten(ADC.ATTN_11DB)       # Set input attenuation range to 0-3.3V

# Function to read voltage from ADC
def read_voltage():
    raw_adc_value = adc.read()         # Read raw ADC value (0-4095 for 12-bit)
    voltage = (raw_adc_value / 4095) * 3.3  # Scale the value to voltage (0-3.3V)
    return voltage

# Main loop to read ADC and display voltage
while True:
    voltage = read_voltage()           # Measure voltage
    voltage_str = f"{voltage:.4f}V"   # Format voltage with 4 decimal places
    print(f"Measured Voltage: {voltage_str}")  # Print to console (optional)
    
    tm1638.displayNumber(int((voltage)*10000))      # Display on TM1638 module
    
    time.sleep(0.5)                   # Update every 0.5 seconds