#koitan saada tuple listan indexin etsimisen toimimaan. Moduuli7teht3

example = [(1,4,0), (300,13,2),(240,4,11)]

keijo = 240
print(next((i for i, elem in enumerate(example) if elem[0] == keijo), -1))