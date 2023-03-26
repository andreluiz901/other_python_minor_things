#collect email from user
#split email using @, save 1° part as username and 2° part as the domain
#spli domain using ., 1° part 

def slicer():
    print("hi, im email slicer! \n")

    email_input = input("Input email address: ")

    (username, domain) = email_input.split("@") 
    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"extension: {extension} \n")

while True: 
    slicer()
