import parent
import child

dad = parent.Parent("Hill", "Brown")
print(dad.last_name)


son = child.Child(dad)
print(son.last_name)
