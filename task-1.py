class Data:
	def __init__(self, data: str):
		self.data = data

	@classmethod
	def transform_data(cls, data):
		day, month, year = map(int, data.split('-'))

		return {'day': day, 'month': month, 'year': year}

	@staticmethod
	def is_valid(data: str):
		day, month, year = map(int, data.split('-'))

		return 1 <= day <= 31 and 1 <= month <= 12 and 1960 <= year


print(Data.transform_data('31-12-1960'))
print(Data.is_valid('31-12-1960'))
