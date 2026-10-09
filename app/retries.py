from .provider import ProviderFailure

def charge_with_retry(provider, amount_minor, idempotency_key, sleep=lambda _: None, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return provider.charge(amount_minor,f"{idempotency_key}:{attempt}")
        except ProviderFailure:
            if attempt == max_attempts-1:
                raise
            sleep(1)
