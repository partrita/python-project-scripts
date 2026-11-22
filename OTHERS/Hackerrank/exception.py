list_a = [1,2,3,4,5]

try:
    index = int(input("Enter the index: "))
    
    try:
        print(list_a[index])     
    except IndexError:
        print(f"The index {index} is incorrect and index should lie between -5 and 4")

except ValueError:
    print("Use an integer as an input") 