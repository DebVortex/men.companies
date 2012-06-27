from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class CompanyListView(BrowserView):
	
	index = ViewPageTemplateFile("companylistview.pt")

	def	__call__(self):
		self.companies = self.build_company_list()
		return self.index()
	
	def build_company_list(self):
		child_nodes = self.context.getChildNodes()
		child_list = []

		for child in child_nodes:
			child_dict = {
				"title":child.title,
				"description":child.description,
				"url":child.absolute_url(),
			}
			child_list.append(child_dict)
		return child_list

class CompanyView(BrowserView):

	def __call__(self):
		pass