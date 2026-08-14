class Solution(object):
    def divide(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        return min(max(result, -2**31), 2**31 - 1)