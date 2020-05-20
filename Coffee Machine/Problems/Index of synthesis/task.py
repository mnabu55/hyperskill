number = float(input())

if number < 2:
    print("Analytic")
elif 2 <= number <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
