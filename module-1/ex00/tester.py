from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15, 1.8, 1.8]
weight = [165.3, 38.4, 65, 67.9]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))
