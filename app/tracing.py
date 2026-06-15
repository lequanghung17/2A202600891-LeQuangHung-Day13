from __future__ import annotations

import os
from functools import wraps
from typing import Any

try:
    from langfuse import get_client

    def observe(*args: Any, **kwargs: Any):
        name = kwargs.get("name")

        def decorator(func):
            @wraps(func)
            def wrapper(*func_args: Any, **func_kwargs: Any):
                span_name = name or func.__name__
                with get_client().start_as_current_span(name=span_name):
                    return func(*func_args, **func_kwargs)

            return wrapper

        if args and callable(args[0]):
            return decorator(args[0])
        return decorator

    class _LangfuseContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            get_client().update_current_trace(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            metadata = kwargs.pop("metadata", None)
            usage_details = kwargs.pop("usage_details", None)
            if usage_details is not None:
                metadata = {**(metadata or {}), "usage_details": usage_details}
            if metadata is not None or kwargs:
                get_client().update_current_span(metadata=metadata, **kwargs)

        def flush(self) -> None:
            get_client().flush()

    langfuse_context = _LangfuseContext()
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

        def flush(self) -> None:
            return None

    langfuse_context = _DummyContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))


def flush_traces() -> None:
    langfuse_context.flush()
