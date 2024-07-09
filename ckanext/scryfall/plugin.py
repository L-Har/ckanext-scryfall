import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class ScryfallPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IPackageController)
    
    read(self, entity):
        pass

    create(self, entity):
        pass

    edit(self, entity):
        pass

    delete(self, entity):
        pass

    after_create(self, context, pkg_dict):
        pass

    after_update(self, context, pkg_dict):
        pass

    after_delete(self, context, pkg_dict):
        pass

    after_show(self, context, pkg_dict):
        pass

    before_search(self, search_params):
        pass

    after_search(self, search_results, search_params):
        pass

    before_index(self, pkg_dict):
        pass

    before_view(self, pkg_dict):
        pass