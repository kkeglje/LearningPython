birthdays = {'Karlo': '21.11','Goga': '1.3','Vanja': '10.03'}

while True:
    print('Enter a name:(blank to quit)')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for '+name)
        print('When is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday daabase updated.\n')