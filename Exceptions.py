class CompleteLevel(Exception):
	def __init__(self):
		self.nome = "Fase Concluida"
	def __str__(self):
		return repr(self.nome)
