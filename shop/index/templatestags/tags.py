from django import template
from django.db.models import Count
from about.models import AboutTeam
from catalog.models import Category, Catalog
from index.models import Action, Benefit, Contact

register = template.Library()


# Тег акции на главной
@register.inclusion_tag('tags/index_action.html')
def get_index_action():
    index_action = Action.objects.filter(action_active=True)
    return {'index_action_item': index_action}


# Тег команды для главной страницы
@register.inclusion_tag('tags/team_index.html')
def get_index_team():
    index_team = AboutTeam.objects.filter(team_index=True)[:4]
    return {'index_team_item': index_team}


# Тег команды
@register.inclusion_tag('tags/team_about.html')
def get_about_team():
    about_team = AboutTeam.objects.all().order_by('team_order').filter(team_draft=True)
    return {'about_team_item': about_team}


# Тег приемуществ
@register.inclusion_tag('tags/benefit.html')
def get_benefit():
    benefit = Benefit.objects.all()
    return {'benefit_item': benefit}


# Тег контактов в подвале
@register.inclusion_tag('tags/footer_contacts.html')
def get_footer_contacts():
    footer_contacts = Contact.objects.all()
    return {'footer_contacts_item': footer_contacts}


# Тег контактов на странице
@register.inclusion_tag('tags/page_contact.html')
def get_page_contact():
    page_contact = Contact.objects.all()
    return {'page_contact_item': page_contact}


# Тег категорий и счетчика товаров
@register.inclusion_tag('tags/categories.html')
def get_categories():
    category = Category.objects.all
    category_count = Category.objects.annotate(catalog_count=Count('catalog')).values('category_title', 'catalog_count')
    return {'categories': category, 'category_counts': category_count}


# Тег товаров нового поступления
@register.inclusion_tag('tags/new_arrivals.html')
def get_new_arrivals():
    new_arrivals = Catalog.objects.filter(catalog_new_arrivals=True, catalog_draft=True).order_by('-catalog_date')[:6]
    return {'new_arrivals_item': new_arrivals}