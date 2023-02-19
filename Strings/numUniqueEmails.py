def numUniqueEmails(emails: list[str]) -> int:
    l2 = []
    l1 = []
    l3 = []
    for e in emails:
        s = e.split('@')[0]
        s1 = e.split('@')[1]
        l2.append(s1)
        s = s.replace('.', '')
        if '+' in s:
            ind = s.index('+')
            s = s[:ind]
        l1.append(s.split()[0])
    for i in range(0, len(l1)):
        new = l1[i] + '@' + l2[i]
        print(new)
        l3.append(new)
    print(len(set(l3)))


emails = ["alice.z@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
numUniqueEmails(emails)
