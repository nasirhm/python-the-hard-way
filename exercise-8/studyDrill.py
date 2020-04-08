formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# made a mistake to not add , for each statement
print formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight"
)