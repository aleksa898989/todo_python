task_name = input("Name of the task: ")
person_assigned = input("Person: ")
status = input("Status: ")


file = open('todoList.txt', 'a')
file.write("Task Name: " + task_name + "\n" + "Person: " +  person_assigned + "\n" + "Status: "  + status + "\n")
file.close()

print("Data written to file")
