import module_car as car

meta = 1000 #dystans wyscigu
slope = 0.1 #nachylenie
friction = 0.5 #tarcie

car1 = car.Car("KIA",30,1000,10,0.3,2.5)
car2 = car.Car("SKODA",40,800,13,0.3,2.2)

while car1.distance<meta and car2.distance<meta:
    print("PREDKOSC 1:",car1.velocity)
    print("PREDKOSC 2:",car2.velocity)
    car1.move(slope,friction)
    car2.move(slope,friction)

print("DISTANCE:",car1.distance, car2.distance)
print("PREDKOSC:",car1.velocity, car2.velocity)