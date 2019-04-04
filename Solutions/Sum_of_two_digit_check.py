class SumOfTwoDigitCheck():

    def __init__(self, list_number, digit):
        self.list_number = list_number
        self.digit = digit

    def sort_first_method(self):
        list_sorted = sorted(self.list_number)
        left_limit = 0
        right_limit = len(self.list_number) - 1
        while left_limit < right_limit:
            sum_in_iteration = list_sorted[right_limit] + list_sorted[left_limit]
            if sum_in_iteration == self.digit:
                return True
            if sum_in_iteration < self.digit:
                left_limit += 1
            if sum_in_iteration > self.digit:
                right_limit -= 1
        return False

    def check_sum_pair(self):

        known_numbers = set()
        for number in self.list_number:
            if (self.digit - number) in known_numbers:
                return True
            else:
                known_numbers.add(number)
        return False

    def min_max_method(self):
        while self.list_number:
            lowest_digit = min(self.list_number)
            highest_digit = max(self.list_number)
            sum_in_iteration = lowest_digit + highest_digit
            if sum_in_iteration == self.digit:
                return True
            elif sum_in_iteration < self.digit:
                self.list_number.remove(lowest_digit)
            elif sum_in_iteration > self.digit:
                self.list_number.remove(highest_digit)
        return False


if __name__ == "__main__":
    digit_input = 0
    list_input = [int(x) for x in input("Input the list separated by spaces").strip().split()]
    digit_input = int(input("Enter the number to search"))
    checker_class = SumOfTwoDigitCheck(list_input, digit_input)
    print("method with sort")
    print (checker_class.sort_first_method())
    print("check sum pair method")
    print (checker_class.check_sum_pair())
    print("Min Max Method")
    print (checker_class.min_max_method())
