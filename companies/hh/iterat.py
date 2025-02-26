print(
    next(iter([1, 2, 3]))
)
print(
    sum(iter([1, 2, 3]))
)
try:
    print(
        iter([1, 2, 3])[0]  # error
    )
except Exception as e:
    print(e)
print(
    [x for x in iter([1, 2, 3])]
)
print(
    list(iter([1, 2, 3]))
)

i = iter([1, 2, 3])
print(i)
print(next(i))
print(next(i))
print(next(i))
