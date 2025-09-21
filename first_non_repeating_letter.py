def first_non_repeating_letter(s):
    s_lower = s.lower()
    for i,letter in enumerate(s_lower):
       if s_lower.count(letter) == 1:
            return s[i]
    return ""
        
  
  
print(first_non_repeating_letter("~><#~><"))