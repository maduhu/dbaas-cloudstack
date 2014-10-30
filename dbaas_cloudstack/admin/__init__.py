# -*- coding:utf-8 -*-
from django.contrib import admin
from .cloudstack_serviceoffering import CloudStackServiceofferingAdmin
from .cloudstack_bundle import CloudStackBundleAdmin
from .cloudstack_region import CloudStackRegionAdmin
from .. import models

admin.site.register(models.CloudStackOffering, CloudStackServiceofferingAdmin)
admin.site.register(models.CloudStackBundle, CloudStackBundleAdmin)
admin.site.register(models.CloudStackRegion, CloudStackRegionAdmin)
