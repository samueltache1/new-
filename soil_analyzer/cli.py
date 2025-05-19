"""Click-based command line interface for the soil analyzer."""

import click

from .input import prompt_for_soil_data, read_soil_data_from_csv
from .analysis import analyze_soil
from .recommendation import recommend_amendments, recommend_crops


@click.group(invoke_without_command=True)
@click.option("--interactive", is_flag=True, help="Run in interactive mode")
@click.pass_context
def cli(ctx, interactive):
    """Intelligent Soil Condition Analyzer."""
    if ctx.invoked_subcommand is None:
        if interactive:
            ctx.invoke(interactive_cmd)
        else:
            click.echo(ctx.get_help())


@cli.command("interactive")
def interactive_cmd():
    """Prompt for a single soil sample and analyze it."""
    sample = prompt_for_soil_data()
    _print_report(sample)


@cli.command("analyze-csv")
@click.argument("path")
def analyze_csv(path):
    """Analyze soil samples from a CSV file."""
    samples = read_soil_data_from_csv(path)
    for i, sample in enumerate(samples, 1):
        click.echo(f"\nSample {i}:")
        _print_report(sample)


def _print_report(sample):
    report = analyze_soil(sample)
    amendments = recommend_amendments(sample)
    crops = recommend_crops(sample)
    click.echo("Analysis:")
    for k, v in report.items():
        click.echo(f"- {k}: {v}")
    click.echo("\nRecommendations:")
    if amendments:
        click.echo("* Amendments: " + "; ".join(amendments))
    if crops:
        click.echo("* Crops: " + ", ".join(crops))


def main():  # pragma: no cover - entry point
    cli()


if __name__ == "__main__":  # pragma: no cover
    main()

