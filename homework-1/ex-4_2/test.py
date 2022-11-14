import main

for i in range(10000):
    if i%100 == 0:
        print(i)

    a = main.find_pattern_in_grid(main.rng, (6,6), 5)
    if a:
        print(a)

print("Finished")