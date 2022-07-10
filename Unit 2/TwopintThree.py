# Calculates the cost to rent videos and VHS tapes from Five Star Retro Video rents
new_videos = int(input("Enter the number of new videos: "))
oldies = int(input("Enter the number of oldies: "))
cost_of_new_videos = new_videos*3.0
cost_of_oldies = oldies*2.0
print("The total cost is $", cost_of_new_videos + cost_of_oldies)