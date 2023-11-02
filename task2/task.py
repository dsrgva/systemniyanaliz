import csv
from io import StringIO

def task(csv_string):
    reader = csv.reader(StringIO(csv_string))
    con = {}

    for row in reader:
        n1, n2 = row
        con.setdefault(n1, [])
        con.setdefault(n2, [])

        con[n1].append(n2)

    con = {k: v for k, v in sorted(con.items())}
    res = {i: {"r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0} for i in con}

    def q(node):
        count = len(con[node]) + 1
        for n in con[node]:
            res[n]["r4"] += 1
            count += q(n) - 1
        return count

    for i in con:
            node_connections = con[i]
            res[i]["r1"] += len(node_connections)
            for n in node_connections:
                res[n]["r2"] += 1
                res[n]["r5"] += len(node_connections) - 1
            res[i]["r3"] = q(i) - res[i]["r1"] - 1
            res[i]["r4"] -= res[i]["r2"]

    finding = []
    
    for x in res:
        num = res[x]
        finding = [[num["r1"], num["r2"], num["r3"], num["r4"], num["r5"]] for num in res.values()]

    return "\n".join([",".join([str(elem) for elem in row]) for row in finding])

csv_string = "1,2\n2,3\n2,4\n3,5\n3,6"
print(task(csv_string))
