# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, url

from .views import IndexView, EditClusterView, ClusterDetailView, \
    EditTemplateView, CreateClusterView, CreateNodeTemplateView, \
    NodeTemplateDetailView


CLUSTERS = r'^(?P<instance_id>[^/]+)/%s$'
TEMPLATES = r'^templates/(?P<template_id>[^/]+)/%s$'
VIEW_MOD = 'openstack_dashboard.syspanel.hadoop.views'


urlpatterns = patterns(VIEW_MOD,
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^create$', CreateClusterView.as_view(), name='create_cluster'),
    url(r'^create_template$', CreateNodeTemplateView.as_view(),
        name='create_template'),
    url(r'^clusters/(?P<cluster_id>[^/]+)/$', ClusterDetailView.as_view(),
        name='cluster_details'),
    url(r'^node_templates/(?P<node_template_id>[^/]+)/$',
        NodeTemplateDetailView.as_view(), name='node_template_details'),
    url(CLUSTERS % 'update', EditClusterView.as_view(), name='edit_cluster'),
    url(TEMPLATES % 'edit_template', EditTemplateView.as_view(),
        name='edit_template')
)
