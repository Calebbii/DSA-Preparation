def insert(self, intervals):
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        
        result.append(newInterval)
        
        # Add all intervals that come after the new interval
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result