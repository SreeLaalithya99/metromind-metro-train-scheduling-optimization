import pulp

trains = ["Train_A","Train_B","Train_C"]
slots = ["Slot1","Slot2","Slot3"]

model = pulp.LpProblem("TrainScheduling", pulp.LpMaximize)

x = pulp.LpVariable.dicts("schedule",
                          [(t,s) for t in trains for s in slots],
                          cat="Binary")

model += pulp.lpSum(x[t,s] for t in trains for s in slots)

for t in trains:
    model += pulp.lpSum(x[t,s] for s in slots) <= 1

for s in slots:
    model += pulp.lpSum(x[t,s] for t in trains) <= 1

model.solve()

print("Schedule:")
for t in trains:
    for s in slots:
        if x[t,s].value()==1:
            print(t,"->",s)
