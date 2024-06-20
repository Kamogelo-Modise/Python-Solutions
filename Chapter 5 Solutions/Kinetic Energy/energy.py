#This program uses functions to calculate kinetics energy

#get_mass function definition
def get_mass():
    mass = float(input("Mass: "))
    return mass

#get_velocity function definition
def get_velocity():
    velocity = float(input("Velocity: "))
    return velocity

#kinetic_energy function definition
def kinetic_energy(m, v):
    energy = (1 / 2) * m * (v**2)
    return energy

#main function definition
def main():
    #get objects mass
    mass = get_mass()
    
    #get objects velocity
    velocity = get_velocity()
    
    #get kinetics energy
    energy = kinetic_energy(mass, velocity)
    
#main function call
main()