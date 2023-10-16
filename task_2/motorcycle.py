from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release) -> None:
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75
        return self.speed

    def park(self):
        self.park = 0
        return self.park

    def get_num_wheels(self):
        return self.num_wheels
