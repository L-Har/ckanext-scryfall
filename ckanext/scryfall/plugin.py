import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class ScryfallPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IPackageController)
    
    def read(self, entity):
        pass

    def create(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass

    def after_create(self, context, pkg_dict):
        pass

    def after_update(self, context, pkg_dict):
        pass

    def after_delete(self, context, pkg_dict):
        pass

    def after_show(self, context, pkg_dict):
        pass

    def before_dataset_search(self, search_params):
        pass

    def before_search(self, search_params):
        pass

    def after_search(self, search_results, search_params):
        pass

    def before_index(self, pkg_dict):
        pass

    def before_view(self, pkg_dict):
        pass