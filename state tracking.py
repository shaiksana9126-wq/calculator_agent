state = {
"done": False,
"steps": 0
}

for i in range(3):
state["steps"] += 1
print("Step:", state["steps"])

state["done"] = True

print("State:", state)