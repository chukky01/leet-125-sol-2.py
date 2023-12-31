class Solution:
  def isPalindrome(self,s:str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
      while left < right and not s[left].isalnum():
        right -= 1
      if s[left].lower() != s[right].lower():
        return False
      left, right = left + 1, right - 1
    return True
