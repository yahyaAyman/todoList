from stack import *

class ToDoList:

    def __init__(self):
        self.tasks = []
        self._size = 0
        self._deleted_tasks = []
        self.stack = Stack()
        

    # ADD IN METHODS HERE ACCORDING TO INSTRUCTIONS #
    def add_task(self, task_name: str, index = None)-> None:
        """
        Adds and creates a new task to the self.task and the new task is added
        to the end of the list
        """
        if index == None:
            self.tasks.append(task_name)
            self._size += 1
        elif index != None:
            self.tasks.insert(index, task_name)
            self._size += 1
        

    def delete_task(self, index: int)-> None:
        """ Deletes a certain task at a certain index in the self.task list"""
        if len(self.tasks) == 0:
            print("There are no tasks to delete. Please add tasks to your task list first!")
        
        self._deleted_tasks.append((index, self.tasks.pop(index)))
        self._size = self._size - 1
        
    def __len__(self):
        """Returns the number of tasks in the self.task list ie, length of the list containing the tasks"""
        return self._size

    def redo(self):
        """Redoes what the undo method does """
        if self.stack.size() == 0:
            print("Nothing has been undone to redo! Please undo something in order to be able to redo!")
        else:
            if self.stack.size() > 0:
                self._size += 1
                to_do = self.stack.pop()
                index = to_do[0]
                task = to_do[1]
                self.tasks.insert(index, task)
                self.delete_task(index+1)
            elif len(self._delted_tasks) > 0:
                
                self.undo
                
                
            
            
    

    def undo(self):
        """
        undoes what the delete task method does
        """
        check = True
        print('1', self.tasks)
        if len(self._deleted_tasks) > 0:
            self._size += 1
            current = self._deleted_tasks.pop()
            self.tasks.insert(current[0], current[1] )
            self.stack.push(current)
            print('2', self.tasks)
            if len(self._deleted_tasks) == 0:
                check = False
        elif len(self.tasks) > 0 and check == True:
            index_undone = self._size
            self._size = self._size - 1
            current = (index_undone, self.tasks.pop())
            self.stack.push(current)
            self._deleted_tasks.append((current[0], current[1]))
            print('3', self.tasks)
            if len(self._deleted_tasks) == 0:
                check = True
        elif len(self._deleted_tasks) == 0 or len(self.tasks) == 0:
            print("You can not undo, nothing has been removed from your task list!")
        else:
            pass

    def __repr__(self) -> str:
        counter = 1
        if len(self.tasks) == 0:
            return("There are no tasks to view. Please add tasks to your To Do List first.")
        for i in range (self._size - 1):
            print (str(counter) + ": " + self.tasks[i])
            counter += 1
        return (str(counter) + ": " + self.tasks[self._size - 1])

##            counter = 0
##            for i in range(len(self.tasks)):
##                counter += 1
##                print(str(counter) + ': ' + self.tasks[i])
            

                
commands = Stack()
#Notes for us#
## The command is a stack that keeps track of the commands that is given by the user##
todolist = ToDoList()

print("Welcome to your temporary To Do List")
print("-------------------------------------")
print("At any point, you may type: \n" \
            "'v' to view whole list \n" \
            "'d' to delete an existing item \n" \
            "'u' to undo what you just added, \n"
            "'r' to redo what you previously undid)")
print("-------------------------------------")

counter = 0
while True:
    c = input("What is something you need to get done? \n")
    if (c == 'v'):
        print(todolist)
    elif (c == 'd'):
        # MODIFY THIS ACCORDING TO INSTRUCTIONS #
        num = int(input("Delete which task "))
        new_num = num - 1
        try :
            todolist.delete_task(new_num)
        except IndexError:
            while new_num > len(todolist) or new_num < 0:
                print(("The index at ") + str(num) + (" is invalid, please try again!"))
                num = int(input("What task do you want to delete?"))
                new_num = num - 1
        print(todolist)
    elif (c == 'u'):
        todolist.undo()            
        
        # YOUR CODE HERE #
    elif (c == 'r'):
        todolist.redo()
    else:
        todolist.add_task(c)
        commands.push(('insert', c, len(todolist)-1))
        redos = Stack()


### What is the difference between undo and redo?
### What are the restrictions to undo?
### What are the restrictions to redo?
