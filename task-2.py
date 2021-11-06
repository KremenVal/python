class Road:
	_length = 0
	_width = 0
	mass_asphalt = 25
	blade_thickness = 5

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def mass_of_asphalt(self):
		return self.length * self.width * self.mass_asphalt * self.blade_thickness / 1000


new_road = Road(20, 5000)
print(new_road.mass_of_asphalt())
