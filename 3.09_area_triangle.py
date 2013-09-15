def area(vertices):
    A = 0.5 * abs(
        vertices[1][0] * vertices[2][1] - # x2, y3
        vertices[2][0] * vertices[1][1] - # x3, y2
        vertices[0][0] * vertices[2][1] + # x1, y3
        vertices[2][0] * vertices[0][1] + # x3, y1  
        vertices[0][0] * vertices[1][0] - # x1, y2
        vertices[1][0] * vertices[0][1]   # x2, y1
        )
    return A

v1 = (0,0); v2 = (1,0); v3 = (1,2);
vertices = [v1, v2, v3]

triangle1 = area(vertices)

print 'Area of triangle is %.2f' % triangle1

"""
$ python 3.09_area_triangle.py 
Area of triangle is 1.00
"""
