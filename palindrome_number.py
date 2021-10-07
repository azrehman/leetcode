class Solution:
	def isPalindrome(self, x: int) -> bool:
		# edge case negatives:
		if x < 0:
			return False
		# edge case end with 0:
		if x % 10 == 0:
			return x == 0

		# general case
		temp = x
		rev = 0
		# construct reverse of x
		while (temp > 0):
			last = temp % 10
			rev = (rev * 10) + last
			temp //= 10
		return x == rev
