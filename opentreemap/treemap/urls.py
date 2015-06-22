# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.conf.urls import patterns, url

from treemap import routes

# Testing notes:
# We want to test that every URL succeeds (200) or fails with bad data (404).
# If you add/remove/modify a URL, please update the corresponding test(s)
# in treemap/tests/urls.py

USERNAME_PATTERN = r'(?P<username>[\w.@+-]+)'

urlpatterns = patterns(
    '',
    url(r'^$', routes.index_page, name='instance_index_view'),
    url(r'page/(?P<page>[a-zA-Z0-9 ]+)/$',
        routes.static_page, name='static_page'),
    url(r'^boundaries/(?P<boundary_id>\d+)/geojson/$',
        routes.boundary_to_geojson),
    url(r'^boundaries/$', routes.boundary_autocomplete),
    url(r'^edits/$', routes.edits_page, name='edits'),
    url(r'^photo_review_full/$', routes.photo_review),
    url(r'^photo_review/$', routes.photo_review_partial,
        name='photo_review'),
    url(r'^photo_review/next$', routes.next_photo, name='photo_review_next'),
    url('^features/(?P<feature_id>\d+)/photo/(?P<photo_id>\d+)/'
        '(?P<action>(approve)|(reject))$',
        routes.approve_or_reject_photo, name='approve_or_reject_photo'),
    url(r'^species/$', routes.species_list, name="species_list_view"),
    url(r'^map/$', routes.map_page, name='map'),

    url(r'^features/(?P<feature_id>\d+)/$',
        routes.map_feature_detail, name='map_feature_detail'),
    url(r'^features/(?P<type>\w+)/$',
        routes.add_map_feature, name='add_map_feature'),
    url(r'^features/(?P<feature_id>\d+)/edit$',
        routes.edit_plot_detail, name='map_feature_detail_edit'),
    url(r'^features/(?P<feature_id>\d+)/popup$',
        routes.map_feature_popup, name='map_feature_popup'),
    url(r'^features/(?P<feature_id>\d+)/trees/(?P<tree_id>\d+)/$',
        routes.delete_tree),
    url(r'^features/(?P<feature_id>\d+)/sidebar$',
        routes.get_map_feature_sidebar, name='map_feature_sidebar'),
    url(r'^features/(?P<feature_id>\d+)/photo$',
        routes.add_map_feature_photo, name='add_photo_to_map_feature'),
    url(r'^features/(?P<feature_id>\d+)/detail$',
        routes.map_feature_accordion, name='map_feature_accordion'),
    url('^features/(?P<feature_id>\d+)/photo/(?P<photo_id>\d+)$',
        routes.rotate_map_feature_photo, name='rotate_photo'),
    url(r'^features/(?P<feature_id>\d+)/favorite$',
        routes.favorite_map_feature, name='favorite_map_feature'),
    url(r'^features/(?P<feature_id>\d+)/unfavorite$',
        routes.unfavorite_map_feature, name='unfavorite_map_feature'),

    url(r'^plots/$', routes.add_map_feature, name='add_plot'),
    url(r'^plots/(?P<feature_id>\d+)/eco$',
        routes.get_plot_eco, name='plot_eco'),
    url(r'^plots/(?P<feature_id>\d+)/trees/(?P<tree_id>\d+)/eco$',
        routes.get_plot_eco, name='tree_eco'),
    url(r'^plots/(?P<feature_id>\d+)/trees/(?P<tree_id>\d+)/$',
        routes.tree_detail, name='tree_detail'),

    # TODO: this duplication exists in multiple places.
    # we make two endpoints for 'plots/<id>/tree/<id>/' and 'plots/<id>/'
    # to simplify the client, because the plot_detail page itself can
    # have two different urls, and it makes it easier to say stuff like
    # url = document.url = '/photos' or whatever. We can find a higher level
    # way to handle this duplication and reduce the total number of endpoints
    # for great good.
    url(r'^plots/(?P<feature_id>\d+)/photo$',
        routes.add_tree_photo, name='add_photo_to_plot'),
    url(r'^plots/(?P<feature_id>\d+)/tree/(?P<tree_id>\d+)/photo$',
        routes.add_tree_photo, name='add_photo_to_tree'),

    url(r'^config/settings.js$',
        routes.instance_settings_js, name='settings'),
    url(r'^benefit/search$', routes.search_tree_benefits),
    url(r'^users/%s/$' % USERNAME_PATTERN, routes.instance_user_page,
        name="user_profile"),
    url(r'^users/%s/edits/$' % USERNAME_PATTERN, routes.instance_user_audits),
)
