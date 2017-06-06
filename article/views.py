
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib import auth
from django.urls import reverse
from django.views.generic import UpdateView

from article.forms import CommentForm, ArticleForm
from article.models import Article, Comments, Category




def articles(request):  # страница со всеми статьями
    
    return render_to_response('articles.html',
                              { 'categories': Category.objects.all()  ,'articles': Article.objects.all(), 'username': auth.get_user(request).username})


def article(request, article_id=1):  # добавление статьи
    args = {}
    args.update(csrf(request))
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['article'] = Article.objects.get(id=article_id)
    args['form'] = CommentForm
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id):  # лайки/рейтинг статей
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):  # добавление комментариев
   
    if request.POST:
        form = CommentForm(request.POST)
        username = auth.get_user(request).username
       
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.username_comments = request.user
            form.save()
           
    return redirect('/articles/get/%s/' % article_id)
'''

    '''
def addarticle(request):  # форма добавления новой статьи))
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = ArticleForm()
    if request.POST:
        newarticle_form = ArticleForm(request.POST, request.FILES)
        if newarticle_form.is_valid():
            cd = newarticle_form.cleaned_data
            cd.update({'user': request.user})
            Article.objects.create(**cd)
            return redirect('/')
        else:
            args['form'] = newarticle_form  # если есть ошибки, снова на страницу
            return redirect('//')
    return render_to_response('addarticle.html', args)



def get_category(request, alias):
    try:
        username = auth.get_user(request).username
        category = Category.objects.get(alias=alias)
        article = Article.objects.filter(category=category)
    except:
        raise Http404 ('Обьект не найден')
    context = {'category': category,
               'articles': article,
               'username': username,

               }
    return render_to_response('articles.html', context)