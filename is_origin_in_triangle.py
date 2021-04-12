import math

def is_origin_in_triangle(x1,y1,x2,y2,x3,y3):
    area_12= calc_triangle_area(x1,y1,x2,y2,0,0)
    area_13= calc_triangle_area(x1,y1,x3,y3,0,0)
    area_23 = calc_triangle_area(x2,y2,x3,y3,0,0)
    sum_triangles_area = area_12+area_23+area_13
    tot_area = calc_triangle_area(x1,y1,x2,y2,x3,y3)
    if tot_area== sum_triangles_area:
        print("True")
        return True
    else:
        print("False")
        return False



def calc_triangle_area(x0, y0, x1, y1, x2, y2):
    base=math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
    dist = (abs((x2-x1)*(y1-y0)-1*(x1-x0)*(y2-y1)))/base
    area = (base*dist)/2
    return area




is_origin_in_triangle(1, 1, -1, -1, 1, -1)
is_origin_in_triangle(3, 3, 1, 1, 3, 1)
is_origin_in_triangle(-2,2,2,-1,2,2)
is_origin_in_triangle(1,1,2,2,7,6)





