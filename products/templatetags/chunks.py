from django import template

register = template.Library()

@register.filter(name='chunks')

def chunks(list_data,chunk_size):
    chunk = []
    i = 0
    for x in list_data:
        chunk.append(x)
        i = i +1
        if i == chunk_size:
            yield chunk
            i = 0
            chunk =[]
    if chunk:
        yield chunk

