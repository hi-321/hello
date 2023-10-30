import pandas as pd
def y_in(x, w, b):
    sum = 0
    for i in range(len(w)):
        sum += x[i] * w[i]
    sum += b
    return sum

def update_weights(a, t, x, w, b):
    for i in range(len(w)):
        w[i] += a * t * x[i]
    b += a * t
    return (w, b)


r = 4
c = 3
data = []
for i in range(0, r):
    a = []
    print("Enter row " + str(i + 1))
    for j in range(0, c):
        temp = int(input())
        a.append(temp)
    data.append(a)
df = pd.DataFrame(data, columns=['X1', 'X2', 'T'])
print(df.to_string(index=False))



target = df.iloc[:, -1].tolist()
if -1 in target:
    activation = 1  # step-fn
else:
    activation = 0  # threshold fn
theta = float(input("Enter threshold:"))
alpha = float(input("Enter learning rate:"))
epochs = int(input("Enter no. of epochs:"))
w1=int(input("Enter the Initial Weight(w1):"))
w2=int(input("Enter the Initial Weight(w2):"))
bias=int(input("Enter the Initial Bias:"))
weights = []
weights.append(w1)
weights.append(w2)
for i in range(epochs):
    print("\nEpoch ", i + 1)
    count = 0
    list3 = []
    for j in range(r):
        yin = y_in(df.iloc[j].tolist(), weights, bias)
        if activation == 0:
            y = 1 if yin >= theta else 0
        else:
             y = 1 if yin >= theta else -1
        if target[j] != y:
            count += 1
            updated_vals = update_weights(alpha, target[j], df.iloc[j].tolist(), weights, bias)
            weights, bias = updated_vals[0], updated_vals[1]

        list2 = []
        list1 = []
        l2 = df.iloc[j].tolist()
        for n in range(len(l2)):
            list1.append(l2[n])
        list1.append(yin)
        list1.append(y)
        for n in range(len(weights)):
            list1.append(weights[n])
        list1.append(bias)
        list2.append(list1)
        df2 = pd.DataFrame(list2, columns=['X1', 'X2', 'T', 'Yin', 'Y', 'W1', 'W2', 'B'])
        list3.append(df2.iloc[0].tolist())
    df3 = pd.DataFrame(list3, columns=['X1', 'X2', 'T', 'Yin', 'Y', 'W1', 'W2', 'B'])
    print(df3.to_string(index=False))
    if count == 0:
        print("\nConverged Successfully")
        break
