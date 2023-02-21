def kinetic_energy(mass, speed):
    return 1 / 2 * mass * (speed ** 2)


mass = int(input('Specify body weight: '))
speed = int(input('Specify the speed of the body: '))

print(f'Kinetik energy of the body is {kinetic_energy(mass, speed)}')
