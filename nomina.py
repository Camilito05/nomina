
## us1 /create register
users = 
def createUser():
    user = []
    id = int(input("Ingrese su documento de indentidad:  "))
    user.append(id)
    user_name = input("Ingres el nombre: ")
    user.append(user_name)
    user_last_name = input("ingrese su apellido: ")
    user.append(user_last_name)
    pone = input("Ingrese su numero Telefonico: ")
    user.append(pone)
    user_email = input("ingrese si Email: ")
    user.append(user_email)
    user_password = input("ingrese la contraseña: ")
    user.append(user_password) 
    users.append(user)

createUser()
createUser()

print(users)
    


    