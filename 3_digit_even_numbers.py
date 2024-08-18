
"""
Finding 3-Digit Even Numbers
You are given an integer array digits, where each element is a digit. The array may contain duplicates.
You need to find all the unique integers that follow the given requirements:
The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
Return a sorted array of the unique integers.

Example 1:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.

Example 2:
Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.

Example 3:
Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.

Constraints:
3 <= digits.length <= 100
0 <= digits[i] <= 9


"""
# # print(input_array)
#
# map = defaultdict(int)
# for i in input_array:
#     map[i] += 1
#
# # print(map)
#
# evens = []
# for i in input_array:
#     if i % 2 == 0:
#         evens.append(i)
#
# # print(f'{evens=}')
# # print(f'{map}')
#
#
# two_digits = []
# for i in evens:
#     for j in input_array:
#         print(i, j)
#         if i == j:
#             if map[j] > 1:
#                 two_digits.append(j * 10 + i)
#                 map[j] -=1
#         else:
#             two_digits.append(j * 10 + i)
#
# print(two_digits)
# print(map)
#
# three_digits = []
# for i in two_digits:
#     for j in input_array:
#         if j != 0:
#             if map[int(i // 10)] > 1 and map[int(i % 10)] > 1 and map[j] > 1:
#                 three_digits.append(j * 100 + i)
#
#             # if not(str(j) in str(i)):
#             # three_digits.append(j*100 + i)
#
# print(sorted(set(three_digits)))
#
#

# result = []
# for i in range(len(input_array)):
#     for j in range(i+1, len(input_array)):
#         if input_array[i] != 0:
#             c = input_array[i] * 100 + input_array[j] * 10
#             for k in range(len(input_array)):
#                 if input_array[k] % 2 == 0:
#                     c += input_array[k]
#                     result.append(c)
#
# print(sorted(result))

def finding_3_digit_even_numbers(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i != j and i != k and j != k and data[i] != 0 and data[k] % 2 == 0:
                    result.append(data[i]*100 + data[j]*10 + data[k])

    return sorted(set(result))


def test_finding_3_digit_even_numbers():
    test_data = (
        ([3, 7, 5], []),
        ([2, 1, 3, 0], [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]),
        ([2, 2, 8, 8, 2], [222, 228, 282, 288, 822, 828, 882])
    )
    for input_data, answer in test_data:
        assert finding_3_digit_even_numbers(input_data) == answer, 'Wrong answer'

    print('All tests pass')


test_finding_3_digit_even_numbers()

