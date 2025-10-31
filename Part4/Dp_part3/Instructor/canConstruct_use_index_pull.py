def canConsruct(target, wordBank, dp):
    for i in range(1,len(target)):
        for item in wordBank:
            item_length = len(item)
            if i-item_length < -1:
                continue

            if i-item_length+1 < 0:
                continue
           
            # Very important!
            # Instructor should discuss why it is processed like this
            if i-item_length == -1:
                if target[i-item_length+1:i+1] == item:
                    dp[i] = True
                    break
            elif target[i-item_length+1:i+1] == item and dp[i-item_length]:
                dp[i] = True
                break

    print(dp)
    return dp[len(target)-1]

def wordBreak(str, wordDict):
    if not s:
        return True
    dp = [False] * (len(s))
    if s[0] in wordDict:
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
