"""python -m maturarbeit_engine run --config local.json"""
import argparse
import sys
from .engine.simulation import run_simulation


def main(argv=None):
    parser = argparse.ArgumentParser(description="Local Buy-and-Hold backtest core")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--config", required=True)
    args = parser.parse_args(argv)
    try:
        outcome = run_simulation(args.config)
    except (ValueError, OSError, UnicodeError) as exc:
        print(f"Run failed: {exc}", file=sys.stderr)
        return 2
    print(outcome.output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
