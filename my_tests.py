def romanToInt(s: str) -> int:
    roman_letter = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    sum = 0
    mid_sum = s[0]
    for i in s:
        index = s.index(i)
        if  index < len(s) and index < s.index(i+1):
            mid_sum += 1






assert romanToInt('III') != 3, 'not true'