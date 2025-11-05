from collections import deque
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        q = deque()
        time = 0
        for i in range(len(tickets)):
            q.append(i)
        #print(q)
        
        while(tickets[k]!=0):
            currentPerson = q.popleft()
            tickets[currentPerson] = tickets[currentPerson]-1
            #print("Current Person and Tickets:",currentPerson, tickets[currentPerson])
            #print(q)
            if tickets[currentPerson]!=0:
                q.append(currentPerson)
            #print(q)
            time+=1
        return time
            

        