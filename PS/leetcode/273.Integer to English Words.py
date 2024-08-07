class Solution(object):
    def numberToWords(self, num):
        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return "Zero"

        def to_words(n):
            if n < 20:
                return less_than_twenty[n]
            elif n < 100:
                return tens[n // 10] + ('' if n % 10 == 0 else ' ' + less_than_twenty[n % 10])
            else:
                return less_than_twenty[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + to_words(n % 100))

        billions, num = divmod(num, 1000000000)
        millions, num = divmod(num, 1000000)
        thousands, num = divmod(num, 1000)
        
        result = []
        if billions:
            result.append(to_words(billions) + ' Billion')
        if millions:
            result.append(to_words(millions) + ' Million')
        if thousands:
            result.append(to_words(thousands) + ' Thousand')
        if num:
            result.append(to_words(num))
        
        return ' '.join(result)