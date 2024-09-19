from DataReader import DataReader
import json
from Types import DataType


class JSONReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        students = {}
        for student, subject in data.items():
            students[student] = [(subject, int(score)) for subject, score in subject.items()]
        return students
