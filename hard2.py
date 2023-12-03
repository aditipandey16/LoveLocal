def shortest(s):
    def palindrome(sub):
        return sub == sub[::-1]

    n = len(s)
    
    for i in range(n - 1, -1, -1):
        if palindrome(s[:i + 1]):
            return s[i + 1:][::-1] + s

    return s 

s = input()
print(shortest(s))