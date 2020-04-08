formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight"
)

# Still a mystery why the first 2 string reponds with '' and the last one as ""