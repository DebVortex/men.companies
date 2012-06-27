from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText

from men.companies import _

class ICompanyList(form.Schema):
    """A list of companies.
    """
    
    title = schema.TextLine(
            title=_(u"title_company_list_label",
                    u"Name"),
            required=True,
            description=_(u"title_company_list_descr",
                          u""),
        )
    
    description = schema.Text(
            title=_(u"description_company_list_lable",
                    u"Description"),
            required=False,
        )
    
    information = RichText(
            title=_(u"information_company_list_lable",
                    u"Information"),
            required=False,
        )
