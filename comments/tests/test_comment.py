from django.db.utils import IntegrityError
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    'attribute',
    [
        'text',
        'publication',
        'person',
    ]
)
def test_not_none_attributes(comment, attribute):
    with pytest.raises(IntegrityError):
        comment.update(**{attribute: None})