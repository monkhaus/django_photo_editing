from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.template import loader
from .forms import PostForm
from .models import Post

from django.contrib.auth.decorators import login_required


@login_required(login_url='account:login')
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)

	if(form.is_valid()):
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	    "form": form,
	}
	return render(request, "face/post_form.html", context)

@login_required(login_url='account:login')
def post_detail(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	context = {

	    "title": instance.title,
	    "instance": instance,
	}
	return render(request, "face/post_detail.html", context)

@login_required(login_url='account:login')
def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
	    "title": "List"
	}
	return render(request, "face/base.html", context)

@login_required(login_url='account:login')
def post_update(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if(form.is_valid()):
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Item Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {

	    "title": instance.title,
	    "instance": instance,
	    "form": form,
	}
	return render(request, "face/post_form.html", context)


@login_required(login_url='account:login')
def post_delete(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	instance.delete()
	messages.success(request, "Item Deleted")
	return redirect("face:list")
