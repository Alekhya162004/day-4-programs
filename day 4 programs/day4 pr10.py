def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) != sorted(s2):
        return False
    if len(s1) == 1:
        return s1 == s2
    for i in range(1, len(s1)):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if isScramble(s1, s2):
    print("True")
else:
    print("False")
