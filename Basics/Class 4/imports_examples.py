# Option 1
import main_functions

main_functions.get_action()

# Option 2
import main_functions as fns

fns.get_action()

# Option 3
from main_functions import get_action, greet

greet("Eimantas")
get_action()

# Option 4
from main_functions import *

get_action()
greet()
get_entry_details()
