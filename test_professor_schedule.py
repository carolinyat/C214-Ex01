import unittest # Biblioteca para testes unitários
from professor_schedule import ProfessorSchedule # Classe a ser testada

class TestProfessorSchedule(unittest.TestCase):

    # Dados que serão usados no teste
    def setUp(self):
        # Campos válidos
        self.valid_data = {
            "nomeDoProfessor": "Dr. Renzo",
            "horarioDeAtendimento": "08:00 - 10:00",
            "periodo": "integral",
            "sala": "3"
        }
        # Campos inválidos
        self.invalid_data = {
            "nomeDoProfessor": "",
            "horarioDeAtendimento": "",
            "periodo": "",
            "sala": ""
        }

    # Testes de sucesso

    def test_predio_correct_for_sala_1_to_5(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("3"), 1) 

    def test_predio_correct_for_sala_6_to_10(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("7"), 2)

    def test_predio_correct_for_sala_above_10(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("12"), 3)

    def test_populate_schedule_success(self):
        ps = ProfessorSchedule(self.valid_data)
        result = ps.populate_schedule()
        self.assertEqual(result['predio'], 1)
        self.assertEqual(result['nomeDoProfessor'], "Dr. Renzo")
        self.assertEqual(result['horarioDeAtendimento'], "08:00 - 10:00")
        self.assertEqual(result['periodo'], "integral")
        self.assertEqual(result['sala'], "3")

    def test_predio_for_edge_sala_5(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("5"), 1)

    def test_predio_for_edge_sala_10(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("10"), 2)

    def test_predio_correct_for_sala_11_to_15(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("14"), 3)

    def test_populate_schedule_success_with_different_sala(self):
        data = self.valid_data.copy()
        data["sala"] = "8"
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertEqual(result['predio'], 2)
        self.assertEqual(result['sala'], "8")

    def test_populate_schedule_success_with_periodo_noturno(self):
        data = self.valid_data.copy()
        data["periodo"] = "noturno"
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertEqual(result['periodo'], "noturno")

    def test_populate_schedule_success_full_data(self):
        data = {
            "nomeDoProfessor": "Dr. Ana",
            "horarioDeAtendimento": "14:00 - 16:00",
            "periodo": "noturno",
            "sala": "6"
        }
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertEqual(result['nomeDoProfessor'], "Dra. Rosana")
        self.assertEqual(result['horarioDeAtendimento'], "14:00 - 16:00")
        self.assertEqual(result['periodo'], "noturno")
        self.assertEqual(result['sala'], "6")
        self.assertEqual(result['predio'], 2)

    # Testes de falha

    def test_invalid_sala_empty(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.get_predio("")

    def test_invalid_sala_non_numeric(self):
        ps = ProfessorSchedule(self.valid_data)
        with self.assertRaises(ValueError):
            ps.get_predio("abc")

    def test_missing_nome_do_professor(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_missing_horario_de_atendimento(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_missing_periodo(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_missing_sala(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_sala_with_spaces(self):
        ps = ProfessorSchedule(self.valid_data)
        with self.assertRaises(ValueError):
            ps.get_predio("   ")

    def test_null_values_in_fields(self):
        data = {
            "nomeDoProfessor": None,
            "horarioDeAtendimento": "08:00 - 10:00",
            "periodo": "integral",
            "sala": "4"
        }
        ps = ProfessorSchedule(data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_invalid_period_value(self):
        data = self.valid_data.copy()
        data["periodo"] = "manhã"
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertNotEqual(result['periodo'], "integral")
        self.assertEqual(result['periodo'], "manhã")

    def test_invalid_field_format(self):
        data = self.valid_data.copy()
        data["horarioDeAtendimento"] = "no horário da tarde"
        ps = ProfessorSchedule(data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

if __name__ == "__main__":
    unittest.main()
