def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    counter = 0
    
    if year%4==0:
        counter+=1 
    if year%100!=0:
        counter+=1
    if year%400==0:
        counter+=1 
        
    if counter>=2:
        return True
    else:
        return False       