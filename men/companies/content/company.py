from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from men.companies import _

class ICompany(form.Schema):
    """A company type include informations about the company
    """
    
    title = schema.TextLine(
            title=_(u"title_company_label",
                    u"Organisation Name"),
            required=True,
            description=_(u"title_company_descr",
                          u""),
        )
    
    description = schema.Text(
            title=_(u"description_company_label",
                    u"Description"),
            required=False,
    )

    address = schema.Text(
            title=_(u"address_company_label",
                    u"Address"),
            required=True,
        )
    
    contact = schema.TextLine(
            title=_(u"contact_company_label",
                   u"Contact"),
            required=True,
        )
    
    telephone = schema.TextLine(
            title=_(u"telephone_company_label",
                   u"Phone"),
            required=True,
        )
    
    email = schema.TextLine(
            title=_(u"email_company_label",
                   u"E-Mail"),
            required=True,
        )

    comment = schema.Text(
            title=_(u"comment_company_label",
                   u"Comment"),
            required=False,
        )
    
    logo = NamedImage(
            title=_(u"logo_company_label",
                    u"Logo"),
            description=_(u"logo_company_descr",
                          u"Please upload an image"),
            required=False,
        )
                    
    


