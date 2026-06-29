def rearrange_by_frequency(nums: list[int]) -> list[int]:
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return sorted(nums, key=lambda x: (-freq[x], x))


print(rearrange_by_frequency([4, 5, 6, 5, 4,3, 3, 4]))