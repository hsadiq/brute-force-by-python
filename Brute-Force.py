<pre><code> password = input("pass:") #idea = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"," "] #THE IDEA ABOVE IS THE FULL A-Z, 0-9 (takes ages) password = input("pass:") idea = ["a","b","c","d"] awnser = [""] *6 var = 0 var1 = 0 var2 = 0 var3 = 0 char = 0
while awnser != password:
awnser = idea[var]
print(awnser)
if var != len(idea):
var += 1 if var == len(idea): var = 0
while awnser != password:
awnser = idea[var]+idea[var1]
print(awnser)
if var != len(idea): var += 1 if var == len(idea):
if var1 != len(idea): var = 0 var1 += 1
if var1 == len(idea): var = 0 var1 = 0
while awnser != password:
awnser = idea[var]+idea[var1]+idea[var2]
print(awnser)
if var != len(idea):
var += 1
if var == len(idea):
if var1 != len(idea):
var = 0
var1 += 1
if var1 == len(idea):
if var2 != len(idea):
var = 0
var1 = 0
var2 += 1
if var2 == len(idea):
var = 0
var1 = 0
var2 = 0
while awnser != password:
awnser = idea[var]+idea[var1]+idea[var2]+idea[var3]
print(awnser)
if var != len(idea):
var += 1
if var == len(idea):
if var1 != len(idea):
var = 0
var1 += 1
if var1 == len(idea):
if var2 != len(idea):
var = 0
var1 = 0
var2 += 1
if var2 == len(idea):
print("==============================================")
print("Password too long or characters not in string!") print("==============================================") break print("==================") print("") input("Password = "+awnser) <</code> & lt;/pre>
