from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15, 1.75, 1.80, 1.7]
weight = [165.3, 38.4, 70, 80, 65]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 22.6))