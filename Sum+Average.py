def summation(N,M): #หาผลรวม
  sum = 0 #ตัวแปรตั้งต้น = 0
  for i in range(N,M+1): #ผลรวม N ถึง M
    sum += i #รวมค่าผลรวม
  return sum

N = int(input("ค่า N : "))
M = int(input("ค่า M : "))

sum = summation(N,M) #แสดงผลรวม
print("ผลรวม :",sum)

def average(N,M): #หาค่าเฉลี่ย
  avg = sum / (M-N+1) #ค่าผลรวม / จำนวนทั้งหมด
  return avg

avg = average(N,M) #แสดงค่าเฉลี่ย
print("ค่าเฉลี่ย :",avg)
