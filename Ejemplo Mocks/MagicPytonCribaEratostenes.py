#
# Tenemos mocks a partir de la 3.3
#
import unittest
from unittest.mock import MagicMock

class CribaEratostenes:
	def calcula(self, val):
		#lb = None
		lb =  self.creaListaDeNumerosSinMarcar(val)
		self.marcarMultiplos(lb)
		return self.creaListaDePrimos(lb)
		#return lb
	#def creaListaDeNumerosSinMarcar(self, val):
	#	pass
	#def marcarMultiplos(self, lb):
	#	pass
	#def creaListaDePrimos(self, lb):
	#	pass


class TestBase(unittest.TestCase):

	def test_richtSequenceOfCalls(self):
		criba = CribaEratostenes()

		criba.creaListaDeNumerosSinMarcar = MagicMock(return_value=None)
		criba.marcarMultiplos = MagicMock() 
		criba.creaListaDePrimos = MagicMock()

		criba.calcula(5)

		criba.creaListaDeNumerosSinMarcar.assert_called_once_with(5)
		criba.marcarMultiplos.assert_called_once_with(None)
		criba.creaListaDePrimos.assert_called_once_with(None)

# Si ponemos in metodo assert_called_one() no funciona
# igual me estoy inventando el metodo y el mock se lo traga

# Main
if __name__ == '__main__':
    unittest.main()

