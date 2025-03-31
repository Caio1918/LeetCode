def buddyStrings(s, goal):
    copy = s

    for i in range(len(s)*(len(s)-1)):
        for j in range(len(s)*(len(s)-1)):
            point = copy[i]
            copy[i] = copy[j]
            copy[j] = point

            if copy == goal:
                return true
            else:
                continue


