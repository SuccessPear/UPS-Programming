def valid_pattern(s, p):
    # Initialize the index for pattern p
    i = 0

    # Simplify the pattern string by removing redundant characters after '*'
    while i < len(p):
        # If the current character is preceded by a '*' and matches the character before '*',
        # it is redundant, so remove it from the pattern
        if p[i-1] == '*':
            if p[i] == p[i-2]:
                # Remove the redundant character from pattern p
                p = p[:i] + p[i+1:]
                continue
        i += 1

    # Initialize indices for the input string (s) and the pattern (p)
    i = 0
    j = 0

    # Match the input string (s) against the simplified pattern (p)
    while i < len(s) and j < len(p):
        # If match, move on
        if s[i] == p[j]:
            i += 1
            j += 1
            continue

        # If p[j] = '.' move on
        if p[j] == '.':
            i += 1
            j += 1
            continue

        #'*' in the pattern
        if p[j] == '*':
            # If the current character in the string matches the character before '*', 
            # move to next index in s
            if s[i] == s[i-1]:
                i += 1
                continue
            # If the characters don't match, move to the next character in the pattern
            if s[i] != s[i-1]:
                j += 1
                continue

        # If no conditions match, return False (pattern doesn't match)
        return False

    # If both the string and pattern are not fully processed
    if i != len(s) and j != len(p):
        return False

    # If both string and pattern are fully processed, the pattern matches the string
    return True

p = 'a*cc.b'
s = 'aaaaacceb'
print(valid_pattern(s, p))
