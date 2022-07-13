a_list = list(map(int, input().split()))

a_list.append(a_list[0] != a_list[-1])

print(*a_list)