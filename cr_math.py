def arithmetic_mean(nums):
    return (sum(nums))/len(nums)
n = int(input())
print(arithmetic_mean([int(input()) for i in range(n)]))