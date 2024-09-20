#assigning values to variables
car_color = 'Red'
sales = 1500
price = 2500000.50
is_popular = True

print(car_color)
print(sales)
print(price)
print(is_popular)

#lists and dictionaries
#list
colors = ['Red', 'White', 'Blue', 'Green', 'Black']
print(colors[1])

#dictionary : key-value pair
car_info = {
    "color" : "red",
    "sales" : 1500,
    "price" : 2500000.50
}
print(car_info['color'])

if sales>1000:
    print("High Sales")
else:
    print("Low Sales")
    
#for loop
for color in colors:
    print(color)
    
count = 0
while count < 5:
    print(count)
    count+=1