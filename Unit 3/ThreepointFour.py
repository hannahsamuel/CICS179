# A program that lets the user enter the initial height from which the ball is dropped, the bounciness index, and the
# number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the ball.
# The program outputs the total distance traveled by the ball
# bounciness index = ball height/ ball dropped height
# ball height = index* ball dropped height
height = float(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
number_of_times = int(input("Enter the number of times the ball is allowed to continue bouncing:"))
total = height
bounce_height = 0
while number_of_times > 0:
    total += bounce_height
    bounce_height = index*height
    total += bounce_height
    number_of_times -= 1
    height = bounce_height

print("Total distance traveled is: ", total, "units.")
