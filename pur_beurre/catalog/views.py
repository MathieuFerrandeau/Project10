"""views management"""
import logging

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models import Product, UserFavorite



#logging.basicConfig(filename="logs/views.log",
 #                   filemode="w",
  #                  format='%(asctime)s - %(message)s',
   #                 datefmt='%d-%b-%y %H:%M:%S',
    #                level=logging.INFO)

# Create your views here.
def index(request):
    """index view"""
    template = loader.get_template('catalog/index.html')
    return HttpResponse(template.render(request=request))


def credits(request):
    """credits view"""
    return render(request, 'catalog/credits.html')


def search(request):
    """search view"""
    user_query = request.GET.get('query')
    query = str.capitalize(user_query)
    try:
        product = Product.objects.filter(name=query).first()
        substitutes = Product.objects.filter(
            category=product.category,
            nutrition_grade__lt=product.nutrition_grade).order_by(
                "nutrition_grade")
        paginator = Paginator(substitutes, 6)
        page = request.GET.get('page')
        alt_products = paginator.get_page(page)
        context = {
            'alt_products': alt_products,
            'paginate': True,
            'title': query,
            'image': product.picture,
        }
    except AttributeError:
        messages.warning(request, "Ce produit n'existe pas. Vérifiez l'orthographe de la recherche")
        return redirect('catalog:index')
    logging.info('New search', exc_info=True, extra={
        'request': request,
    })
    return render(request, 'catalog/search.html', context)


def detail(request, product_id):
    """detail view"""
    product = Product.objects.get(id=product_id)

    context = {
        'name': product.name,
        'title': 'Informations nutritionnelles',
        'product': product,
        'nutrition_image': product.nutrition_image,
    }

    return render(request, 'catalog/detail.html', context)


@login_required
def favorite(request, product_id):
    """favorite view"""
    try:
        UserFavorite.objects.get(user_name_id=request.user.id,
                                 product_id=(product_id)
                                 )
        messages.warning(request, 'Ce produit est déjà dans vos favoris.')
        return redirect(request.META.get('HTTP_REFERER'))
    except ObjectDoesNotExist:
        UserFavorite.objects.create(user_name_id=request.user.id,
                                    product_id=(product_id)
                                    )
        messages.success(request, 'Le produit a bien été enregistré.')
        return redirect(request.META.get('HTTP_REFERER'))
