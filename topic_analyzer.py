from typing import Dict, List, Tuple, Set

class TopicAnalyzer: 
    def __init__(self):
        self.topic_categories = {
            "programming": {
                'python', 'code', 'programming', 'development', 'software', 'algorithm', 
                'function', 'variable', 'loop', 'class', 'method', 'library', 'framework'
            },
            "artificial_intelligence": {
                'ai', 'machine', 'learning', 'artificial', 'intelligence', 'model', 
                'neural', 'network', 'deep', 'training', 'prediction', 'classification'
            },
            "data_science": {
                'data', 'analysis', 'statistics', 'dataset', 'pandas', 'numpy', 
                'visualization', 'graph', 'chart', 'correlation', 'pattern'
            },
            "education": {
                'learn', 'study', 'explain', 'understand', 'help', 'question', 
                'answer', 'tutorial', 'course', 'practice', 'example'
            }
        }
    
    def analyze_conversation_topics(self, keywords: List[Tuple[str, float]]) -> Dict[str, List[str]]:
        if not keywords:
            return {"general": []}
        
        top_words = [word.lower() for word, score in keywords]
        result = {}
        
        for word in top_words:
            for topic, topic_keywords in self.topic_categories.items():
                if word in topic_keywords:
                    if topic not in result:
                        result[topic] = []
                    result[topic].append(word)
        
        return result if result else {"general": top_words[:3]}
    
    def add_topic_category(self, topic_name: str, keywords: Set[str]) -> None:
        self.topic_categories[topic_name] = keywords
