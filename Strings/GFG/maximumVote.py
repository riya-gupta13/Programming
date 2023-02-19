import collections


def maximumVote(arr):
    votes = collections.Counter(arr)
    print(votes)
    ans=[]
    val = max(votes.values())
    for i in votes.keys():
        if votes[i]==val:
            ans.append(i)
    print(ans)
    return sorted(ans)[0]




votes = ["john", "johnny", "jackie",
         "johnny", "john", "jackie",
         "jamie", "jamie", "john",
         "johnny", "jamie", "johnny",
         "john"]
print(maximumVote(votes))
