from django_components import component

VALID_STYLES = {'rounded'}

@component.register('navbar')
class NavLink(component.Component):
    template_name = 'navbar/template.html'

    def get_context_data(self, request, style: str, navlinks: object):
        if(style not in VALID_STYLES):
            raise ValueError('Value "style" must be one of %r.' % VALID_STYLES)

        return {
            'request': request,
            'style': style,
            'navlinks': navlinks.items(),
        }
    
    class Media:
        css = 'navbar/style.css'
        js = 'navbar/script.js'