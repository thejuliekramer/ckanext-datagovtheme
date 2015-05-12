import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
from sqlalchemy.util import OrderedDict

class DatagovTheme(p.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    p.implements(p.IConfigurer)
    p.implements(p.IFacets, inherit=True)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_resource('fanstatic_library', 'datagovtheme')
    
    
    def dataset_facets(self, facets_dict, package_type):

        if package_type != 'dataset':
            return facets_dict

        return OrderedDict([('groups', 'Topics'),
                            ('vocab_category_all', 'Topic Categories'),
                            ('metadata_type','Dataset Type'),
                            ('tags','Tags'),
                            ('res_format', 'Formats'),
                            ('organization_type', 'Organization Types'),
                            ('organization', 'Organizations'),
                            ('publisher', 'Publisher'),
                           ## ('extras_progress', 'Progress'),
                           ])

    def organization_facets(self, facets_dict, organization_type, package_type):

        if not package_type:
            return OrderedDict([('groups', 'Topics'),
                                ('vocab_category_all', 'Topic Categories'),
                                ('metadata_type','Dataset Type'),
                                ('tags','Tags'),
                                ('res_format', 'Formats'),
                                ('groups', 'Topics'),
                                ('harvest_source_title', 'Harvest Source'),
                                ('capacity', 'Visibility'),
                                ('dataset_type', 'Resource Type'),
                                ('publisher', 'Publisher'),
                               ])
        else:
            return facets_dict
    
    def group_facets(self, facets_dict, organization_type, package_type):

        # get the categories key
        group_id = p.toolkit.c.group_dict['id']
        key = 'vocab___category_tag_%s' % group_id
        if not package_type:
            return OrderedDict([(key, 'Categories'),
                                ('metadata_type','Dataset Type'),
                                ('organization_type', 'Organization Types'),
                                ('tags','Tags'),
                                ('res_format', 'Formats'),
                                ('organization', 'Organizations'),
                                (key, 'Categories'),
                                #('publisher', 'Publisher'),
                               ])
        else:
            return facets_dict