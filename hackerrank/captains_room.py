if __name__ == "__main__":
    k = int(input())
    room_nums = input().split()
    unique_room_nums = set(room_nums)
    for unique_room_num in unique_room_nums:
        room_nums.remove(unique_room_num)
    captains_room = unique_room_nums.difference(set(room_nums)).pop()
    print(captains_room)
