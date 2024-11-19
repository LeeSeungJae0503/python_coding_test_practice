def solution(cards):
    def explore_group(start, visited):
        group_size = 0
        current = start
        while not visited[current]:
            visited[current] = True
            current = cards[current] - 1
            group_size += 1
        return group_size
    
    
    visited_list = [False] * len(cards)
    group_size = []
    count = 0
    
    for i in range(len(cards)):
        if not visited_list[i]:
            group_size.append(explore_group(i, visited_list))
            
    group_size.sort(reverse=True)
    
    if len(group_size) < 2:
        return 0
    return group_size[0] * group_size[1]
        