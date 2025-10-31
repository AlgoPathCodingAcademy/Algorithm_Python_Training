def canConsruct(target, wordBank, dp):
    for i in range(1,len(target)+1):
        for item in wordBank:
            item_len = len(item)
            
            if i - item_len < 0 :
                continue
            
            if dp[i - item_len]:
                # Both methods work
                #if target[i-item_len:i] == item:
                if target[0:i - item_len] + item == target[0:i]:
                    dp[i] = True

    print(dp)
    return dp[len(target)]

def wordBreak(str, wordDict):
    if not s:
        return True
    dp = [False] * (len(s)+1)
    dp[0] = True
    return canConsruct(s,wordDict,dp)
    
s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s,wordDict))


s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s,wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s,wordDict))
