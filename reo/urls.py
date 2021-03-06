# *********************************************************************************
# REopt, Copyright (c) 2019-2020, Alliance for Sustainable Energy, LLC.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list
# of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice, this
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#
# Neither the name of the copyright holder nor the names of its contributors may be
# used to endorse or promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
# *********************************************************************************
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^errors/', views.errors, name='errors'),
    url(r'^annual_kwh/', views.annual_kwh, name='annual_kwh'),
    url(r'^invalid_urdb/', views.invalid_urdb, name='invalid_urdb'),
    url(r'^help/', views.help, name='help'),
    url(r'^results/', views.results, name='results'),
    url(r'^simulated_load/', views.simulated_load, name='simulated_load'),
    url(r'^emissions_profile/', views.emissions_profile, name='emissions_profile'),
    url(r'^generator_efficiency/', views.generator_efficiency, name='generator_efficiency'),
    url(r'^chp_defaults/', views.chp_defaults, name='chp_defaults'),
    url(r'^loadprofile_chillerthermal_chiller_cop/', views.loadprofile_chillerthermal_chiller_cop, name='loadprofile_chillerthermal_chiller_cop'),
    url(r'^absorption_chiller_defaults/', views.absorption_chiller_defaults, name='absorption_chiller_defaults'),
    url(r'^schedule_stats/', views.schedule_stats, name='schedule_stats')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
