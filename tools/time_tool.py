from datetime import datetime
from .base import ToolResult


class TimeTool:

    def execute(self, query: str) -> ToolResult:
        """Get current date and time."""
        now = datetime.now()
        
        # Parse what the user is asking for
        query_lower = query.lower()
        
        if "time" in query_lower and "date" not in query_lower:
            content = f"The current time is {now.strftime('%I:%M %p')}."
        elif "date" in query_lower and "time" not in query_lower:
            content = f"Today's date is {now.strftime('%A, %B %d, %Y')}."
        else:
            content = f"The current date and time is {now.strftime('%A, %B %d, %Y at %I:%M %p')}."
        
        return ToolResult(
            success=True,
            content=content,
            source="time_tool",
            metadata={"timestamp": now.isoformat()}
        )
