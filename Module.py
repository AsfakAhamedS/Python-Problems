
import ModuleFunction
print(ModuleFunction.name1())

import ModuleFunction as mF
print(mF.name2())

from ModuleFunction import name3
print(name3())

from ModuleFunction import *
print(name1())
print(name2())
print(name3())

print(dir(ModuleFunction))