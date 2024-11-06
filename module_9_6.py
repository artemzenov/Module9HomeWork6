def all_variants(text):
    
    end = len(text)
    
    for step in range(1, len(text) + 1):
        
        for start in range(0, end):
            
            yield text[start : start+step]
        
        end -= 1


a = all_variants("abcde")

for i in a:
    print(i)
