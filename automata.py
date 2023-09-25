import unittest
def AutomataFinito(cadena):
    estados = {'q1', 'q2', 'q3'}
    estado_inicial = 'q1'
    estado_final = 'q3'
    alfabeto = {'0', '1'}
    transiciones = {
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q1', '1': 'q3'},
        'q3': {'0': 'q2', '1': 'q1'}
    }
    estado_actual = estado_inicial
    for simbolo in cadena:
        if simbolo not in alfabeto:
            return False 
        estado_actual = transiciones[estado_actual][simbolo]
    return estado_actual in estado_final



class TestAutomataFinito(unittest.TestCase):
    
    def test_accepts_valid_string(self):
        self.assertTrue(AutomataFinito('1'))  
    
    def test_rejects_invalid_string(self):
        self.assertFalse(AutomataFinito('11'))  
    
    def test_rejects_string_with_invalid_symbols(self):
        self.assertFalse(AutomataFinito('12'))  
    
    def test_accepts_empty_string(self):
        self.assertFalse(AutomataFinito('')) 
    
    def test_accepts_string_with_zeros_only(self):
        self.assertFalse(AutomataFinito('00'))  
    
    def test_accepts_string_with_ones_only(self):
        self.assertFalse(AutomataFinito('11')) 

if __name__ == '__main__':
    unittest.main()
