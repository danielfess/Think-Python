import turtle

def draw(t,length,n):
    """Draw a tree with n levels, where at each split there are two branches.
    length = length of the smallest branch, with previous branches growing
    linearly in size.  t: turtle.
    """
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)

if __name__ == '__main__':
	bob = turtle.Turtle()
	draw(bob,20,5)
	turtle.mainloop()