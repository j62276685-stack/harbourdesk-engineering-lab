import json
from pathlib import Path

class ProviderFailure(Exception):
    def __init__(self, status, code, retry_after=None, elapsed_seconds=0):
        self.status, self.code, self.retry_after = status, code, retry_after
        self.elapsed_seconds = elapsed_seconds
        super().__init__(code)

class ScriptedProvider:
    """Local deterministic stub: no network requests or real payments."""
    def __init__(self, responses, on_call=lambda seconds: None):
        self.responses, self.calls = list(responses), []
        self.on_call = on_call

    @classmethod
    def from_file(cls, path):
        return cls(json.loads(Path(path).read_text())["responses"])

    def charge(self, amount_minor, idempotency_key):
        self.calls.append({"amount_minor":amount_minor,"idempotency_key":idempotency_key})
        if not self.responses:
            raise RuntimeError("Provider script exhausted")
        result = self.responses.pop(0)
        self.on_call(result.get("elapsed_seconds",0))
        if result.get("status",200) != 200:
            raise ProviderFailure(result["status"],result["code"],result.get("retry_after"),result.get("elapsed_seconds",0))
        return result
