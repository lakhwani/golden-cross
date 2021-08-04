closing_sum_200 = 0

with open('data/SPY.csv') as file:
    content = file.readlines()[-200:]
    for line in content:
        print(line)
        parsed = line.split(",")
        closing = parsed[4]
        closing_sum_200 += float(closing)

ma_200 = closing_sum_200 / 200
print(ma_200)