from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from .models import User


def index(request):
    users = User.objects.order_by('id')
    template = loader.get_template('users/index.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def createUser(request):
    awaitingKeys = ['first_name', 'last_name', 'address', 'phone', 'username']
    testKeys = True

    for k, v in request.POST.items():
        if k not in awaitingKeys:
            testKeys = False
    if testKeys == False:
        return JsonResponse({'message': 'form is invalid'}, status=401)
    else:
        for k in awaitingKeys:
            if (len(request.POST[k]) == 0):
                return JsonResponse({'message': k + ' is empty'}, status=401)

        if User.objects.filter(username=request.POST['username']).exists():
            return JsonResponse({'message': 'username already exist'}, status=401)
        u = User(first_name=request.POST['first_name'],
                 last_name=request.POST['last_name'],
                 address=request.POST['address'],
                 phone=request.POST['phone'],
                 username=request.POST['username'],
                 )
        u.save()
        return JsonResponse({'user': u.to_dict()}, status=200)
