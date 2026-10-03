def agent(temperature):
    if temperature > 100:
        return "success"
    else:
        return "failure"


temperatures = [80, 101, 120]

for temp in temperatures:
    state = agent(temp)
    print("Temperature:", temp)
    print("State:", state)
    print("-" * 30)