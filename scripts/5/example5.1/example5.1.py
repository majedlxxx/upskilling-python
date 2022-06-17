def fill_template(template, data):
    results = template
    results = results.replace('NAME', data['name'])
    results = results.replace('POSITION', data['position'])
    results = results.replace('STARTDATE', data['startdate'])
    results = results.replace('SALARY', data['salary'])
    results = results.replace('EXPDATE', data['expdate'])
    return results




f = open('template.txt', 'r')
template = f.read()
f.close()

offers = []

no_of_offers = int(input("Enter number of offers: "))

for i in range(no_of_offers):
    offer = {
        'name': input("Enter name: "),
        'position': input("Enter position: "),
        'startdate': input("Enter starting date: "),
        'salary': input("Enter salary: "),
        'expdate': input("Enter expiry date: ")
    }
    offers.append(offer)
    
for offer in offers:
    email_content = fill_template(template, offer)
    f = open(f"{offer['position']}_{offer['name']}.txt", 'w')
    f.write(email_content)
    f.close()
    
    