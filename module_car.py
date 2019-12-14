class Car:

    def __init__(self,name,start_v,mass,power,coefficient_of_resistance,frontal_surface):
        self.name = name
        self.velocity = start_v
        self.mass = mass
        self.power = power*740 #KM na kW
        self.distance = 0
        self.coefficient_of_resistance = coefficient_of_resistance #wspolczynnik oporu
        self.frontal_surface = frontal_surface # powierzchnia czołowa pojazdu

    def move(self,slope,friction):
        self.velocity_change(slope,friction)
        self.distance += self.velocity*0.01 #tymczasowe rozwiazanie

    def velocity_change(self,slope,friction):
        self.velocity += (self.power-slope*self.mass*9.81-friction*self.mass*(1-slope**2)-1.293*0.5*self.frontal_surface*(self.velocity**2)*self.coefficient_of_resistance)*0.01 #tymczasowe rozwiazanie
        if self.velocity <=0:
            self.velocity = 0
            print("SAMOCHOD SIE ZATRZYMAL!",self.name)
            
            
