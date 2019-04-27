import pytest
import sn


@pytest.fixture
def ctx():
    sn.TIMELINES = {}
    sn.SUBSCRIPTIONS = {}
    yield sn
    sn.TIMELINES = {}
    sn.SUBSCRIPTIONS = {}
