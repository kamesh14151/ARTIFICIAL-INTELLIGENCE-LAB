# EX.NO.7 — Information Retrieval Using Semantic Search

## 🎯 Aim
To design and implement a system for **information retrieval using semantic search** by segmenting a string without spaces into meaningful words using a **dictionary and dynamic programming** approach.

---

## 📚 Algorithm

1. Start the program
2. Define a **dictionary** of valid words
3. Input a **string without spaces**
4. Create a **DP array** to store valid segment positions
5. Initialize `DP[0] = True` (empty string is valid)
6. For each position `i` in the string:
   - Check all previous positions `j < i`
   - If `s[j:i]` is in dictionary **and** `DP[j] == True`
   - Mark `DP[i] = True` and store the word
7. **Reconstruct** segmented words using stored positions
8. **Display** the segmented words
9. Stop the program

---

## 💻 Program (Python)

```python
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
```

---

## 🖼️ Output

![Semantic Search Output](exp7/semantic-search/search.png)

---

## ✅ Result
The **semantic search-based information retrieval system** was successfully implemented using a dynamic programming approach, and the input string was segmented into meaningful words.
