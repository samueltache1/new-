"""Command line interface for the soil analyzer."""
import argparse
from .input import prompt_for_soil_data
from .analysis import analyze_soil
from .recommendation import recommend_amendments, recommend_crops
from .formatting import format_report


def main(argv=None):
    parser = argparse.ArgumentParser(description="Intelligent Soil Condition Analyzer")
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    args = parser.parse_args(argv)

    if args.interactive:
        sample = prompt_for_soil_data()
        report = analyze_soil(sample)
        amendments = recommend_amendments(sample)
        crops = recommend_crops(sample)
        print("Analysis:")
        print(format_report(report))
        print("\nRecommendations:")
        if amendments:
            print("* Amendments: " + '; '.join(amendments))
        if crops:
            print("* Crops: " + ', '.join(crops))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
