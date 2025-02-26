import re
text = [
    '+7-(123)-45678',
    '+7-123-45678',
    '+7-12-345678',
    '+7-(1234)-5678',
    '+7-12345-678'
]
for i in text:
    # print(i)
    print(re.match("^\+7-(\d{3,5})-\d{3,5}?", i) is not None)


"""
(...)
Matches whatever regular expression is inside the parentheses,
 and indicates the start and end of a group
"""