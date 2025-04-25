def calculated_discount():
    price=int(input("Enter the price: "))
    discount_percentage=int(input("Enter the discount percentage: "))
    
    if discount_percentage==None:
        results= price
        return results
    else:
        discount_price = price * (discount_percentage / 100)
        results=price - discount_price
        return results
    
answer=calculated_discount()
print(answer)