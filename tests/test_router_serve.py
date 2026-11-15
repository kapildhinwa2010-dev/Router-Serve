import pytest
import torch
from router_serve import RouterServe, create_router_serve

class TestRouterServe:
    def test_init(self):
        m = RouterServe(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = RouterServe(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_router_serve()
        assert isinstance(m, RouterServe)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
