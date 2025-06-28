# AI Chat Log Summarizer

A Python tool that analyzes chat logs between users and AI assistants using TF-IDF and NLP techniques for intelligent conversation insights.

## Features

- **Chat Log Parsing**: Processes `User:` and `AI:` formatted conversations
- **TF-IDF Analysis**: Advanced keyword extraction with mathematical scoring
- **Topic Detection**: Automatically categorizes conversations (AI, Programming, Data Science, Education)
- **NLTK Support**: Optional enhanced text processing with lemmatization
- **Multiple Formats**: Single file or batch folder analysis

## Requirements

- Python 3.6+
- Optional: `pip install nltk` (for enhanced analysis)

## Installation

```bash
git clone https://github.com/TareqazizUday/AI-Chat-Log-Summarizer.git
cd ai-chat-log-summarizer
```

## Usage

### Basic Commands

```bash
# Standard analysis with TF-IDF and NLTK
python main.py chat.txt

# Basic frequency analysis (no TF-IDF)
python main.py chat.txt --basic

# Disable NLTK features (basic text processing)
python main.py chat.txt --no-nltk

# Analyze multiple files
python main.py chat_logs/ --multiple

# Save output to file
python main.py chat.txt --output summary.txt
```

## Input Format

```
User: Hello! Can you explain machine learning?
AI: Machine learning is a subset of AI that enables computers to learn from data without explicit programming.
User: What are the main types?
AI: There are three main types: supervised, unsupervised, and reinforcement learning.
```

## Sample Outputs

### Standard TF-IDF Analysis Output

```
======================================================================
                    CHAT LOG ANALYSIS SUMMARY
======================================================================

CONVERSATION STATISTICS:
  Total exchanges: 7
  User messages: 7
  AI messages: 7
  Total messages: 14

ANALYSIS METHOD:
  Keyword extraction: TF-IDF
  Text processing: NLTK Enhanced

TOP KEYWORDS (TF-IDF):
  1. Explain (TF-IDF: 0.660)
  2. Doe (TF-IDF: 0.660)
  3. Work (TF-IDF: 0.660)
  4. Give (TF-IDF: 0.632)
  5. Machine (TF-IDF: 0.626)

CONVERSATION TOPICS:
  Artificial Intelligence: machine
  Education: explain

======================================================================
```

### Basic Frequency Analysis Output (`--basic` flag)

```
======================================================================
                    CHAT LOG ANALYSIS SUMMARY
======================================================================

CONVERSATION STATISTICS:
  Total exchanges: 7
  User messages: 7
  AI messages: 7
  Total messages: 14

ANALYSIS METHOD:
  Keyword extraction: Frequency Analysis
  Text processing: NLTK Enhanced

TOP KEYWORDS (Frequency Analysis):
  1. Learning (Frequency: 14)
  2. Machine (Frequency: 7)
  3. Pattern (Frequency: 4)
  4. Data (Frequency: 4)
  5. Python (Frequency: 4)

CONVERSATION TOPICS:
  Programming: python
  Artificial Intelligence: learning, machine
  Data Science: pattern, data

======================================================================
```

### Multiple Files Analysis Output (`--multiple` flag)

#### TF-IDF Method
```
ANALYSIS OF 4 CHAT LOG FILES
============================================================

FILE: data_science.txt
----------------------------------------
Exchanges: 6
User messages: 6
AI messages: 6
Top keywords: kind, important, degree

FILE: ml_conversation.txt
----------------------------------------
Exchanges: 7
User messages: 7
AI messages: 7
Top keywords: explain, work, doe

FILE: python_help.txt
----------------------------------------
Exchanges: 6
User messages: 6
AI messages: 6
Top keywords: error, avoid, future

FILE: web_development.txt
----------------------------------------
Exchanges: 12
User messages: 12
AI messages: 12
Top keywords: important, learn, development

OVERALL STATISTICS:
Total files analyzed: 4
Total exchanges: 31
Total user messages: 31
Total AI messages: 31
Most common keywords across all files:
  1. kind (appears in 2 analyses)
  2. important (appears in 2 analyses)
  3. degree (appears in 1 analyses)
  4. versus (appears in 1 analyses)
  5. project (appears in 1 analyses)
```

#### Frequency Method (`--multiple --basic`)
```
ANALYSIS OF 4 CHAT LOG FILES
============================================================

FILE: data_science.txt
----------------------------------------
Exchanges: 6
User messages: 6
AI messages: 6
Top keywords: data, project, skill

FILE: ml_conversation.txt
----------------------------------------
Exchanges: 7
User messages: 7
AI messages: 7
Top keywords: learning, machine, pattern

FILE: python_help.txt
----------------------------------------
Exchanges: 6
User messages: 6
AI messages: 6
Top keywords: variable, python, code

FILE: web_development.txt
----------------------------------------
Exchanges: 12
User messages: 12
AI messages: 12
Top keywords: web, development, like

OVERALL STATISTICS:
Total files analyzed: 4
Total exchanges: 31
Total user messages: 31
Total AI messages: 31
Most common keywords across all files:
  1. data (appears in 2 analyses)
  2. project (appears in 2 analyses)
  3. python (appears in 2 analyses)
  4. skill (appears in 1 analyses)
  5. scientist (appears in 1 analyses)
```

## Command Options

| Command | Description |
|---------|-------------|
| `chat.txt` | Input file path |
| `--basic` | Use frequency analysis instead of TF-IDF |
| `--no-nltk` | Disable NLTK, use basic text processing |
| `--multiple` | Analyze multiple files in folder |
| `--output` | Save results to file |

## Technical Features

- **TF-IDF Algorithm**: Mathematical keyword relevance scoring
- **Automatic Fallback**: Works without NLTK installation
- **Topic Categorization**: AI, Programming, Data Science, Education
- **Multi-line Support**: Handles complex conversation formats
- **Error Handling**: Robust file processing and validation

## Performance Modes

### Enhanced Mode (Default)
- NLTK tokenization and lemmatization
- 179+ stop words filtering
- Root form keyword extraction
- Higher accuracy results

### Basic Mode (`--no-nltk`)
- Simple text processing
- 65+ stop words filtering
- Faster processing
- No external dependencies

### Frequency Mode (`--basic`)
- Word frequency counting
- No TF-IDF mathematical scoring
- Simpler keyword extraction

## Analysis Method Comparison

The tool shows different results based on the analysis method:

- **TF-IDF Analysis**: Identifies contextually important terms with mathematical scoring
- **Frequency Analysis**: Shows most commonly used words across the conversation
- **Multiple Files**: Provides comprehensive analysis across chat log collections

## Project Structure

```
ai-chat-log-summarizer/
├── main.py                     # Main executable script
├── chat_analyzer.py            # Main analyzer orchestrator
├── text_processor.py           # Text preprocessing module
├── chat_parser.py              # Chat log parsing module
├── keyword_extractor.py        # TF-IDF and frequency analysis
├── topic_analyzer.py           # Topic classification module
├── summary_generator.py        # Report generation module
├── chat_logs/                  # Folder containing multiple chat files
│   ├── ml_conversation.txt     # Machine learning discussion
│   ├── web_development.txt     # Web development chat
│   ├── python_help.txt         # Python programming help
│   └── data_science.txt        # Data science conversation
├── requirements.txt            # Optional dependencies (nltk)
└── README.md                   # This documentation
```

### File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Main script entry point with CLI |
| `chat_analyzer.py` | Main orchestrator combining all modules |
| `text_processor.py` | Text preprocessing and NLTK handling |
| `chat_parser.py` | Chat log file parsing functionality |
| `keyword_extractor.py` | TF-IDF and frequency analysis |
| `topic_analyzer.py` | Topic classification and categorization |
| `summary_generator.py` | Report and summary generation |
| `chat_logs/` | Folder containing multiple chat files for batch analysis |
| `*.txt` files | Individual chat conversations |
| `requirements.txt` | NLTK dependency (optional) |
| `README.md` | Complete documentation |

## Quick Test

```bash
# Test with sample file
python main.py chat.txt

# Compare different modes
python main.py chat.txt --basic
python main.py chat.txt --no-nltk

# Test multiple file analysis
python main.py chat_logs/ --multiple
```

## License

MIT License - Open source and free to use.
