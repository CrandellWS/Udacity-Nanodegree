import parent
import child

dad = parent.Parent("Hill", "Brown")
print(dad.last_name)


son = child.Child(dad, 12321)
print(son.last_name)
