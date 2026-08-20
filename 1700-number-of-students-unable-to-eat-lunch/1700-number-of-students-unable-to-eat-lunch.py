class Solution(object):
    def countStudents(self, students, sandwiches):
        q=deque(students)
        i=0

        while q:
            if q[0]==sandwiches[i]:
                q.popleft()
                i+=1
            else:
                q.append(q.popleft())

            if all(student!=sandwiches[i] for student in q):
                break
        return len(q)                
        