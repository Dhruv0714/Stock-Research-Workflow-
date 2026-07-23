from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED

console = Console()

STATUS_STYLE = {
    "waiting": ("○", "dim white"),
    "running": ("⟳", "bold yellow"),
    "completed": ("✓", "bold green"),
    "failed": ("✗", "bold red"),
}


class WorkflowDashboard:
    def __init__(self, ticker: str, task_labels: list[str]):
        self.ticker = ticker
        self.order = task_labels
        self.status = {label: "waiting" for label in task_labels}
        self.live = Live(self._render(), console=console, refresh_per_second=8)

    def _render(self):
        table = Table.grid(padding=(0, 2))
        table.add_column(justify="center", width=3)
        table.add_column(justify="left", min_width=24)
        table.add_column(justify="right")

        for label in self.order:
            state = self.status[label]
            icon, style = STATUS_STYLE[state]
            table.add_row(
                f"[{style}]{icon}[/{style}]",
                label,
                f"[{style}]{state.capitalize()}[/{style}]",
            )

        return Panel(
            table,
            title=f"[bold cyan]Stock Research Workflow · {self.ticker}[/bold cyan]",
            border_style="cyan",
            box=ROUNDED,
            padding=(1, 2),
        )

    def start(self):
        self.live.start()

    def stop(self):
        self.live.stop()

    def _set(self, label: str, state: str):
        if label in self.status:
            self.status[label] = state
            self.live.update(self._render())

    def start_task(self, label: str):
        self._set(label, "running")

    def complete_task(self, label: str, next_label: str | None = None):
        self._set(label, "completed")
        if next_label:
            self._set(next_label, "running")

    def fail_task(self, label: str):
        self._set(label, "failed")

    def current_running(self):
        return next((l for l, s in self.status.items() if s == "running"), None)
