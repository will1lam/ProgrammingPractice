# One of my all time favorite problems. A variation of this classic problem introduced me to Python programming.

# The prompt:
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Solution:
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Create an array to store your answers, notice that "-> List[str]:" indicates a return time of an array of strings.
        answerArr = []
        # Start off with i = 1, because the prompt asks for a (1-indexed) string array for your answer.
        i = 1
        # We want to compare i at the starting index, as well as the final index n, so we need to add (n + 1) to avoid an "off-by-one" error, and check all the numbers from (1-indexed).
        while (i != (n + 1)):
            if (((i % 3) == 0) and ((i % 5) == 0)):
                answerArr.append("FizzBuzz")
            elif ((i % 3) == 0):
                answerArr.append("Fizz")
            elif ((i % 5) == 0):
                answerArr.append("Buzz")
            else:
                answerArr.append(str(i))
            # Don't want any infinite loops.
            i += 1
        return answerArr
      
