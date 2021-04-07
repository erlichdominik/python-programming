import math


class Slope:
    def __init__(self, h):
        self.x_start = 0
        self.y_start = h
        self.x_end = h
        self.y_end = 0
        self.angle = math.radians(45)

    def put_sphere(self, sphere):
        sphere.initialize_object(self, )


class Object:
    def __init__(self, m, dt, r):
        self.m = m
        self.v = 0
        self.g = 10
        self.dt = dt
        self.sx = 0
        self.sy = r
        self.dsx = 0
        self.dv = 0
        self.x_cm_r = 0
        self.y_cm_r = 0
        self.beta = 0
        self.omega = 0
        self.db = 0
        self.do = 0
        self.xp = 0
        self.yp = 0
        self.a = 0
        self.epsilon = 0
        self.k = 0

    def initialize_object(self, slope, calculate_dsx, calculate_dv,
                          calculate_x_cm_r, calculate_y_cm_r, calculate_db,
                          calculate_a, calculate_epsilon, calculate_do,
                          calculate_xp, calculate_yp, calculate_x, calculate_y):
        self.dsx = calculate_dsx()
        self.dv = calculate_dv()
        self.x_cm_r = calculate_x_cm_r()
        self.y_cm_r = calculate_y_cm_r()
        self.db = calculate_db()
        self.a = calculate_a()
        self.epsilon = calculate_epsilon()
        self.do = calculate_do()
        self.xp = calculate_xp()
        self.yp = calculate_yp()






def main():
    slope = Slope(20)
    sphere = Object(1, 0.05, 2)
    slope.put_sphere(sphere)


main()
