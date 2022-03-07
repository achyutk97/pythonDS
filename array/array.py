# Exercise: Array DataStructure

# A. Let us say your expense for every month are listed below, January - 2200 February - 2350 March - 2600 April - 2130 May - 2190 Create a list to store these monthly expenses and using that find out,

# In Feb, how many dollars you spent extra compare to January?
# Find out your total expense in first quarter (first three months) of the year.
# Find out if you spent exactly 2000 dollars in any month
# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on thi

month = ["January", "February", "March", "April", "May"]
month_expansion = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(month_expansion[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print(sum(month_expansion[:3]))

# 3. Find out if you spent exactly 2000 dollars in any month
for i in month_expansion:
  if i == 2000:
    print("spent exactly 2000 dollars in", month[month_expansion.index(i)])
    break
else:
  print("Not Found")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
month.append("June")
month_expansion.append(1980)
print(month_expansion)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
for i in month:
  if i == "April":
    month_expansion[month.index(i)] -= 200
    print(month_expansion)

# B. You have a list of your favourite marvel super heros. heros=['spider man','thor','hulk','iron man','captain america'] Using this find out,

# Length of the list
# Add 'black panther' at the end of this list
# You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
# Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
print("Length of the list", len(heros))
heros.append('black panther')
print("after adding black panther list is", heros)
heros.pop()
print("Deleting black panther from list is", heros)
heros.insert(3, "black panther")
print("add 'black panther' after 'hulk now list is ", heros)
heros[1:3] = ["doctor strange"]
print(heros)
heros.sort()
print(heros)

# C. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
n = int(input("Enter number of element you want to enter:-"))
print([i for i in range(1, n) if i%2 != 0])

