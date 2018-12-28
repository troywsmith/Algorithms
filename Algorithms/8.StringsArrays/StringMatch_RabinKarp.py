"""
Name: The Rabin Karp Algorithm
Description: Returns all occurences of pattern string in text string
Input: a text string and a pattern string
Output: list of occurences
Time Complexity: best/average-O(n+m), worst O(nm)
Space Complexity: 
Algorithm Technique: N/A
"""


def search(txt, pat, d, q):
    M = len(pat)
    N = len(txt)
    h = pow(d, M-1, q)
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    occurences = []

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N-M+1):

        # Check the hash values of current window of text and pattern
        if p == t:

            match = True

            # Check for characters one by one
            for j in range(M):

                if txt[i+j] != pat[j]:
                    match = False
                    break

            if match:
                occurences.append(i)

        # Calculate hash value for next window of text:
        # Remove leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t+q

    return occurences


# Driver program to test the above function
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
d = 256  # number of characters in the input alphabet
q = 101  # A prime number
print("Pattern found at index " + str(search(txt, pat, d, q)))
print("Pattern found at index " + str(search('acaabc', 'aab', d, q)))
print("Pattern found at index " + str(search('acaaca', 'aca', d, q)))
print("Pattern found at index " + str(search('000010001010001', '0001', d, q)))