import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # [[0,10],[1,5],[12,17],[13,14]]
        # end_room_num = minheap [[10, 0], [5, 1], []] # get the earlier unused room
        # unused_rooms = minheap [0, 1] # lowest number meeting room
        meetings.sort(key=lambda x: x[0])
        end_room_num = []
        unused_rooms = [i for i in range(n)]
        count = [0] * n
        for start, end in meetings:
            while len(end_room_num) > 0 and start >= end_room_num[0][0]:
                _, room = heapq.heappop(end_room_num)
                heapq.heappush(unused_rooms, room)

            if len(unused_rooms) > 0:
                room = heapq.heappop(unused_rooms)
                heapq.heappush(end_room_num, (end, room))
                count[room] += 1
            else:
                tmpend, tmproom = heapq.heappop(end_room_num)
                heapq.heappush(end_room_num, (tmpend + end - start, tmproom))
                count[tmproom] += 1
        
        res, rescount = -1, -1
        for i in range(n):
            if count[i] > rescount:
                rescount = count[i]
                res = i
        return res

