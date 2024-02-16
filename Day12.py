import functools

def isPlacingOK(chunk: str, spaces: int, num: int) -> bool:
	for i in range(spaces):
		if chunk[i] == '#':
			return False
	for i in range(spaces, spaces + num):
		if chunk[i] == '.':
			return False
	if len(chunk) > spaces + num and chunk[spaces + num] == '#':
		return False
	return True

@functools.lru_cache(maxsize=None)
def getPossibleOptions(chunk: str, nums: tuple, extra: int) -> int:
	res = 0
	if extra < 0:
		return 0
	if not nums and extra == 0:
		return 1
	if not nums:
		return 1 if isPlacingOK(chunk, extra, 0) else 0
	if extra == 0:
		return 1 if isPlacingOK(chunk, extra, nums[0]) else 0
	for i in range(extra + 1 - (len(nums) - 1)):
		buffer = 1 if len(nums) > 1 else 0
		if isPlacingOK(chunk, i, nums[0]) and extra >= i + buffer:
			res += getPossibleOptions(chunk[i + nums[0] + buffer:], nums[1:], extra - i - buffer)
	return res

result1 = []
result2 = []

with open("input.txt") as f:
	for line in f.readlines():
		chunks, nums = line.strip().split()
		nums1 = [int(x) for x in nums.split(',')]
		nums2 = [int(x) for x in nums.split(',')] * 5
		chunks2 = '?'.join([chunks for i in range(5)])
		result1.append(getPossibleOptions(chunks, tuple(nums1), len(chunks) - sum(nums1)))
		result2.append(getPossibleOptions(chunks2, tuple(nums2), len(chunks2) - sum(nums2)))

	print("Result 1:", sum(result1))
	print("Result 2:", sum(result2))