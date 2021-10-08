people = ["players", "haters", "heart-breakers", "fakers"]
actions = ["play", "hate", "break", "fake"]

for index, person in enumerate(people):
    print(people[index], "gonna", (actions[index] + " ") * 5)
