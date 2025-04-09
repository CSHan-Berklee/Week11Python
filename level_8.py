running = True
if running == True:
    x = input ('What happens when no prompt is given to the input function?') 
    if x == "nothing":
        print("you are correct, next question")
    else:
        print("you are wrong, think about it again")
        running = False
    y = input ('is it possible to pass a varialbe into the function instead of a string')
    if y == "No":
        print("you are correct, congratulation")
    elif y != "No":
        print("you are wrong")