database = input(f'\nEnter the name of the database you want to create: ')
environment = input(f'\nEnter the name of the environment (DTAP) you want to create: ')

# Composing the code

line1 = ('CREATE ROLE IF NOT EXISTS RL_' + str(database) + '_' + str(environment)+'_ADMIN;')
line2 = ('USE ROLE RL_' + str(database) + '_' + str(environment)+'_ADMIN;')
line3 = ('CREATE DATABASE DB_' + str(database) + '_' + str(environment)+';')

# Writing the lines to file
file1='V1__createdatabase.sql'
with open(file1,'w') as out:
    out.write('{}\n{}\n{}\n'.format(line1,line2,line3))
  
# Checking if the data is 
# written to file or not 
file1 = open('V1__createdatabase.sql', 'r') 
print(file1.read()) 
file1.close()