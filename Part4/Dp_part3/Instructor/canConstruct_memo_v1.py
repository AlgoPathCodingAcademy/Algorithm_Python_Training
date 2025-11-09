memo = {}

def canConstruct(target, wordBank):
    global memo

    if len(target) == 0:
        return True
        
    if target in memo:
        return memo[target]

    # This pattern is as same as the one used in search in Binary Tree
    isFound = False
    for item in wordBank:
        if target.startswith(item):
            isFound = isFound or canConstruct(target[len(item):],wordBank)
    
    memo[target] = isFound
    return isFound
    
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
    print("Running quick correctness tests...\n")
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
