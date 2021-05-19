class Simplex(object):
	def __init__(self, tableauSimplex):
		self.tableauSimplex = tableauSimplex
		self.nombreDeVariables = len(tableauSimplex[0])
		self.simplexInverse = [[row[i] for row in tableauSimplex] for i in range(self.nombreDeVariables)]
		self.valeursRHS = self.simplexInverse[-1]
		self.puissance = 10**10 ### 10 puissance 10 : a modifier si besoin

	def rechercheVariableEntrante(self):
		variableEntrante = min(self.tableauSimplex[0])
		colomnePivot = self.tableauSimplex[0].index(variableEntrante)
		print ("Tableau apres pivotement :", colomnePivot)
		return colomnePivot

	def ratioTest(self, colomnePivot):
		listeRatio = [float(x[0])/x[1] if x[1] > 0 else self.puissance for x in zip(self.valeursRHS, self.tableauSimplex[colomnePivot])]
		lignePivot = listeRatio.index(min(listeRatio))
		print ("listeRatio:", listeRatio)
		print ("lignePivot:", lignePivot)
		return lignePivot

	def creerVariableSortante(self, lignePivot, colomnePivot):
		a = self.tableauSimplex[lignePivot][colomnePivot]
		lignePivotante = [(1.0/a) * i for i in self.tableauSimplex[lignePivot]]
		self.tableauSimplex.remove(self.tableauSimplex[lignePivot])
		nouveauTableauSimplex = list()
		for row in self.tableauSimplex:
			a = row[colomnePivot] * -1
			nouvelleLigne = [i[0] + i[1]*a for i in zip(row, lignePivotante)]
			nouveauTableauSimplex.append(nouvelleLigne)
		nouveauTableauSimplex.insert(lignePivot, lignePivotante)
		self.tableauSimplex = nouveauTableauSimplex
		self.simplexInverse = [[row[i] for row in self.tableauSimplex] for i in range(self.nombreDeVariables)]
		self.valeursRHS = self.simplexInverse[-1]
		print
		for row in nouveauTableauSimplex:
			print (row)		

	def verifierOptimisation(self):
		if min(self.tableauSimplex[0]) >= 0:
			return True
		else:
			return False

	def conditionArret(self):
		print ("Tableau initial \n")
		for row in self.tableauSimplex:
			print (row)
		print
		print ("\n\n")
		while not self.verifierOptimisation():
			column = self.rechercheVariableEntrante()
			row = self.ratioTest(column)
			self.creerVariableSortante(row, column)
			print ("\n ====================================== \n")

if __name__ == "__main__":

	tableau = [[1, -3, -2, 0, 0, 0, 0],
			   [0, 2, 1, 1, 0, 0, 100],
			   [0, 1, 1, 0, 1, 0, 80],
			   [0, 1, 0, 0, 0, 1, 40]]

	a = Simplex(tableau)
	a.conditionArret()
