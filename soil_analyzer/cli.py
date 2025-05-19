"""Command line interface for the soil analyzer using Click."""
import click

from .input import prompt_for_soil_data
from .analysis import analyze_soil
from .recommendation import recommend_amendments, recommend_crops
from .io import read_csv


def _print_report(sample: dict) -> None:
    report = analyze_soil(sample)
    amendments = recommend_amendments(sample)
    crops = recommend_crops(sample)

    click.echo("Analysis:")
    for k, v in report.items():
        click.echo(f"- {k}: {v}")
    click.echo("\nRecommendations:")
    if amendments:
        click.echo("* Amendments: " + '; '.join(amendments))
    if crops:
        click.echo("* Crops: " + ', '.join(crops))


@click.group()
def cli():
    """Intelligent Soil Condition Analyzer"""


@cli.command()
@click.option('--interactive', is_flag=True, help='Run in interactive mode')
def analyze(interactive: bool):
    """Analyze a single soil sample."""
    if not interactive:
        click.echo("Use --interactive to enter data interactively or 'analyze-csv PATH' to analyze a CSV file.")
        return
    sample = prompt_for_soil_data()
    _print_report(sample)


@cli.command('analyze-csv')
@click.argument('path', type=click.Path(exists=True))
def analyze_csv(path: str):
    """Analyze soil samples from a CSV file."""
    samples = read_csv(path)
    for i, sample in enumerate(samples, start=1):
        click.echo(f"\nSample {i}:")
        _print_report(sample)


if __name__ == '__main__':
    cli()
