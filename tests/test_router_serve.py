"""Tests for Router-Serve RoutingService."""

import pytest

from router_serve import RoutingService, ServeRegistry


def test_route_picks_cheapest_sufficient():
    service = RoutingService()
    service.add_expert("small", capacity=1.0, cost=1.0)
    service.add_expert("large", capacity=10.0, cost=5.0)
    assert service.route(0.5) == "small"
    assert service.route(5.0) == "large"


def test_route_no_expert_raises():
    service = RoutingService()
    service.add_expert("small", capacity=1.0)
    with pytest.raises(ValueError):
        service.route(2.0)


def test_serve_tracks_usage_and_rejections():
    service = RoutingService()
    service.add_expert("e", capacity=1.0)
    service.serve("r1", 0.5)
    with pytest.raises(ValueError):
        service.serve("r2", 5.0)
    assert service.usage() == {"e": 1}
    assert service.stats["routed"] == 2
    assert service.stats["rejected"] == 1


def test_serve_returns_latency():
    service = RoutingService()
    service.add_expert("e", capacity=1.0)
    out = service.serve("r1", 0.5)
    assert out["expert"] == "e"
    assert out["latency_ms"] >= 0.0


def test_add_expert_validates():
    service = RoutingService()
    with pytest.raises(ValueError):
        service.add_expert("", 1.0)
    with pytest.raises(ValueError):
        service.add_expert("e", 0.0)
    with pytest.raises(ValueError):
        service.add_expert("e", 1.0, cost=-1.0)


def test_base_registry_still_works():
    assert ServeRegistry().summary()["requests"] == 0
