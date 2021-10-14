#asing for input
name = str(input("what is your name"))
task = int(input("hello, " + name + " how many task are you going to be doing today?(enter numbers please)"))
todo = []
#looping input here
for i in range(0, task):
    num1 = input("what are your task to do " + name)
    todo.append(num1)
donecount = 0
while donecount < task:
    print("task are " + str(todo))
    done = input( "which task have you done" )
    # stores the done task
    other = []

    # using here to remove task when done
    if done in todo:
        donein = int(todo.index(done))
        todo.pop(donein)
        other.append(done)
        print("you still have " + str(todo) + name)
        print("task you have done are:" + str(other))
        donecount = donecount + 1
    else:
        print("This is not a task ")

print("good job you have done all your task!")