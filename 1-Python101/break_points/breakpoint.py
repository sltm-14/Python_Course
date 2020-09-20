import pdb

print("\nBEFORE FIRST BREAKPOINT\n")

pdb.set_trace()
print("AFTER FIRST BREAKPOINT")

# You can continue running without the debugger using the "continue" command.

pdb.set_trace()
print("AFTER SECOND BREAKPOINT")
