def decision_tree(weather, temperature):
    if weather == "sunny":
        if temperature > 30:
            return "Play inside"
        else:
            return "Play outside"
    else:
        return "Stay home"
weather = input("Enter weather (sunny/rainy): ").lower()
temperature = int(input("Enter temperature in °C: "))

decision = decision_tree(weather, temperature)
print("Decision Tree Output:", decision)
