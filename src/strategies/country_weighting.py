"""Pure GDP country weights with one explicitly configured proxy per country."""
from dataclasses import replace
from ..data.macro import select_gdp_targets
from ..engine.portfolio import run_annual_portfolio


class CountryWeighting:
    def run(self, context, params):
        if (not context.config.country_weighting_enabled or context.macro is None
                or params != context.config.country_params()):
            raise ValueError("Country weighting requires the configured, validated macro context.")
        decisions = []

        def target_at(date, kind):
            targets, decision = select_gdp_targets(context.macro, params, date, kind)
            decisions.append(decision)
            return targets

        result = run_annual_portfolio(context, "country_weighting", target_at)
        return replace(result, macro_decisions=tuple(decisions))
