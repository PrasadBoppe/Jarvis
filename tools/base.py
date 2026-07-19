from dataclasses import dataclass
from typing import Optional


@dataclass
class ToolResult:
    """Structured result from tool execution."""
    success: bool
    content: str
    source: str
    metadata: Optional[dict] = None
