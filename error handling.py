def agent(action):
    valid_actions = ["move", "stop", "wait"]

    if action in valid_actions:
        return {"status": "success", "action": action}
    else:
        return {"status": "error", "message": "Invalid action"}


print(agent("move"))
print(agent("jump"))