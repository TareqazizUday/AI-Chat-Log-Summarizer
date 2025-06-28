import os
from collections import Counter
from typing import Dict, List
from text_processor import TextProcessor
from chat_parser import ChatParser
from keyword_extractor import KeywordExtractor
from topic_analyzer import TopicAnalyzer
from summary_generator import SummaryGenerator


class ChatLogAnalyzer:
    def __init__(self, use_nltk: bool = True):
        """Initialize the analyzer with all required components."""
        self.text_processor = TextProcessor(use_nltk=use_nltk)
        self.chat_parser = ChatParser()
        self.keyword_extractor = KeywordExtractor(self.text_processor)
        self.topic_analyzer = TopicAnalyzer()
        self.summary_generator = SummaryGenerator(self.topic_analyzer)
    
    def analyze_single_file(self, file_path: str, use_tfidf: bool = True) -> str:
        try:
            chat_data = self.chat_parser.parse_chat_log(file_path)
            keywords = self.keyword_extractor.extract_keywords(chat_data['all_text'], use_tfidf=use_tfidf)
            return self.summary_generator.generate_summary(chat_data, keywords, use_tfidf, self.text_processor.is_nltk_available)
        except Exception as e:
            return f"Error analyzing {file_path}: {str(e)}"
    
    def analyze_multiple_files(self, folder_path: str, use_tfidf: bool = True) -> str:
        if not os.path.isdir(folder_path):
            return f"Error: {folder_path} is not a valid directory"
        
        txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if not txt_files:
            return f"No .txt files found in {folder_path}"
        
        file_results = []
        all_keywords = []
        total_exchanges = total_user_msgs = total_ai_msgs = 0
        
        for filename in txt_files:
            file_path = os.path.join(folder_path, filename)
            file_result = {
                'filename': filename,
                'error': None,
                'exchanges': 0,
                'user_messages': 0,
                'ai_messages': 0,
                'keywords': []
            }
            
            try:
                chat_data = self.chat_parser.parse_chat_log(file_path)
                keywords = self.keyword_extractor.extract_keywords(chat_data['all_text'], use_tfidf=use_tfidf)
                
                file_result.update({
                    'exchanges': chat_data['total_exchanges'],
                    'user_messages': len(chat_data['user_messages']),
                    'ai_messages': len(chat_data['ai_messages']),
                    'keywords': keywords
                })
                
                total_exchanges += chat_data['total_exchanges']
                total_user_msgs += len(chat_data['user_messages'])
                total_ai_msgs += len(chat_data['ai_messages'])
                all_keywords.extend([word for word, score in keywords])
                
            except Exception as e:
                file_result['error'] = str(e)
            
            file_results.append(file_result)
        
        overall_stats = {
            'total_files': len(txt_files),
            'total_exchanges': total_exchanges,
            'total_user_msgs': total_user_msgs,
            'total_ai_msgs': total_ai_msgs,
            'common_keywords': Counter(all_keywords).most_common(5) if all_keywords else []
        }
        
        return self.summary_generator.generate_multi_file_summary(file_results, overall_stats)
    
    def save_summary(self, summary: str, output_path: str) -> bool:
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summary)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
