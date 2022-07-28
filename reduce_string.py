def solution(S):
    letters = []
    for char in S:
        if letters and letters[-1] == char:
            letters.pop()
        else:
            letters.append(char)

    return "".join(letters)
