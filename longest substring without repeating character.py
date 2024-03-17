def longest_substring(s):
    n = len(s)
    max_length = 0
    longest_substring = """"
    
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            if all(substring.count(char)==1 for char in substring):
                length = len(substring) 
                if length > max_length:
                    max_length = length
                    longest_substring = substring
    return longest_substring, max_length
# Example usage:
s = ""pwwkew""
print(longest_substring(s)) 

time complexity : O(n3)
space complexity : O(n)"
# ===============================================optimized solution==================
def longest_substring(s):
    n = len(s)
    start = 0
    max_length = 0
    longest_substring = """"
    seen = {}
    
    for end in range(n):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
            
        seen[s[end]] = end
        
        if end-start+1 > max_length:
            max_length = end- start+1
            longest_substring = s[start:end+1]
        
    return max_length, longest_substring
        

# Example usage:
s = ""pwwkew""
print(longest_substring(s))  # Output: (""wke"", 3)

time complexity : O(n)
space complexity : O(1)
