# 308-Jamie-Ct-3b d-house — Tests

## Strategy

- Unit tests for all core logic
- Integration tests marked with `@pytest.mark.integration`
- Slow tests marked with `@pytest.mark.slow`

## Running Tests

```bash
# All tests
python -m pytest tests/ -v

# Skip slow tests
python -m pytest tests/ -m "not slow"
```

## Test Organization

| File | Coverage |
|------|----------|
| `test_*.py` | Core functionality |
