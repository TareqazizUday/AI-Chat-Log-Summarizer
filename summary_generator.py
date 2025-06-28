from typing import Dict, List, Tuple
from topic_analyzer import TopicAnalyzer


class SummaryGenerator:
    def __init__(self, topic_analyzer: TopicAnalyzer):
        self.topic_analyzer = topic_analyzer
    
    def generate_summary(self, chat_data: Dict, keywords: List[Tuple[str, float]], 
                        use_tfidf: bool = True, use_nltk: bool = True) -> str:
        method = "TF-IDF" if use_tfidf else "Frequency Analysis"
        processing = "NLTK Enhanced" if use_nltk else "Basic Processing"
        
        summary = [
            "=" * 70,
            "                    CHAT LOG ANALYSIS SUMMARY",
            "=" * 70,
            "\nCONVERSATION STATISTICS:",
            f"  Total exchanges: {chat_data['total_exchanges']}",
            f"  User messages: {len(chat_data['user_messages'])}",
            f"  AI messages: {len(chat_data['ai_messages'])}",
            f"  Total messages: {len(chat_data['user_messages']) + len(chat_data['ai_messages'])}",
            f"\nANALYSIS METHOD:",
            f"  Keyword extraction: {method}",
            f"  Text processing: {processing}"
        ]

        if keywords:
            summary.append(f"\nTOP KEYWORDS ({method}):")
            for i, (word, score) in enumerate(keywords, 1):
                score_text = f"TF-IDF: {score:.3f}" if use_tfidf else f"Frequency: {int(score)}"
                summary.append(f"  {i}. {word.capitalize()} ({score_text})")

        topics = self.topic_analyzer.analyze_conversation_topics(keywords)
        if topics:
            summary.append("\nCONVERSATION TOPICS:")
            for topic, topic_keywords in topics.items():
                topic_name = topic.replace('_', ' ').title()
                keywords_str = ', '.join(topic_keywords)
                summary.append(f"  {topic_name}: {keywords_str}")
        
        summary.append("\n" + "=" * 70)
        return '\n'.join(summary)
    
    def generate_multi_file_summary(self, file_results: List[Dict], overall_stats: Dict) -> str:
        results = [
            f"ANALYSIS OF {len(file_results)} CHAT LOG FILES",
            "=" * 60
        ]
        
        for file_result in file_results:
            results.extend([
                f"\nFILE: {file_result['filename']}",
                "-" * 40
            ])
            
            if file_result['error']:
                results.append(f"Error: {file_result['error']}")
            else:
                results.extend([
                    f"Exchanges: {file_result['exchanges']}",
                    f"User messages: {file_result['user_messages']}",
                    f"AI messages: {file_result['ai_messages']}"
                ])
                
                if file_result['keywords']:
                    keyword_str = ', '.join([word for word, score in file_result['keywords'][:3]])
                    results.append(f"Top keywords: {keyword_str}")

        results.extend([
            "\nOVERALL STATISTICS:",
            f"Total files analyzed: {overall_stats['total_files']}",
            f"Total exchanges: {overall_stats['total_exchanges']}",
            f"Total user messages: {overall_stats['total_user_msgs']}",
            f"Total AI messages: {overall_stats['total_ai_msgs']}"
        ])
        
        if overall_stats['common_keywords']:
            results.append("Most common keywords across all files:")
            for i, (word, count) in enumerate(overall_stats['common_keywords'], 1):
                results.append(f"  {i}. {word} (appears in {count} analyses)")
        
        return '\n'.join(results)
