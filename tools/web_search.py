from ddgs import DDGS
from .base import ToolResult


class WebSearchTool:

    def execute(self, query: str) -> ToolResult:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        lines = []

        for result in results:
            lines.append(
                f"Title: {result['title']}\n"
                f"URL: {result['href']}\n"
                f"Snippet: {result['body']}\n"
            )

        content = "\n".join(lines)
        
        return ToolResult(
            success=True,
            content=content,
            source="web_search",
            metadata={"query": query, "result_count": len(results)}
        )