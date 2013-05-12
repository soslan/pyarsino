class ArsinoDevice:
	
	def __init__(self, device):
		self.device=device
		
	def query(q):
		return "making query"
		
	def digital_on(self, pin):
		self.query("D"+str(pin)+"e1e")
	
	def digital_off(self, pin):
		self.query("D"+str(pin)+"e0e")
		
	def get_digital(self, pin):
		return self.query("d"+str(pin)+"e")
	
	def get_analog(self, pin):
		return self.query("a"+str(pin)+"e")
		
	def set_analog(self, pin, value):
		self.query("A"+str(pin)+"e"+str(value)+"e")
