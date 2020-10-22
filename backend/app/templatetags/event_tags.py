from django import template
register = template.Library()

# USE THIS TO DEFINE FILTERS FOR TEMPLATE STUFF
@register.filter(name='filter')
def get_seller(value):
	return value