def project_to_distance(point_x, point_y, distance):
    import math


    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print (round(point_x * scale, 4), round(point_y * scale, 4))

project_to_distance(2, 7, 4)