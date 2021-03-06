import serial

class ArsinoDevice:
	
	def __init__(self, device):
		self.device = device
		self.serial = serial.Serial(device,9600)
		
	def query(self,q):
		self.serial.flushInput()
		self.serial.write(q)
		response=self.serial.readline()
		return response
		
	def set_digital_output_on(self, pin):
		self.query("D"+str(pin)+"e1e")
	
	def set_digital_output_off(self, pin):
		self.query("D"+str(pin)+"e0e")
		
	def digital_output_toggle(self,pin):
		current_state=self.get_digital_input(pin)
		if current_state == 0:
			self.set_digital_output_on(pin)
		else:
			self.set_digital_output_off(pin)
		
	def get_digital_input(self, pin):
		return int(self.query("d"+str(pin)+"e"))
	
	def get_analog_input(self, pin):
		return float(self.query("a"+str(pin)+"e"))
		
	def set_analog_output(self, pin, value):
		self.query("A"+str(pin)+"e"+str(value)+"e")
		
	def set_pin_to_input_mode(self, pin):
		self.query("i"+str(pin)+"e")
		
	def set_pin_to_output_mode(self, pin):
		self.query("o"+str(pin)+"e")
		
	def get_analog_pin(self, pin):
		return AnalogPin(self, pin)
		
	def get_digital_pin(self, pin):
		return DigitalPin(self, pin)
		
class ArsinoPin():
	def __init__(self, device, pin):
		self.device=device
		self.pin=pin
		
class AnalogPin(ArsinoPin):
	def get_voltage(self):
		return self.device.get_analog_input(self.pin)
		
class DigitalPin(ArsinoPin):
	def turn_on(self):
		self.device.set_digital_output_on(self.pin)
		
	def turn_off(self):
		self.device.set_digital_output_off(self.pin)
		
	def toggle(self):
		self.device.digital_output_toggle(self.pin)
		
	
		
		
		
		
