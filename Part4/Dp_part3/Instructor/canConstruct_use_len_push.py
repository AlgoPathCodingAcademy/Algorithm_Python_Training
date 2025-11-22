def canConstruct(target, wordBank, dp):
    for i in range(len(target)+1):
        for item in wordBank:
            if dp[i]:
                if target[i:i+len(item)] == item:
                    dp[i+len(item)] = True

    print(dp)
    return dp[len(target)]

def wordBreak(s, wordDict):
    if not s:
        return True
    dp = [False] * (len(s)+1)
    dp[0] = True
    return canConstruct(s,wordDict,dp)
    
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s,wordDict))

s = "leetcode"
wordDict = ["leet","code"]

print(wordBreak(s,wordDict))

s = "catsandog"

wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s,wordDict))
