from django.shortcuts import render


def impl_babylon(request):
    context = {'my_var': 'impl_babylon.html'}
    return render(request, 'impl_babylon.html', context)
    # return render(request, 'impl_babylon.html')
