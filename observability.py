def agent(steps):
    log = []

    for step in steps:
        log.append(step)

    return log


steps = ["Observe", "Decide", "Act"]

result = agent(steps)

print("Full Log:")
for item in result:
    print(item)