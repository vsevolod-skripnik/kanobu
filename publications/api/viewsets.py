from django.db.models import Count, Q, When, F, Case
from rest_framework import mixins, viewsets

from opinions.models import Opinion
from publications.api.serializers import PublicationSerializer
from publications.models import Publication


class PublicationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return Publication.objects.annotate(
            opinion_count=Count('opinions'),
            like_count=Count('opinions', filter=Q(opinions__category=Opinion.CATEGORY_LIKE)),
            dislike_count=Count('opinions', filter=Q(opinions__category=Opinion.CATEGORY_DISLIKE)),
            current_user_opinion=Case(When(opinions__owner=self.request.user.id, then=F('opinions__category'))),
        )
