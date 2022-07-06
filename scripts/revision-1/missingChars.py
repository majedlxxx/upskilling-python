def missing_chars(string):
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    all_chars = list(all_chars)
    # all_chars = [str(i) for i in range(0,10)]  + [chr(i) for i in range(ord('a', ord('z')+1))]
    
    # missing = ""
    # for ch in all_chars:
    #     if ch not in string:
    #         missing += ch
    
    # return missing
    
    for ch in string:
        if ch in all_chars:
            all_chars.remove(ch)
    
    return "".join(all_chars)


print(missing_chars('abc123'))
"""
input: string
return value is a string consisting 
of 0-9 and a-z that are missing from the original string (in order)
output should start with digits 0-9 in order followed by lowercase chars a-z (in order)
example:
input: abc123
output: 0456789def....z


"""



