# bmi calc
# 18.5	Underweight
# 18.5–24.9	Healthy Weight
# 25–29.9	Overweight
# 30–34.9	Obesity Class I
# 35–39.9	Obesity Class II
# ≥40	Obesity Class III severe obesity

weight = input("Please enter your weight in kgs:")
height = input("Please enter our height in m:")

w = float(weight)
h = float(height)

# 10**2 math.pow(h,2) h*h
bmi = w / (h ** 2)

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are healthy")
elif bmi >= 25.0 and bmi <= 29.9:
    print("You are overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("You are obese class 1")
elif bmi >= 35 and bmi <= 39.9:
    print("You are obese class 2")
else:
    print("You are obese class 3")
# git init
# git add .
# git commit -m
# git push
