# See Break Statement
name = "Alexander"
for i in name:
    print(i)
    if i == 'x':
        break

# See Break Statement within for loop
languageName = ["Java", "Python", "PHP", "C", "Ruby", "Go"]
for l in range(len(languageName)):
    print(languageName[l])
    if languageName[l] == "C":
        print("Hey I found \"C\" and break the loop")
        break

# See Continue Statement within for loop
languageName2 = ["Java", "Python", "PHP", "C", "Ruby", "Go"]
for l in range(len(languageName2)):
    print(languageName2[l])
    if languageName2[l] == "C":
        print("Hey I found \"C\" but not break the loop")
        continue
