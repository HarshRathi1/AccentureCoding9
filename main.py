'''You are given a function,
Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);
The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.
Assumption: String Contains only lower-case alphabetical letters.
Note:
Return null if string is null.
If both characters are not present in string or both of them are same , then return the string unchanged.
Example:
Input:
Str: apples
ch1:a
ch2:p
Output:
paales
Explanation:
‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales.'''
str="apple"
ch1='a'
ch2='p'
n=len(str)
def ReplaceCharacter(str,n,ch1,ch2):
    if n<1:
        return 'null'
    if (ch1 not in str and ch2 not in str) or ch1==ch2:
        return str
    else:
        arr = list(str)
        s = ''
        for i in range(n):
            if arr[i] == ch1:
                arr[i] = ch2
            elif arr[i] == ch2:
                arr[i] = ch1
        for i in arr:
            s += i
        return s
print(ReplaceCharacter(str,n,ch1,ch2))