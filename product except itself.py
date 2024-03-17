def product(lst):
    n = len(lst)
    left_products = [1] * n  
    right_products = [1] * n 
    result = [1] * n
    
    for i in range(1,n):
        left_products[i] = left_products[i-1] * lst[i-1]
        
    for i in range(n-2,-1,-1):
        right_products[i] = right_products[i+1] * lst[i+1]
    
    for i in range(n):
        result[i] = left_products[i] * right_products[i]
     
    return result

lst = [1, 2, 3, 4]
print(product(lst))

time complexity : O(n)
space complexity : O(n)

# ============================================================================
def product(lst):
    n = len(lst)
    result = [1] * n
    
    left_product = 1
    for i in range(n):
        result[i] = result[i] * left_product
        left_product *= lst[i]
        
    right_product = 1 
    for i in range(n-1,-1,-1):
        result[i] = result[i] * right_product
        right_product *= lst[i]
     
    return result

lst = [1, 2, 3, 4]
print(product(lst))

time complexity = O(n)
space complexity = O(1)
