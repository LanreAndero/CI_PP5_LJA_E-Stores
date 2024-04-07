from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        return HttpResponse(status=405)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product in the shopping bag
    """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id, None)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        return HttpResponse(status=405)


def remove_from_bag(request, item_id):
    """
    Remove the specified product from the shopping bag
    """
    if request.method == 'POST':
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
