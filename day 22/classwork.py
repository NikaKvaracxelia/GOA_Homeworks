# name = "Nika"

# print(name[1:3])



# name = "giorgi"

# print(name[0:2 + 1])


# list = [1 , 2 , 3 , 4 , 5 , 6]


# print(list[0:3 + 1])


def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    current = start

    if step > 0:
        while current < stop:
            current += step
    elif step < 0:
        while current > stop:
            current += step
    else:
        print("Step cannot be zero")
    

def range_reverse(start, stop):
    if start < stop:
        return range(stop - 1, start - 1, -1)
    else:
        return range(stop + 1, start + 1, 1)
    
start = 10
stop = 5
for i in range_reverse(start, stop):
    print(i)

print("join goa")
print("join goa")
