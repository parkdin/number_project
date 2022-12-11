class Number:
    def __init__(self, value):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        n = self.value
        if n % 2 != 0:
            return True
        else:
            return False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        n = self.value
        if n % 2 == 0:
            return True
        else:
            return False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        n = self.value
        if n > 1:
            for i in range(2, n):
                if n % i != 0:
                    return True
                else:
                    return False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        n = self.value
        divisor = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisor += [i]
        return divisor

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        n = self.value
        sum = 0
        for i in str(n):
            sum += int(i)
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        n = self.value
        reverse = (str(n))[::-1]
        return int(reverse)

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        n = self.value
        reversed = (str(n))[::-1]
        if int(reversed) == n:
            return True
        else:
            return False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        n = self.value
        num_list = []
        for i in str(n):
            num_list.append(i)
        return num_list

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        n = self.value
        max = int((str(n))[0])
        for i in str(n):
            i = int(i)
            if i > max:
                max = i
        return max
    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        n = self.value
        min = int((str(n))[0])
        for i in str(n):
            i = int(i)
            if i < min:
                min = i
        return min

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        n = self.value
        sum = 0
        average = 0
        for i in str(n):
            sum += int(i)
        average = float(sum / len(str(n)))
        return average
    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        n = self.value
        sort = []
        for i in str(n):
            min = (str(n))[0]
            if min > (str(n)[int(i)]):
                sort += [min]

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(987)
#print(number.get_number())
#print(number.is_odd())
print(number.get_median())