def calculate_love_score(name1, name2):
    name1_name2 = (name1+name2).lower()
    single_digit = 0
    double_digit = 0
    
    for i in str.lower("TRUE"):
        for j in name1_name2:
            if i==j:
                double_digit+=1
    
    for k in str.lower("LOVE"):
        for l in name1_name2:
            if k==l:
                single_digit+=1
    
                
    love_score = (double_digit*10)+single_digit
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")