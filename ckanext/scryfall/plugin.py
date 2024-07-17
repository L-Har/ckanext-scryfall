import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ScryfallPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IPackageController)

    def read(self, entity):
        """read"""
        print("In read")

    def create(self, entity):
        """create"""
        print("In ")


    def edit(self, entity):
        """edit"""
        print("In ")
        
    def delete(self, entity   ):
        """delete"""
        print("In ")
        
    def after_create(self, context, pkg_dict):
        """after_create"""
        print("In ")
        
    def after_update(self, context, pkg_dict):
        """after_update"""
        print("In ")
        
    def after_delete( self, context, pkg_dict):
        """after_delete"""
        print("In ")
        
    def after_show(self, context, pkg_dict):
        """after_show"""
        print("In ")
        
    def before_dataset_search( self, search_params):
        """before_dataset_search"""
        print("In ")
        
    def before_search(self, search_params):
        """before_search"""
        print("In ")
        
    def after_search(self, search_results, search_params):
        """after_search"""
        print("In ")
        
    def before_index(self, pkg_dict):
        """before_index"""
        print("In ")
        
    def before_view(self, pkg_dict):
        """before_view"""
        print("In ")
        