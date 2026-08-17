from django.shortcuts import render


def impl_aframe(request):
    context = {'my_var': 'impl_aframe.html'}
    return render(request, 'impl_aframe.html', context)
    # return render(request, 'impl_aframe.html')
