#!/usr/bin/env python3
import argparse
import sys
import os
from chat_analyzer import ChatLogAnalyzer


class MainApp:
    """Main application class for chat log analyzer."""
    
    def __init__(self):
        """Initialize the main application."""
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create and configure argument parser."""
        parser = argparse.ArgumentParser(description='AI Chat Log Summarizer with TF-IDF Support')
        
        parser.add_argument('input', help='Path to chat log file or folder')
        parser.add_argument('--multiple', action='store_true', help='Analyze multiple files in a folder')
        parser.add_argument('--output', '-o', help='Output file to save summary')
        parser.add_argument('--basic', action='store_true', help='Use basic frequency analysis instead of TF-IDF')
        parser.add_argument('--no-nltk', action='store_true', help='Disable NLTK features (use basic text processing)')
        parser.add_argument('--version', action='version', version='Chat Log Analyzer v1.0')
        
        return parser
    
    def _validate_input(self, args) -> None:
        """Validate input arguments."""
        if not os.path.exists(args.input):
            print(f"Error: Path '{args.input}' does not exist.")
            sys.exit(1)
        
        if args.multiple and not os.path.isdir(args.input):
            print(f"Error: '--multiple' flag requires a directory path.")
            sys.exit(1)
        
        if not args.multiple and not os.path.isfile(args.input):
            print(f"Error: '{args.input}' is not a file.")
            sys.exit(1)
    
    def _perform_analysis(self, analyzer: ChatLogAnalyzer, args, use_tfidf: bool) -> str:
        """Perform the analysis based on arguments."""
        if args.multiple:
            print(f"Analyzing multiple files in: {args.input}")
            return analyzer.analyze_multiple_files(args.input, use_tfidf=use_tfidf)
        else:
            print(f"Analyzing file: {args.input}")
            return analyzer.analyze_single_file(args.input, use_tfidf=use_tfidf)
    
    def run(self) -> None:
        """Run the main application."""
        args = self.parser.parse_args()
        
        self._validate_input(args)
        
        analyzer = ChatLogAnalyzer(use_nltk=not args.no_nltk)
        use_tfidf = not args.basic
        
        print(f"Using {'TF-IDF' if use_tfidf else 'frequency analysis'} for keyword extraction")
        print("-" * 60)
        
        try:
            summary = self._perform_analysis(analyzer, args, use_tfidf)
            print(summary)
            
            if args.output:
                if analyzer.save_summary(summary, args.output):
                    print(f"\nSummary saved to: {args.output}")
                else:
                    print(f"\nFailed to save summary to: {args.output}")
                    sys.exit(1)
                    
        except KeyboardInterrupt:
            print("\nAnalysis interrupted by user.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)


def main():
    """Main function to run the chat log analyzer."""
    app = MainApp()
    app.run()


if __name__ == "__main__":
    main()