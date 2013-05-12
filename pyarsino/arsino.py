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
		
	def digital_on(self, pin):
		self.query("D"+str(pin)+"e1e")
	
	def digital_off(self, pin):
		self.query("D"+str(pin)+"e0e")
		
	def get_digital(self, pin):
		return int(self.query("d"+str(pin)+"e"))
	
	def get_analog(self, pin):
		return float(self.query("a"+str(pin)+"e"))
		
	def set_analog(self, pin, value):
		self.query("A"+str(pin)+"e"+str(value)+"e")
