def manage_stage_changes(changes):
    cancelled = []
    scheduled = []
    for change in changes:
        if change != 'Cancel' and change != 'Reschedule':
            scheduled.append(change[9])
        elif change == 'Cancel':
            recently_cancelled = scheduled.pop()
            cancelled.append(recently_cancelled)
        elif change == 'Reschedule':
            scheduled.append(cancelled.pop())
    return scheduled   

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# ["A", "C", "B", "D"]
# []
# ["Z"]

# Understand
    # Schedule = push on stack
    # Cancel = pop from stack
    # reschedule = push most recently canceled on to stack
    # return stack