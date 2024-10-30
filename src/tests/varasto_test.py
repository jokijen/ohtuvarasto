import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    # UUSI
    def test_palautetaan_oikea_merkkijonoesitys(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    
    # UUSI
    def test_uudella_varastolla_ei_negatiivista_alkusaldoa(self):
        varasto = Varasto(10, -1)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    # UUSI
    def test_uudella_varastolla_ei_negatiivista_tilavuutta(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    # UUSI
    def test_ei_voi_lisata_varastoon_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    # UUSI
    def test_ei_voi_lisata_varastoon_tilavuutta_isompaa_maaraa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    # UUSI
    def test_ei_voi_ottaa_negatiivista_maaraa_varastosta(self):
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0.0)

    # UUSI
    def test_ei_voi_ottaa_saldoa_isompaa_maaraa_varastosta(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(saatu_maara, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
