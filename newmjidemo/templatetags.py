from django import template


reg = template.Library()


@reg.filter
def key( item, string ):
  return item.get(string,'')
