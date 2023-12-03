from django.shortcuts import render

# Использовал вымышленные данные, но это задание правда делал я!!!
# Просто не хочется светить свои данные на гитхабе


# Create your views here.
def index(request):
    header = 'Данные студента'
    student = {'study_place': 'Лучший колледж', 'group_num': "450-10",
               'specialization': 'Программирование Python',
               'after_graduation': 'Senior Python разработчик'}

    data = {'student': student}

    return render(request, 'index.html', context=data)

def about(request):
    student = {'name': 'Иванов Иван Иванович', 'height': '175', 'weight': '67', 'age': 17}
    data = {'student': student}
    return render(request, 'about.html', context=data)


def contact(request, phone, social_network, address, link):
    return render(request, 'contact.html', {'phone': phone, 'social_network': social_network, 'address': address, 'link': link})

def contacts(request):
    contacts_data = [
        {'name': 'Имя1', 'email': 'email1@example.com', 'phone': '+7234567893'},
        {'name': 'Имя2', 'email': 'email2@example.com', 'phone': '+7876543216'},
    ]
    return render(request, 'contacts.html', {'contacts_data': contacts_data})
def form(request):
    return render(request, 'form.html')