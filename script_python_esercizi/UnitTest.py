import unittest
from unittest.mock import patch
""" 
def somma_token(a,b):
    return a + b

class TestMioCodice(unittest.TestCase):
    def test_somma_token(self):
        risultato = somma_token(10,20)
        self.assertEqual(risultato, 30)
if __name__ == '__main__':
    unittest.main()
"""

def calcola_sconto(prezzo, percentuale):
    if percentuale > 100:
        raise ValueError("La percentuale non può essere maggiore di 100%")
    prezzo_finale = prezzo - (prezzo * (percentuale / 100))
    return prezzo_finale

class TestSistemiIA(unittest.TestCase):
    def test_calcola_sconto(self):
        risultato = calcola_sconto(100, 5)
        self.assertEqual(risultato , 95)
    
    def test_sconto_eccessivo_lancia_errore(self):
        with self.assertRaises(ValueError):
            calcola_sconto(100, 150)

def invia_prompt_a_chatgpt(prompt):
    pass

class TestIntegrazioneIA(unittest.TestCase):
    @patch('__main__.invia_prompt_a_chatgpt')
    def test_chiamata_ia_finta(self, finta_funzione):
        finta_funzione.return_value = "Ciao! Sono un finto ChatGPT!"
        risultato = invia_prompt_a_chatgpt("Ciao")
        self.assertEqual(risultato, "Ciao! Sono un finto ChatGPT!")
        finta_funzione.assert_called_once_with("Ciao")

def recupera_saldo_banca(id_utente):
    pass

class TestServerBancario(unittest.TestCase):
    @patch('__main__.recupera_saldo_banca')
    def test_recupera_saldo_banca(self, mock_banca):
        mock_banca.return_value = 500

        saldo = recupera_saldo_banca(1)
        self.assertEqual(saldo, 500)

if __name__ == '__main__':
    unittest.main()