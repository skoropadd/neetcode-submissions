class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.time = 0 
        self.followers = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        users = self.followers[userId] | {userId}
        for u in users: 
            for time, tid in self.tweets[u][-10:]: 
                heapq.heappush(feed, (time, tid))
                if len(feed) > 10: 
                    heapq.heappop(feed)

        res = []
        while feed: 
            res.append(heapq.heappop(feed)[1])

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)