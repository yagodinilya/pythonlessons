def info(name, surname, birthday, city, email, phone):
    return f"Name: {name}; Surname: {surname}; birthday: {birthday};" \
           f"City: {city}; Email: {email}; Phone: {phone} "
print(info(name="Ilya", surname="Yagodin", birthday="08.10.1996",
           city="Moscow", email="yagodin.ilya@gamil.com", phone="89037428970"))
