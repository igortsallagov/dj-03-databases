from django.shortcuts import render
from .models import Phone, Apple, Samsung


def show_catalog(request):
    phones = Phone.objects.all()
    phones_list = list()
    all_params = list()
    extra_params = list()
    for field in Phone._meta.get_fields()[1:]:
        if field.name not in all_params:
            all_params.append(field.name)
    for phone in [Apple, Samsung]:
        for field in phone._meta.get_fields()[1:]:
            if field.name not in all_params and field.name not in extra_params:
                extra_params.append(field.name)
    for phone in phones:
        phone_list = list()
        for param in all_params[1:]:
            phone_list.append(getattr(Phone.objects.get(id=phone.id), param))
        for param in extra_params[1:]:
            for model in [Apple, Samsung]:
                if model.objects.filter(id=phone.id):
                    if hasattr(model.objects.get(id=phone.id), param):
                        value = getattr(model.objects.get(id=phone.id), param)
                        if value is True:
                            phone_list.append('Есть')
                        phone_list.append(value)
                else:
                    phone_list.append('-')
        phones_list.append(phone_list)

    context = {
        'phones': phones_list
    }
    return render(
        request,
        'catalog.html', context
    )
