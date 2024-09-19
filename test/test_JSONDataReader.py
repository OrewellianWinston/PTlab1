# -*- coding: utf-8 -*-
from src.Types import DataType
from src.JSONDataReader import JSONReader
import pytest
import json


class TestJSONReader:
    @pytest.fixture()
    def json_file_content(self) -> tuple[dict[str, dict[str, int]], DataType]:
        json_data = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 78,
                "химия": 87,
                "социология": 61
            }
        }
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
        return json_data, data

    def test_read(self, tmpdir,
                  json_file_content:
                  tuple[dict[str, dict[str, int]], DataType]):
        json_data, expected_data = json_file_content

        json_file = tmpdir.join("students.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
        reader = JSONReader()
        students = reader.read(str(json_file))
        assert students == expected_data
