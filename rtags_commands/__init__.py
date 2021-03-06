"""RTags functionality commands

follow_location: navigates to the definition of symbol under cursor
find_references: presents output panel of all references to symbol under cursor
find_references_virtual_methods:
    presents output panel of all overrides of virtual method under cursor
load_compile_commands: Finds and loads the compile_commands.json file into rdm
"""
__all__ = [
    "follow_location",
    "find_references",
    "find_references_virtual_methods"
    "load_compile_commands"]
