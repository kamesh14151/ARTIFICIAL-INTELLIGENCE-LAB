dictionary = {
    "the", "longest", "list", "of", "stuff",
    "at", "domain", "name", "long", "last"
}

def word_segment(s, dictionary):
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    words_used = [""] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                words_used[i] = s[j:i]
                break

    if not dp[n]:
        return None

    result = []
    i = n
    while i > 0:
        word = words_used[i]
        result.insert(0, word)
        i -= len(word)

    return result

text = "thelongestlistofthelongeststuffatthelongestdomainnameatlonglast"

result = word_segment(text, dictionary)
if result:
    print("Segmented Words:", result)
else:
    print("No valid segmentation found")
