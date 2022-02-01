# Orange Background
Polygon(0, 0, 180, 0, 0, 180, fill=RGB(250, 153, 22))
Line(0, 170, 170, 0)

# Blue Background
Polygon(180, 0, 150, 30, 250, 80, 285, 25, 275, 0, fill=RGB(64, 72, 132))
Line(156, 25, 254, 74)

# Red Background
Polygon(275, 0, 285, 25, 344, 170, 400, 180, 400, 0, fill=RGB(193, 56, 38))
Line(283, 0, 351, 166)
Line(351, 166, 400, 175)

# Black Background
Polygon(285, 25, 231, 110, 308, 118, 310, 87)

# Brown Background
Polygon(0, 180, 0, 200, 210, 190, 180, 120, 238, 100, 251, 80, 151, 29, fill=RGB(89, 53, 27))

# Purple Background
Polygon(231, 110, 238, 100, 180, 120, 200, 190, 290, 290, 372, 175, 344, 170, 310, 87, 308, 118, fill=RGB(32, 37, 75), border='black')

# Blue Background (2)
Polygon(290, 290, 333, 337, 400, 327, 400, 180, 372, 175, fill=RGB(64, 72, 137))

# Blue Background (3)
Polygon(0, 345, 40, 310, 90, 400, 0, 400, fill=RGB(64, 72, 132))

# Orange Background (2)
Polygon(90, 400, 135, 400, 228, 222, 200, 190, 83, 196, 63, 352, fill=RGB(200, 124, 39), border='black')

# Red/Orange Background
Polygon(135, 400, 228, 222, 333, 337, 370, 400, fill=RGB(211, 89, 35))

# Black Backrgound (2)
Polygon(0, 200, 0, 345, 40, 310, 63, 352, 165, 365, 83, 196)

# Yellow Background
Polygon(333, 337, 370, 400, 400, 400, 400, 327, fill=RGB(244, 198, 1))
Line(333, 337, 370, 400)

# Neck + Frets
Polygon(44, 95, 61, 78, 200, 202, 182, 220, fill=RGB(28, 42, 102), border='black', borderWidth=3)
Line(74, 121, 89, 104, fill="lightBlue", lineWidth=4)
Line(94, 138, 107, 123, fill="lightBlue", lineWidth=4)
Line(114, 157, 128, 142, fill="lightBlue", lineWidth=4)
Line(136, 176, 150, 160, fill="lightBlue", lineWidth=4)
Line(157, 196, 172, 180, fill="lightBlue", lineWidth=4)

# Head
Polygon(7, 70, 41, 102, 65, 75, 30, 46, fill=RGB(28, 42, 102), border='black')
Polygon(20, 69, 39, 91, 44, 83, fill='red')
Polygon(33, 60, 49, 80, 55, 75, fill='red')

# Body
Oval(216, 233, 100, 90, rotateAngle=(-40), fill=RGB(200, 170, 99), border='black')
Oval(278, 291, 150, 130, rotateAngle=(-40), fill=RGB(200, 170, 99), border='black')
Arc(278, 291, 150, 130, -30, 90, rotateAngle=(-40), fill=RGB(244, 198, 1), border='black')
Arc(216, 233, 100, 90, 60, 100, rotateAngle=(-40), fill=RGB(89, 53, 27), border='black')
Arc(216, 233, 100, 90, 230, 100, rotateAngle=(-40), fill=RGB(64, 72, 132), border='black')
Arc(278, 291, 150, 130, 180, 110, rotateAngle=(-40), fill=RGB(193, 56, 38), border='black')
Arc(278, 291, 150, 130, 90, 60, rotateAngle=(-40), border='black')
Circle(280, 295, 20, border='black', fill='gray')