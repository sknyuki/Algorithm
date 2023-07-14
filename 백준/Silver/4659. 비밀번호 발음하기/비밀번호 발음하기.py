while 1:
    s = input();
    if s == "end":
        break
    mo_flag = 0
    two_flag = 1
    three_flag = 1
    
    for i in range(len(s)):
        if s[i] in ['a','e','i', 'o', 'u']:
            mo_flag = 1
        
        if i == 0:
            continue
        elif i == 1:
            if (s[i-1] == s[i]) & (s[i] not in ['e', 'o']):
                two_flag = 0
                break
            continue
        
        if (s[i-1] == s[i]) & (s[i] not in ['e', 'o']):
            two_flag = 0
            break
            
        if (s[i-2] in ['a', 'e', 'i', 'o', 'u']) & (s[i-1] in ['a', 'e', 'i', 'o', 'u']) & (s[i] in ['a', 'e', 'i', 'o', 'u']):
            three_flag = 0
            break
            
        if (s[i-2] not in ['a', 'e', 'i', 'o', 'u']) & (s[i-1] not in ['a', 'e', 'i', 'o', 'u']) & (s[i] not in ['a', 'e', 'i', 'o', 'u']):
            three_flag = 0
            break
        
        if (two_flag == 0) | (three_flag == 0):
            break
            
        
    if (two_flag == 0) | (three_flag == 0) | (mo_flag == 0):
        print("<"+s+"> is not acceptable.")
    
    else:
        print("<"+s+"> is acceptable.")