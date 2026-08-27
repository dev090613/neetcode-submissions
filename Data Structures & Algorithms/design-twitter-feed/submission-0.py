class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.followList = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followList[userId].add(userId)
        users = self.followList[userId]

        maxHeap = []
        for user in users:
            lastIdx = len(self.posts[user]) - 1
            if lastIdx >= 0:
                timestamp, tweet = self.posts[user][lastIdx]        
                heapq.heappush(maxHeap, [ timestamp, tweet, user, lastIdx ])
        
        res = []
        while maxHeap and len(res) < 10:
            timestamp, tweet, user, lastIdx = heapq.heappop(maxHeap)
            res.append(tweet)

            if (lastIdx - 1) >= 0:
                timestamp, tweet = self.posts[user][lastIdx - 1]
                heapq.heappush(maxHeap, [ timestamp, tweet, user, lastIdx - 1 ])
            
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
        return