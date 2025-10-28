def getNeighbors(string, wordBanks):
    neighbors = []
    str_ = ""
    for i in range(len(wordBanks)):
        if string.startswith(wordBanks[i]):
            neighbors.append((wordBanks[i], string[len(wordBanks[i]):]))
    return neighbors


memo = {}

def canConstruct(string, wordBank):
    global memo
    if len(string) == 0:
        return True

    if string in memo:
        return memo[string]

    neighbors = getNeighbors(string, wordBank)
    isConstruct = False

    for neighbor, rest in neighbors:
        if neighbor in wordBank:
            isConstruct = isConstruct or canConstruct(rest, wordBank)

    memo[string] = isConstruct
    return isConstruct
    
def run_correctness_tests():
    test_cases = [
        # Basic examples
        ("abcdef", ["ab", "abc", "cd", "def", "abcd"], True),
        ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], False),
        ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], True),

        # Edge / simple cases
        ("", ["cat", "dog", ""], True),             # empty string always constructible
        ("abc", [], False),                         # empty word bank
        ("aaaa", ["a"], True),                      # repeated single letter
        ("aaaa", ["aa"], True),                     # repeated longer piece
        ("aaaa", ["b"], False),                     # impossible prefix
        ("catsdog", ["cat", "cats", "dog"], True),  # overlapping prefix words
        ("potato", ["p", "po", "t", "ta", "to"], True),  # multiple short pieces
        ("apple", ["ap", "app", "le"], True),       # multiple partial matches
    ]

    passed = 0
    print("🔍 Running quick correctness tests...\n")
    for target, wordBank, expected in test_cases:
        global memo
        try:
            memo = {}
            result = canConstruct(target, wordBank)
            correct = (result == expected)
            status = "✅" if correct else "❌"
            print(f"{status} Target='{target}' → got {result}, expected {expected}")
            if correct:
                passed += 1
        except Exception as e:
            print(f"❌ Target='{target}' raised an error: {e}")

    print(f"\nResult: Passed {passed}/{len(test_cases)} correctness tests.\n")

# Run the quick correctness tests
run_correctness_tests()
