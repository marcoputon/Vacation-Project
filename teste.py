#! /usr/bin/python




def loadLevels(arquivo):
	levels = []
	level = []
	arquivo = open(arquivo, "r")
	fases = arquivo.readlines()
	f = False
	nome = ""
	for i in fases:
		if "nome" in i:
			print(i[6:len(i)-1])
			nome = i[6:len(i)-1]
			f = True
			continue
		
		if	f:
			i = i[0:len(i)-1]
			if i != "":
				level.append(i)
			else:
				levels.append([level, nome])
				level = []
				f = False
	levels.append([level, nome])
	return levels


fases = loadLevels("fase1.txt")
for i in fases:
	for j in i[0]:
		print(j)

