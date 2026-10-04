"""Fixed annual targets using the shared portfolio state sequence."""
import pandas as pd
from ..funktionen import validate_target_weights
from ..engine.portfolio import run_annual_portfolio


class Rebalance:
    def run(self, context, params):
        if set(params) != {"target_weights", "rebalance_frequency"} or params["rebalance_frequency"] != "annual":
            raise ValueError("Rebalancing requires explicit target weights and annual frequency.")
        target = validate_target_weights(pd.Series(params["target_weights"])).sort_index()
        return run_annual_portfolio(context, "rebalance", lambda date, kind: target.copy())
