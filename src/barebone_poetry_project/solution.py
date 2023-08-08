class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottom_left_point, top_right_point):
        self.bl_x = bottom_left_point.x
        self.bl_y = bottom_left_point.y
        self.tr_x = top_right_point.x
        self.tr_y = top_right_point.y

    def overlaps_point(self, point):
        # what if the the point is in the boundaries ?
        if point.x > self.bl_x and point.x < self.tr_x and point.y > self.bl_y and point.y < self.tr_y:
            return True
        else:
            return False
