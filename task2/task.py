from io import StringIO
import csv

def read(csvString):
  file = StringIO(csvString)
  reader = csv.reader(file, delimiter=',')
  gr = []
  for row in reader:
     gr.append(row)
  for x in gr:
    for y in x:
      y = int(y)
  return gr

def r1(gr):
  mas = []
  for x in gr:
    if x[0] not in mas:
      mas.append(str(x[0]))
  return mas

def r2(gr):
  mas = []
  for x in gr:
    if x[1] not in mas:
      mas.append(str(x[1]))
  return mas

def r3(gr):
  f, g = gr, gr
  mas = []
  for i in range(len(f)):
    for j in range(len(g)):
      if i != j and f[i][0] not in mas and f[i][1] == g[j][0]:
        mas.append(str(f[i][0]))
  return mas

def r4(gr):
  f, g = gr, gr
  mas = []
  for i in range(len(f)):
    for j in range(len(g)):
      if i != j and f[i][1] not in mas and f[i][0] == g[j][1]:
        mas.append(str(f[i][1]))
  return mas

def r5(gr):
  f, g = gr, gr
  mas = []
  for i in range(len(f)):
    for j in range(len(g)):
      if i != j and f[i][1] not in mas and f[i][0] == g[j][0]:
        mas.append(str(f[i][1]))
  return mas

def task(csvString):
    gr = read(csvString)
    mas1, mas2, mas3, mas4, mas5 = r1(gr), r2(gr), r3(gr), r4(gr), r5(gr)
    return [mas1, mas2, mas3, mas4, mas5]

print(task("1, 2\n 2, 3\n 2, 4\n 3, 5\n 3, 6\n 4, 7"))
