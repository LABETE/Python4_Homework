import inspect
import ____ as mod    # Insert the name of a module instead of ____

print("Functions at the module level:\n")
lst_func_mod = inspect.getmembers(mod, inspect.isfunction)
lst_func_classes = inspect.getmembers(mod, inspect.isclass)

for tup_func in lst_func_mod:
    print("Function name:", tup_func[1].__name__)
    print("args:", inspect.formatargspec(*inspect.getfullargspec(tup_func[1])))
    
for tup in lst_func_classes:
    class_name = tup[1].__name__
    print("\nFunctions in the class:", class_name, "\n")
    mod_with_class = getattr(mod, class_name)
    lst_class = inspect.getmembers(mod_with_class, inspect.isfunction)
    for tup_class_func in lst_class:
        print("Function name:", tup_class_func[1].__name__)
        print("args:", inspect.formatargspec(*inspect.getfullargspec(tup_class_func[1])))
    

    
