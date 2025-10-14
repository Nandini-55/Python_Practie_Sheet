#check if given strings are anagrams or not
#anagrams are words that contain the same characters but in different order 

inp=input()
check=input()
if(sorted(inp.lower())==sorted(check.lower())):
    print("Anagram")
else:
    print("Not anagram")
