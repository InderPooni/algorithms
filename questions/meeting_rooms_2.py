def meeting_room(intervals):
    n = len(intervals)

    start = [0] * n
    end = [0] * n

    for i in range(n):
        start[i] = intervals[i][0]
        end[i] = intervals[i][1]
    

    start.sort()
    end.sort()


    ending = 0
    meetingRooms = 0
    for i in range(n):
        if start[i] < end[ending]:
            meetingRooms += 1
        else:
            ending += 1
    
    return meetingRooms
