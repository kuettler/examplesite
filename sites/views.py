from django.shortcuts import get_object_or_404, render

from .models import Site, SiteData

def formatNumber(n):
    return "{:.2f}".format(n / 100.)

def navbar(page):
    return [{'name': 'Sites', 'href': '/sites', 'active': page == 'sites'},
            {'name': 'Summary', 'href': '/summary', 'active': page == 'summary'},]

def buttons(link):
    return [
        {'href': '/summary', 'active': link == 'sum', 'name': 'Sum'},
        {'href': '/summary-average', 'active': link == 'average', 'name': 'Average'},
    ]

def index(request):
    context = {
        'sites': Site.objects.all(),
        'navbar': navbar('sites'),
    }
    return render(request, 'sites/index.html', context)

def site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    context = {
        'name': site.name,
        'navbar': navbar('sites'),
        'lines': [{
            'date': sitedata.date.date(),
            'value_a': formatNumber(sitedata.value_a),
            'value_b': formatNumber(sitedata.value_b),
        } for sitedata in site.sitedata_set.all()],
    }
    return render(request, 'sites/site.html', context)

def summary(request):
    lines = []
    for site in Site.objects.all():
        line = [(sitedata.value_a, sitedata.value_b) for sitedata in site.sitedata_set.all()]
        lines.append({
            'name': site.name,
            'values_a': formatNumber(sum(e[0] for e in line)),
            'values_b': formatNumber(sum(e[1] for e in line)),
        })
    return render(request, 'sites/summary.html', {'lines': lines,
                                                  'navbar': navbar('summary'),
                                                  'buttons': buttons('sum')})

def summary_average(request):
    lines = []
    for site in Site.objects.all():
        # Use the database to sum and count. The id field of the object is abused to store the count.
        data = SiteData.objects.raw("SELECT count(*) AS id, sum(value_a) AS value_a, sum(value_b) AS value_b FROM sites_sitedata WHERE site_id = %d" % site.id)[0]
        lines.append({
            'name': site.name,
            'values_a': formatNumber(data.value_a / data.id),
            'values_b': formatNumber(data.value_b / data.id),
        })
    return render(request, 'sites/summary.html', {'lines': lines,
                                                  'navbar': navbar('summary'),
                                                  'buttons': buttons('average')})
