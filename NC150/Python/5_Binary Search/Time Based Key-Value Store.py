class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key,[])
        res = ""
        l,r = 0, len(values)-1
        while(l<=r):
            mid = (l+r)//2
            if(values[mid][1] == timestamp):
                res = values[mid][0]
                return res
            elif(timestamp > values[mid][1]):
                res = values[mid][0] # closest element of the value being searched
                l = mid+1
            else:
                r = mid-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)