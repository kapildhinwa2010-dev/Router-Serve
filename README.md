# Router-Serve

[![CI](https://github.com/kapildhinwa2010-dev/Router-Serve/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Router-Serve/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/Router-Serve/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Router-Serve/actions/workflows/codeql.yml)

Serve routing decisions: scalar score in, cheapest sufficient expert out, usage tracked.

## What it does

RoutingService registers experts with a capacity and a cost. Each serve
call takes a scalar score, picks the cheapest expert whose capacity
covers it, records per-expert usage and latency, and counts rejections
when no expert fits.

    from router_serve import RoutingService

    service = RoutingService()
    service.add_expert("small", capacity=1.0, cost=1.0)
    service.add_expert("large", capacity=10.0, cost=5.0)
    out = service.serve("req-1", score=0.5)
    print(out["expert"], out["latency_ms"])

## API

- RoutingService.add_expert / route / serve / usage / stats
- ServeRegistry - the generic base registry (unchanged from DNA-Serve)

## Honest results and limitations

- The score is whatever number you pass in; this service does not compute
  complexity or any other signal (see the Router repos for scorers).
- Decisions are greedy cheapest-sufficient; no load balancing or
  backpressure.
- Single-threaded, in-process; usage counts are not thread-safe.

## Status

Part of the kapildhinwa2010-dev toolkit experiments. CI and CodeQL run on
every push to main. License: MIT.
