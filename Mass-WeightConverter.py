mass = float(input("Enter the mass of the object (in kg): "))
weight = mass * 9.8

print(f"The weight of the object is {weight:.2f} newtons.")

if weight > 500:
    print("The object is too heavy.")
elif weight < 100:
    print("The object is too light.")