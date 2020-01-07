def is_triangle(a,b,c):
    """Takes three integer lengths a, b, c and prints "Yes" or "No"
    depending on whether it is possible to draw a triangle with those
    as side lengths.
    """
    if a+b<c or a+c<b or b+c<a:
        print("No")
    else:
        print("Yes")

def is_triangle_integer(a,b,c):
    """Decides whether it is possible to draw a triangle with side lengths
    being the integer parts of a, b and c.
    """
    #Question: Why bother making this function which depends on the integer
    #parts of the numbers.  That has nothing to do with whether a triangle
    #can be formed with sides of length a, b, c.
    
    is_triangle(int(a),int(b),int(c))

is_triangle(1,1,3)
is_triangle(1,3,1)
is_triangle(3,1,1)
is_triangle(1.8,1.8,3.5)
is_triangle_integer(1.8,1.8,3.5)
