""" orbitdocXBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment

class orbitdocXBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "other"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="OrbitDoc",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="Doc URL",
	    '''
		TODO# The below URL to be replaced with valid document URL
		'''
        default="http://tutorial.math.lamar.edu/pdf/Trig_Cheat_Sheet.pdf",
        scope=Scope.content,
        help="The URL for your document.")
    
    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        
        context = {
            'display_name': self.display_name,
            'url': self.url
        }
        html = self.render_template('static/html/orbitdoc_view.html', context)
        
        frag = Fragment(html)
        frag.add_css(self.load_resource("static/css/orbitdoc.css"))
        frag.add_javascript(self.load_resource("static/js/orbitdoc_view.js"))
        frag.initialize_js('orbitdocXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url
        }
        html = self.render_template('static/html/orbitdoc_edit.html', context)
        
        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/orbitdoc_edit.js"))
        frag.initialize_js('orbitdocXBlockInitEdit')
        return frag

    @XBlock.json_handler
    def save_orbitdoc(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url']
        
        return {
            'result': 'success',
        }
