class LP:
    def __init__(self, x, y, xsize, ysize, lp):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.xsize = xsize
        self.ysize = ysize
        self.steps = 0
        self.xmotion = []
        self.ymotion = []
        self.lp = {lp: 1}

    def step(self, x, y, xsize, ysize):
        if (self.steps < 15):
            self.xmotion.append(x - self.x)
            self.ymotion.append(y - self.y)
            self.steps += 1

        else:
            self.xmotion.pop(0)
            self.xmotion.append(x - self.x)
            self.ymotion.pop(0)
            self.ymotion.append(y - self.y)

        self.velx = sum(self.xmotion) / self.steps
        self.vely = sum(self.ymotion) / self.steps
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize

    def nextstep(self):
        x = self.x + self.velx
        y = self.y + self.vely
        self.x = x
        self.y = y
        if self.steps < 3:
          self.x = -1
          self.y = -1

        return self.x, self.y, (self.xsize, self.ysize)

    def distanceTo(self, x, y):
        dist = (self.x - x)**2 + (self.y - y)**2
        return(dist)

    def add(self, plate):
        if plate in self.lp: self.lp[plate] += 1
        else: self.lp[plate] = 1

