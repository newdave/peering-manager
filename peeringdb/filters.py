import django_filters

from .models import PeerRecord, Synchronization


class PeerRecordFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method="search", label="Search")

    class Meta:
        model = PeerRecord
        fields = [
            "network__asn",
            "network__name",
            "network__irr_as_set",
            "network__info_prefixes6",
            "network__info_prefixes4",
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(network__name__icontains=value) | Q(
            network__irr_as_set__icontains=value
        )
        try:
            ip = ipaddress.ip_interface(value.strip())
            qs_filter |= Q(network_ixlan__ipaddr6__host=str(ip))
            qs_filter |= Q(network_ixlan__ipaddr4__host=str(ip))
        except ValueError:
            pass
        try:
            qs_filter |= Q(network__asn=int(value.strip()))
            qs_filter |= Q(network__info_prefixes6=int(value.strip()))
            qs_filter |= Q(network__info_prefixes4=int(value.strip()))
        except ValueError:
            pass
        return queryset.filter(qs_filter)


class SynchronizationFilter(django_filters.FilterSet):
    class Meta:
        model = Synchronization
        fields = ["time", "added", "updated", "deleted"]
