from django_components import component

VALID_STYLES = {'rounded'}

INACTIVE_ICON_STYLE = 'fa-regular'
ACTIVE_ICON_STYLE = 'fa-solid'

@component.register('nav-link')
class NavLink(component.Component):
    template_name = 'nav-link/template.html'

    def get_context_data(self, request, style: str, title: str, link: str, isActive: bool = None, icon: str = ''):
        if(style not in VALID_STYLES):
            raise ValueError('Value "style" must be one of %r.' % VALID_STYLES)

        if(isActive == None and request.path == link):
            isActive = True
        elif(isActive == None):
            isActive = False

        if(isActive):
            icon = icon.replace(INACTIVE_ICON_STYLE, ACTIVE_ICON_STYLE)

        return {
            'style': style,
            'title': title,
            'link': link,
            'icon': icon,
            'isActive': isActive,
        }
    
    class Media:
        css = 'nav-link/style.css'