"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([ i.start for i in intervals])
        end = sorted([ i.end for i in intervals])
        s,e = 0,0
        res,count = 0,0
        while(s < len(intervals)):
            if(start[s] < end[e]):
                count+=1
                res = max(res,count)
                s+=1
            else:
                count-=1
                e+=1
        return res