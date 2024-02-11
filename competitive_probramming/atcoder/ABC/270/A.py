A, B = map(int, input().split())

if A == 7 or B == 7:
    print(7)
elif A + B == 7:
    print(7)
elif A == B :
    print(A)
elif A <= 3 and B <= 3:
    print(3)
elif set([A, B]) == set([4, 1]):
    print(5)
elif set([A, B]) == set([4, 2]):
    print(6)
elif set([A, B]) == set([5, 1]):
    print(5)
elif set([A, B]) == set([5, 3]):
    print(7)
elif set([A, B]) == set([5, 4]):
    print(5)
elif set([A, B]) == set([6, 2]):
    print(6)
elif set([A, B]) == set([6, 3]):
    print(7)
elif set([A, B]) == set([6, 4]):
    print(6)
elif set([A, B]) == set([6, 5]):
    print(7)