class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list) # structure: {key: [(timestamp, value)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # take a specific key and index into timestamps
        # then provided that you have a list of timestamps
        # which must be ordered by timestamps since direction of
        # insertion is strictly increasing when it comes to timestamps
        if key not in self.timestamps:
            return ""

        left = 0
        right = len(self.timestamps[key]) - 1
        selected = ""

        while left <= right:
            # in this case, whenever middle <= timestamp, left = middle; else right = middle - 1
            middle = (left + right) // 2
            if self.timestamps[key][middle][0] == timestamp:
                return self.timestamps[key][middle][1]
            elif self.timestamps[key][middle][0] < timestamp:
                selected = self.timestamps[key][middle][1]
                left = middle + 1
            else:
                right = middle - 1
        
        return selected 


        
        
        
