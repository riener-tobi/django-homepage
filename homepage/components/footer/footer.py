from django_components import component

@component.register('footer')
class NavLink(component.Component):
    template_name = 'footer/template.html'

    def get_context_data(self, footerlinks: object, brand_name: str, email: str):

        return {
            'footerlinks': footerlinks.items(),
            'brand_name': brand_name,
            'copyright': 'Tobias Riener',
            'copyright_year': '2024',
            'email': email,
        }
    
    class Media:
        css = 'footer/style.css'
        js = 'footer/script.js'