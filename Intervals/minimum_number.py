def findMinArrowShots(points):
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    
    for start, point in points:
        if start > end:
            arrows += 1
            end = point
    
    return arrows