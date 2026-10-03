"""One local run via the same code path for Python and CLI clients."""
from dataclasses import dataclass
from pathlib import Path
from .config import ConfigError, RunConfig, load_config
from .context import prepare_context
from .result import StrategyResult
from ..strategies.buy_hold import BuyAndHold
from ..analysis.metrics import compute_metrics
from ..export.results import export_run


@dataclass(frozen=True)
class RunOutcome:
    result: StrategyResult
    output_path: Path
    manifest: dict


def run_simulation(config: str | Path | RunConfig) -> RunOutcome:
    if isinstance(config, RunConfig):
        validated = load_config(config.config_path)
        if config != validated:
            raise ConfigError("RunConfig differs from its validated configuration file.")
        config = validated
    else:
        config = load_config(config)
    context = prepare_context(config)
    result = BuyAndHold().run(context, {"asset": config.asset})
    summary, metric_status = compute_metrics(result, context)
    path, manifest = export_run(context, result, summary, metric_status)
    return RunOutcome(result, path, manifest)
