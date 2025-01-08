def findSubstring(s, k):
    # Write your code here
    result = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_vowel = 0
    vowel_count = 0
    for i in range(k):
        if s[i] in vowels:
            vowel_count += 1
    if vowel_count != 0:
        max_vowel = vowel_count
        result = s[0:k]
    for i in range(k, len(s)):
        if s[i] in vowels:
            vowel_count += 1
        if s[i-k] in vowels:
            vowel_count -= 1
        if vowel_count > max_vowel:
            max_vowel = vowel_count
            result = s[i-k+1:i+1]
    if max_vowel == 0:
        return "Not found"
        
    return result

s = 'azerdii'
k = 5
print(findSubstring(s,k))