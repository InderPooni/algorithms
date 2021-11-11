

def test_something(arr):
    n = len(arr)

    for k in range(n)[::-1]:
        print(arr[k])

def test(arr):
    n = len(arr)

    for k in range(n-1, -1, -1):
        print(arr[k])

print(test([31,4,312, 98,78,647]))

print("+++++++")
print(test_something([31,4,312, 98,78,647]))