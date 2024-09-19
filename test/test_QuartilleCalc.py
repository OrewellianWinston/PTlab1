import pytest
from src.QuartilleCalc import QuartilleCalc
from src.Types import DataType


class TestQuartilleCalc:
    @pytest.fixture()
    def student_data(self) -> DataType:
        data = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return data

    @pytest.fixture()
    def expected_ratings(self) -> dict[str, float]:
        return {
            "Иванов Иван Иванович": (67 + 100 + 91) / 3,
            "Петров Петр Петрович": (78 + 87 + 61) / 3
        }

    def test_calc(self, student_data: DataType,
                  expected_ratings: dict[str, float]):
        quartille_calc = QuartilleCalc(student_data)
        ratings = quartille_calc.calc()
        assert ratings == pytest.approx(expected_ratings, abs=0.001)

    def test_compare(self, student_data: DataType):
        quartille_calc = QuartilleCalc(student_data)
        quartille_calc.calc()
        last_quartile_students = quartille_calc.compare()

        # Ожидаем, что Петров Петр Петрович попал в последнюю квартиль
        assert len(last_quartile_students) == 1
        assert last_quartile_students[0][0] == "Петров Петр Петрович"
