import random



class Ant():
    def __init__(self, pos: int, direction: bool):
        self.pos = pos
        self.direction = direction
    def move(self):
        if self.direction:
            self.pos += 1
        else:
            self.pos -= 1
    def get_pos(self):
        return self.pos

    def get_dir(self):
        return self.direction

    def map_dir(self):
        if self.direction == True:
            return "forward"
        else:
            return "backward"

    def collision(self):
        self.direction = not self.direction

    def __str__(self):
        return f'Ant at:{self.pos} going {self.map_dir()}'
    def __repr__(self):
        return f'Ant at:{self.pos} going {self.map_dir()}'
    def __lt__(self, other):
        return self.pos < other.pos



class Stick():
    def __init__(self, n):
        self.steps = []
        self.n = n
    def pop_stick(self, ant: Ant):
        self.steps.pop(ant)

    def __str__(self):
        return f'Stick :{self.steps}'
    def get_step(self, i: int):
        return self.steps[i]
    def set_step(self, step: Ant):
        self.steps.append(step)
    def step_refresh(self,):
        self.steps = sorted(self.steps)
    def ant_setup(self):
        if self.n < 1 or self.n > 100:
            raise Exception('Need at least 1 ant, but no more than 100 ants')
        random_pos = random.sample(range(0, 101), self.n)
        for i in random_pos:
            self.set_step(Ant(i, bool(random.randint(0, 1))))

        self.step_refresh()


    def simulate(self):
        to_pop = []
        tick = 0
        print(f"start: {self.steps}")
        if not self.steps:
            raise Exception('No ants on the stick')
        while self.steps:
            for ant in range(len(self.steps)):

                try:
                    if self.steps[ant].get_dir() and self.steps[ant].get_pos() + 1 == self.steps[ant + 1].get_pos():
                        self.steps[ant].collision()
                        self.steps[ant + 1].collision()

                    elif self.steps[ant].get_dir():
                        self.steps[ant].move()
                        if self.steps[ant].get_pos() <= 0 or self.steps[ant + 1].get_pos() > 100:
                            to_pop.append(ant)

                except IndexError:
                    self.steps[ant].move()
                    if self.steps[ant].get_pos() <= 0 or self.steps[ant].get_pos() > 100:
                        to_pop.append(ant)

                        continue

                try:
                    if not self.steps[ant].get_dir() and self.steps[ant].get_pos() - 1 == self.steps[ant - 1].get_pos():
                        self.steps[ant].collision()
                        self.steps[ant - 1].collision()

                    elif not self.steps[ant].get_dir():
                        self.steps[ant].move()
                        if self.steps[ant].get_pos() <= 0 or self.steps[ant].get_pos() > 100:
                            to_pop.append(ant)


                except IndexError:
                    self.steps[ant].move()
                    if self.steps[ant].get_pos() <= 0 or self.steps[ant].get_pos() > 100:
                        to_pop.append(ant)



                self.step_refresh()

            tick += 1

            if len(to_pop) > 1:
                a = to_pop[0]
                b = to_pop[1]
                self.pop_stick(b)
                self.pop_stick(a)
                to_pop = []
                self.step_refresh()
            elif len(to_pop) == 1:
                a = to_pop[0]
                self.pop_stick(a)
                to_pop = []
                self.step_refresh()
            print(self.steps)
        return tick



if __name__ == '__main__':
    stick = Stick(23)
    stick.ant_setup()
    ticks = stick.simulate()
    print(ticks)