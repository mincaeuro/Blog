from django.shortcuts import get_object_or_404,render

from .models import Prispevok, Komentar

def index(request):
	posledne_prispevky = Prispevok.objects.order_by('-pub_date')[:5]
	context = {'posledne_prispevky': posledne_prispevky}
	return render(request, 'posts/index.html', context)

def detail(request, post_id):
	prispevok = get_object_or_404(Prispevok, pk=post_id)
	return render(request, 'posts/detail.html', {'prispevok': prispevok})

