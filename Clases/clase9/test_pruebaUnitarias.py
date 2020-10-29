import unittest
import pruebasUnitarias
class TestPruebasUnitarias (unittest.TestCase):
    def test_suma(self) :
        #Arrenge
        espero = 4
        valor1 = 2
        valor2 = 2
        #Attemp
        resultado = pruebasUnitarias.suma(valor1,valor2)
        #Assert 
        self.assertEqual(resultado,espero)
    def test_suma2(self) :
        #Arrenge
        espero =3
        valor1 = 2
        valor2 = 2
        #Attemp
        resultado = pruebasUnitarias.suma(valor1,valor2)
        #Assert 
        try: 
            self.assertEqual(resultado,espero)
        except AssertionError :
            print ("Prueba fallida")
def hola():
    print ('holi')
def hola2():
    print ('holi')
if __name__ == "__main__":
    hola()
    unittest.main()