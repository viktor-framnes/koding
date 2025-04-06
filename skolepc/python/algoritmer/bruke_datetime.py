import datetime as dt
import time 

tid1 = dt.datetime.now()

print(tid1) 

time.sleep(1)

tid2 = dt.datetime.now()

print(tid2)

# Differanse mellom tidene
t_diff = tid2 - tid1
print(t_diff)

# Typene til tidsobjektene
print(f"typen til datetime.now() {type(tid1)}")
print(f"typen til differanse {type(t_diff)}")

print(f"Tidsdifferanse er {t_diff.days} dager og {t_diff.seconds} sekunder og {t_diff.microseconds} mikrosekunder")

# Lage et manuelt tidsobjekt
tid3 = dt.datetime(2006,3,7,1,37)

t_diff2 = tid1 - tid3
print(f"Tidsdifferansen er {t_diff2.days} dager")