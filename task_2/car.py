from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year_release) -> None:
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60
        return self.speed

    def park(self):
        self.speed = 0
        return self.speed

    def get_num_wheels(self):
        return self.num_wheels

    def get_speed(self):
        return self.speed
