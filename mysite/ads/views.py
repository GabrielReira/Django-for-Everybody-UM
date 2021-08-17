from ads.models import Ad, Comment, Fav
from ads.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from ads.forms import CreateForm, CommentForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse


class IndexView(OwnerListView):
    model = Ad
    template_name = 'ads/ad_list.html'

    def get(self, request):
        favorites = list()

        if (request.user.is_authenticated):
            rows = request.user.favorite_ads.values('id')  # [{'id': 2}, {'id': 7}, ...]
            favorites = [row['id'] for row in rows]  # [2, 7, ...]

        # Milestone 4
        ad_search = request.GET.get("search", False)

        if (ad_search):
            query = Q(title__icontains=ad_search)
            query.add(Q(text__icontains=ad_search), Q.OR)
            query.add(Q(tags__name__in=[ad_search]), Q.OR)
            ad_list = Ad.objects.filter(query).select_related().distinct().order_by('-updated_at')[:10]
        else:
            ad_list = Ad.objects.all().order_by('-updated_at')

        ctx = {'ad_list': ad_list, 'search': ad_search ,'favorites': favorites}

        return render(request, self.template_name, ctx)


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'

    def get(self, request, pk):
        comment_ad = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=comment_ad).order_by('-updated_at')
        comment_form = CommentForm()
        ctx = {'ad': comment_ad, 'comments': comments, 'comment_form': comment_form}

        return render(request, self.template_name, ctx)


class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:ad_list')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}

        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        form.save_m2m()

        return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:ad_list')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form': form}

        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.save()
        form.save_m2m()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad


# Milestone 2

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)

    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        success_url = reverse_lazy('ads:ad_detail', args=[pk])
        ad = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=ad)
        comment.save()

        return redirect(success_url)


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'ads/comment_confirm_delete.html'


# Milestone 3

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        fav_ad = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=fav_ad)
        try:
            fav.save()
        except IntegrityError:
            pass

        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        del_ad = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=del_ad)
            fav.delete()
        except Fav.DoesNotExist:
            pass

        return HttpResponse()
