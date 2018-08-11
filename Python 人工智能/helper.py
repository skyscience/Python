def get_boundary_line(w1, w2, b):
    p1x = float(-b / w1)
    p2y = float(-b / w2)

    return([p1x, 0], [0, p2y])

if __name__ == '__main__':
    print(get_boundary_line(-0.411, -0.223, 0.302))