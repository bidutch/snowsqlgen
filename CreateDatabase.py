# User inputs

database = input(f'\nEnter the name of the database you want to create: ')
environment = input(f'\nEnter the name of the environment (DTAP) you want to create: ')

# Setting variables

strdatabase = str(database)
strenvironment = str(environment)

# Composing the code

line10 = ('CREATE ROLE IF NOT EXISTS RL_' + strdatabase + '_' + strenvironment +'_ADMIN;')
line13 = ('GRANT ALL PRIVILEGES ON ACCOUNT TO ROLE RL_' + strdatabase + '_' + strenvironment +'_ADMIN;')
line15 = ('GRANT ROLE RL_' + strdatabase + '_' + strenvironment +'_ADMIN TO USER JOHAN;')
line20 = ('USE ROLE RL_' + strdatabase + '_' + strenvironment +'_ADMIN;')
line30 = ('CREATE DATABASE DB_' + strdatabase + '_' + strenvironment +';')

# Writing the lines to file
file1='V1.1__createdatabase.sql'
with open(file1,'w') as out:
    out.write('{}\n{}\n{}\n{}\n{}\n'.format(line10,line13,line15,line20,line30))
  
# Checking if the data is 
# written to file or not 
file1 = open('V1.1__createdatabase.sql', 'r') 
print(file1.read()) 
file1.close()