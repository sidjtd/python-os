import os

#1. Open the filenames.txt file with read-only access with the open() function
file_object0 = open('filenames.txt', 'r')
print(file_object0)
file_object0.close()

#2. Print the name of the file and if it is open or closed using the .name and .closed properties

print(file_object0.name)
print(file_object0.closed)

#3. Use a for loop to read all lines of filenames.txt into a list variable
file_object = open('filenames.txt', 'r')
file_list = []

for each in file_object:
  print(each)
  file_list.append(each)


#4. Print out all the lines from the file from your variable
print('blagh', file_list)

#5. Close the filenames.txt file and print if the file is open or closed
file_object.close()
print(file_object.closed)

#6. Create a file using the open() function called secrets.txt
file_secrets = open('secrets.txt', 'w')

#7. Write your own secrets to the file with the write() function
file_secrets.write('Don\'t tell anybody about this... shhhhh!!!!')

#8. Close the secrets.txt file using the close() method. DON'T FORGET!
file_secrets.close()

#9. Print out the contents of the text file in your terminal to prove it worked
file_secrets_check = open('secrets.txt', 'r')
print(file_secrets_check)

file_test = []
for each in file_secrets_check:
  print(each)
  file_test.append(each)

print('confirm this works: ', file_test)

#cat secrets.txt
file_secrets_check.close()

#10. Open your secrets.txt file in append mode and write some more super secret info
file_secret_anew = open('secrets.txt', 'a')
file_secret_anew.write('\nok this is the last straw')

print(file_secret_anew);

#11. Close the secrets.txt file again using the close() function
file_secret_anew.close()

#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function
os.rename('secrets.txt', '.supersecret.txt')

#13. See if you can see the file in your file explorer


#14. Create a list variable named file_names that contains a list of filenames

#15. Use the writelines() function to append the filenames to the filenames.txt file

#16. Delete the initial secrets.txt file now that you have a super secret hidden version

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
