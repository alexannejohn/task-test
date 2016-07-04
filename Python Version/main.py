# Todo: Alter the complete_tasks method so that it only calls 'complete' on
#           non-completed task.
#       Add a remove_task method that removes only one task by id
#
#       Upon calling complete() on a task, set _value of that task object to the number of occurrences of the
#           string "CCN" (case in-sensitive) that appears in the task's name.
#
#       Fix the Task object id, so that it is unique for each new task.
#       Fix other bugs.

# Note: - You cannot edit/change the TaskManager class directly. Think of it as a 3rd party library
#       - You can create new objects, etc

from task_manager import  Task, TaskManager

if __name__ == "__main__":
    task_manager = TaskManager()
    first_task = Task('!!nZ@xr>492CCN;SDRC2#6CcN_$5UcCNq]*m44AhW`')
    second_task = Task('g}~x?C*n9K|LccN_YEL@<=44jkc.dB-v{!#;7*[[')
    third_task = Task('ekCcN,h9=!B46)j6acCN;`n68M+2ZR2CCn^:CUw')

    task_manager.import_task(first_task)
    task_manager.import_task(second_task)
    task_manager.import_task(third_task)

    task_manager.complete_tasks()

    last_task = Task('>.`8tCcn{xsS3sa!G@{cCn(w},U+s)**sACc]NAn#')
    task_manager.import_task(last_task)
    task_manager.complete_tasks()

    task_manager.remove_tasks()
