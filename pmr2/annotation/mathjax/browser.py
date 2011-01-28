import zope.component
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage
from plone.z3cform import layout
from z3c.form.interfaces import IForm

from pmr2.app.interfaces import IExposureSourceAdapter
from pmr2.app.exposure.browser.browser import ExposureFileViewBase

from pmr2.annotation.mathjax.layout import MathJaxLayoutWrapper


class MathJaxNote(ExposureFileViewBase):
    """\
    The MathJax viewer class.
    """

    template = ViewPageTemplateFile('mathjax_text.pt')
    title = ViewPageTemplateFile('mathjax_title.pt')

    def content(self):
        a = zope.component.queryAdapter(self.context, IExposureSourceAdapter)
        if a:
            return a.file()

MathJaxNoteView = layout.wrap_form(MathJaxNote, 
    __wrapper_class=MathJaxLayoutWrapper)
