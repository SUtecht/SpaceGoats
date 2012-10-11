from django import template


register = template.Library()

@register.filter
def article_cut(article):
    if article.find('<!--break-->') >= 0:
        return article[:article.find('<!--break-->')]
    else:
        return article
