from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to '
                         f'{bag[item_id]} in your bag')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        return HttpResponse(status=405)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product in the shopping bag
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, 'Quantity updated successfully')
        else:
            bag.pop(item_id, None)
            messages.success(request, 'Item removed from your bag')

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        return HttpResponse(status=405)


def remove_from_bag(request, item_id):
    """
    Remove the specified product from the shopping bag
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, 'Item removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
