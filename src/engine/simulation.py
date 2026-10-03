"""One local run via the same code path for Python and CLI clients."""
from dataclasses import dataclass, field
from pathlib import Path
from .config import ConfigError, RunConfig, load_config
from .context import prepare_context
from .result import StrategyResult, validate_results
from ..strategies.buy_hold import BuyAndHold
from ..strategies.rebalance import Rebalance
from ..analysis.metrics import compute_metrics
from ..export.results import export_run
import pandas as pd


@dataclass(frozen=True)
class RunOutcome:
    result: StrategyResult
    output_path: Path
    manifest: dict
    results: dict[str, StrategyResult] = field(default_factory=dict)


def run_simulation(config: str | Path | RunConfig) -> RunOutcome:
    if isinstance(config, RunConfig):
        validated = load_config(config.config_path)
        if config != validated:
            raise ConfigError("RunConfig differs from its validated configuration file.")
        config = validated
    else:
        config = load_config(config)
    context = prepare_context(config)
    results = []
    if config.buy_hold_enabled:
        results.append(BuyAndHold().run(context, {"asset": config.asset}))
    if config.rebalance_enabled:
        results.append(Rebalance().run(context, {"target_weights": dict(config.target_weights),
                                                "rebalance_frequency": config.rebalance_frequency}))
    results = validate_results(context, results)
    summaries, statuses = [], {}
    for result in results:
        summary, status = compute_metrics(result, context)
        summaries.append(summary)
        statuses[result.strategy] = status
    # Preserve the accepted single-strategy status shape; add an explicit map for all runs.
    metric_status = statuses[results[0].strategy] if len(results) == 1 else statuses
    path, manifest = export_run(context, results, pd.concat(summaries, ignore_index=True), metric_status)
    return RunOutcome(results[0], path, manifest, {r.strategy: r for r in results})
