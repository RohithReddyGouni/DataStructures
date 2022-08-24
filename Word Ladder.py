class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbours=collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for eachLetter in range(len(word)):
                pattern=word[:eachLetter]+"*"+word[eachLetter+1:]
                neighbours[pattern].append(word)
        visited=set([beginWord])
        
        Que=deque([beginWord])
        
        count=1
        while Que:
            for i in range(len(Que)):
                word=Que.popleft()
                if word==endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for nei in neighbours[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            Que.append(nei)
            count+=1
        return 0