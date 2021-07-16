# name = "SonuKashyap"
# height_m= 2
# weight_kg= 90

# bmi = weight_kg/(height_m **2)
# print("bmi: ")
# print(bmi)
# if bmi<25:
#     print(name)
#     print("is not overweight")
# else:
#     print(name)
#     print("is overweight")
name1 = "sonu"
height_m1=2
weight_kg1=80


def bmi_calculator(name,height_m,weight_kg):
    bmi = weight_kg/(height_m **2)
    print("bmi: ")
    print(bmi)
    if bmi<25:
        return name + "not overweight"
    else:
        return name + "is overweight"
    
result =bmi_calculator(name1,height_m1,weight_kg1)
    
print(result)

    