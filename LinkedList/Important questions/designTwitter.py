class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class Twitter:

    def __init__(self):
        self.LinkedList = LinkedList()
        self.map={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.LinkedList.head = userId
        self.map.__setitem__()

    def getNewsFeed(self, userId: int) -> list[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
