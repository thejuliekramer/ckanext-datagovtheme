# encoding: utf-8

'''Tests for the ckanext.datagovtheme extension.

'''
from ckantoolkit.tests.helpers import FunctionalTestBase
from nose.tools import assert_in, assert_true, assert_not_in, assert_false

from ckan import plugins as p
import mock
import ckanext


class TestDatagovthemeServed(FunctionalTestBase):
    '''Tests for the ckanext.datagovtheme.plugin module.'''

    @classmethod
    def setup_class(cls):
        super(TestDatagovthemeServed, cls).setup_class()

        if not p.plugin_loaded('geodatagov'):
            p.load('geodatagov')

        if not p.plugin_loaded('datagovtheme'):
            p.load('datagovtheme')

    @classmethod
    def teardown_class(cls):
        super(TestDatagovthemeServed, cls).teardown_class()
        p.unload('geodatagov')
        p.unload('datagovtheme')

    def test_plugin_loaded(self):
        assert_true(p.plugin_loaded('datagovtheme'))
        assert_true(p.plugin_loaded('geodatagov'))

    @mock.patch('ckanext.datagovtheme.helpers.is_bootstrap2')
    def test_datagovtheme_css_is_bootstrap2(self, mock):
        mock.return_value = True
        assert ckanext.datagovtheme.helpers.is_bootstrap2() == True
        app = self._get_test_app()

        index_response = app.get('/dataset')
        if ckanext.datagovtheme.helpers.is_bootstrap2():
            print(True)
    
    @mock.patch('ckanext.datagovtheme.helpers.is_bootstrap2')
    def test_datagovtheme_css(self, mock):
        mock.return_value = False
        assert ckanext.datagovtheme.helpers.is_bootstrap2() == False
        app = self._get_test_app()

        index_response = app.get('/dataset')
        if not ckanext.datagovtheme.helpers.is_bootstrap2():
            print(False)


