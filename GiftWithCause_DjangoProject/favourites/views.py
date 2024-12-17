from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from GiftWithCause_DjangoProject.favourites.models import Favourite


@login_required
def likes_functionality(request, pk: int):
    added_to_favourites_gift = Favourite.objects.filter(
        to_gift_id=pk,
        user=request.user
    ).first()

    if added_to_favourites_gift:
        added_to_favourites_gift.delete()
    else:
        new_favourite_gift = Favourite(to_gift_id=pk, user=request.user)
        new_favourite_gift.save()

    # you can add/remove to/from favourites via urls
    url = reverse('gift-details', kwargs={'pk': pk})

    return redirect(f'{url}#{pk}')
    # return redirect(request.META.get('HTTP_REFERER') + f'#{pk}')



