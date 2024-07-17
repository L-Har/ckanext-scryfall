from typing import Any
from ckan.types import Context
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ScryfallPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IPackageController)

    def read(self, entity: "model.Package") -> None:
        """
        Called after IPackageController.before_dataset_view inside
        package_show.
        """

    def create(self, entity: "model.Package"):
        """Called after the dataset had been created inside package_create."""

    def edit(self, entity: "model.Package") -> None:
        """Called after the dataset had been updated inside package_update."""

    def delete(self, entity: "model.Package") -> None:
        """Called before commit inside package_delete."""

    def after_dataset_create(self, context: Context, pkg_dict: dict[str, Any]) -> None:
        """
        Extensions will receive the validated data dict after the dataset
        has been created (Note that the create method will return a dataset
        domain object, which may not include all fields). Also the newly
        created dataset id will be added to the dict.
        """

    def after_dataset_update(self, context: Context, pkg_dict: dict[str, Any]) -> None:
        """
        Extensions will receive the validated data dict after the dataset
        has been updated.

        Note that bulk dataset update actions (`bulk_update_private`,
        `bulk_update_public`) will bypass this callback. See
        ``ckan.plugins.toolkit.chained_action`` to wrap those actions
        if required.
        """

    def after_dataset_delete(self, context: Context, pkg_dict: dict[str, Any]) -> None:
        """
        Extensions will receive the data dict (typically containing
        just the dataset id) after the dataset has been deleted.

        Note that the `bulk_update_delete` action will bypass this
        callback. See ``ckan.plugins.toolkit.chained_action`` to wrap
        that action if required.
        """

    def after_dataset_show(self, context: Context, pkg_dict: dict[str, Any]) -> None:
        """
        Extensions will receive the validated data dict after the dataset
        is ready for display.
        """

    def before_dataset_search(self, search_params: dict[str, Any]) -> dict[str, Any]:
        """
        Extensions will receive a dictionary with the query parameters,
        and should return a modified (or not) version of it.

        search_params will include an `extras` dictionary with all values
        from fields starting with `ext_`, so extensions can receive user
        input from specific fields.
        """
        return search_params

    def after_dataset_search(
        self, search_results: dict[str, Any], search_params: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Extensions will receive the search results, as well as the search
        parameters, and should return a modified (or not) object with the
        same structure::

            {'count': '', 'results': '', 'search_facets': ''}

        Note that count and facets may need to be adjusted if the extension
        changed the results for some reason.

        search_params will include an `extras` dictionary with all values
        from fields starting with `ext_`, so extensions can receive user
        input from specific fields.

        """

        return search_results

    def before_dataset_index(self, pkg_dict: dict[str, Any]) -> dict[str, Any]:
        """
        Extensions will receive what will be given to Solr for
        indexing. This is essentially a flattened dict (except for
        multi-valued fields such as tags) of all the terms sent to
        the indexer. The extension can modify this by returning an
        altered version.
        """
        return pkg_dict

    def before_dataset_view(self, pkg_dict: dict[str, Any]) -> dict[str, Any]:
        """
        Extensions will receive this before the dataset gets
        displayed. The dictionary passed will be the one that gets
        sent to the template.
        """
        return pkg_dict
