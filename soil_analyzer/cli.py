"""Click command line interface for the soil analyzer."""
import csv
import click

from .input import prompt_for_soil_data
from .analysis import analyze_soil
from .recommendation import recommend_amendments, recommend_crops

EXAMPLE_INTERACTIVE = "python -m soil_analyzer.cli interactive"
EXAMPLE_CSV = "python -m soil_analyzer.cli analyze-csv samples.csv"

@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """Intelligent Soil Condition Analyzer.

    Use one of the commands below. Each command's help includes an example.
    """


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


@cli.command(help=f"Run interactive prompts. Example: {EXAMPLE_INTERACTIVE}")
def interactive():
    """Interactively enter one soil sample."""
    sample = prompt_for_soil_data()
    _print_report(sample)


@cli.command('analyze-csv', help=f"Analyze a CSV file. Example: {EXAMPLE_CSV}")
@click.argument('path')
def analyze_csv(path):
    """Load soil samples from PATH and analyze each."""
    samples = []
    with open(path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sample = {
                'pH': float(row['pH']),
                'moisture': float(row['moisture']),
                'organic_matter': float(row['organic_matter']),
                'sand': float(row['sand']),
                'silt': float(row['silt']),
                'clay': float(row['clay']),
            }
            samples.append(sample)
    for i, sample in enumerate(samples, 1):
        click.echo(f"\nSample {i}:")
        _print_report(sample)


def main():
    cli()


if __name__ == '__main__':
    main()
