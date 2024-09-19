from .CalcRating import CalcRating
RatingType = dict[str, float]


class QuartilleCalc(CalcRating):
    def calc(self) -> RatingType:
        super().calc()
        return self.rating

    def compare(self):
        sorted_students = sorted(self.rating.items(), key=lambda x: x[1])

        quartile_size = len(sorted_students) // 4

        if quartile_size == 0:
            quartile_size = 1

        last_quartile_students = sorted_students[:quartile_size]

        print("Студенты в последней квартиле:")
        for student, rating in last_quartile_students:
            print(f"{student}: {rating}")

        return last_quartile_students
