

class NumberLists:
    def __init__(self, first_list, second_list) -> None:
        self.firrst_list = first_list
        self.second_list = second_list

    def average_value_first_list(self):
        if self.second_list.count(0) == len(self.second_list):
            raise ZeroDivisionError('Делить на ноль нельзя')
        else:
            average = sum(self.firrst_list)/len(self.firrst_list)
            return average

    def average_value_second_list(self) -> float:
        if self.second_list.count(0) == len(self.second_list):
            raise ZeroDivisionError('Делить на ноль нельзя')
        average = sum(self.second_list)/len(self.second_list)
        return average

    def compare_values(self, average_first, average_second):
        if average_first > average_second:
            return "Первый список имеет большее среднее значение"
        elif average_first < average_second:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


# num_lists = NumberLists([1, 2, 3, 4], [3, 5, 7, 8])
# av_first = num_lists.average_value_first_list()
# av_first = num_lists.average_value_first_list()
# av_second = num_lists.average_value_second_list()

# num2_lists = NumberLists([1, 2, 3, 4], [0, 0, 0, 0])
# av_first = num2_lists.average_value_first_list()
# print(av_first)
# num_lists.compare_values(av_first, av_second)
