"""Формирование строки состояния публикации."""


def format_status(version: str, deployed: bool) -> str:
    """Возвращает версию и состояние публикации."""
    unused_message = 'publication'
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"
