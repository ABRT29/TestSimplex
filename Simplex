class Simplex(object):
	def __init__(self, simplexTableau):
		self.simplexTableau = simplexTableau
		self.numberOfVariables = len(simplexTableau[0])
		self.invertedSimplex = [[row[i] for row in simplexTableau] for i in range(self.numberOfVariables)]
		self.rhsValues = self.invertedSimplex[-1]
		self.bigM = 10**10 ### Should be changed if you're actually dealing with numbers like this

	def findEnteringVariable(self):
		enteringVariable = min(self.simplexTableau[0])
		pivotColumn = self.simplexTableau[0].index(enteringVariable)
		print "Pivot Column:", pivotColumn
		return pivotColumn

	def ratioTest(self, pivotColumn):
		ratioList = [float(x[0])/x[1] if x[1] > 0 else self.bigM for x in zip(self.rhsValues, self.invertedSimplex[pivotColumn])]
		pivotRow = ratioList.index(min(ratioList))
		print "Ratio List:", ratioList
		print "Pivot Row:", pivotRow
		return pivotRow

	def makeBasicVariable(self, pivotRow, pivotColumn):
		a = self.simplexTableau[pivotRow][pivotColumn]
		pivotingRow = [(1.0/a) * i for i in self.simplexTableau[pivotRow]]
		self.simplexTableau.remove(self.simplexTableau[pivotRow])
		newSimplexTableau = list()
		for row in self.simplexTableau:
			a = row[pivotColumn] * -1
			newRow = [i[0] + i[1]*a for i in zip(row, pivotingRow)]
			newSimplexTableau.append(newRow)
		newSimplexTableau.insert(pivotRow, pivotingRow)
		self.simplexTableau = newSimplexTableau
		self.invertedSimplex = [[row[i] for row in self.simplexTableau] for i in range(self.numberOfVariables)]
		self.rhsValues = self.invertedSimplex[-1]
		print
		for row in newSimplexTableau:
			print row		

	def checkOptimal(self):
		if min(self.simplexTableau[0]) >= 0:
			return True
		else:
			return False

	def solve(self):
		print "Initial Tableau\n" + "-" * 20
		for row in self.simplexTableau:
			print row
		print
		while not self.checkOptimal():
			column = self.findEnteringVariable()
			row = self.ratioTest(column)
			self.makeBasicVariable(row, column)
			print "\n\n"

if __name__ == "__main__":

	tableau = [[1, -3, -2, 0, 0, 0, 0],
			   [0, 2, 1, 1, 0, 0, 100],
			   [0, 1, 1, 0, 1, 0, 80],
			   [0, 1, 0, 0, 0, 1, 40]]

	a = Simplex(tableau)
	a.solve()

	tableau = [[1, -60, -35, -20, 0, 0, 0, 0, 0],
			   [0, 8, 6, 1, 1, 0, 0, 0, 48],
			   [0, 4, 2, 1.5, 0, 1, 0, 0, 20],
			   [0, 2, 1.5, 0.5, 0, 0, 1, 0, 8],
			   [0, 0, 1, 0, 0, 0, 0, 1, 5]]

	b = Simplex(tableau)
	b.solve()
