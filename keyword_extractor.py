import math
from collections import Counter, defaultdict
from typing import List, Tuple
from text_processor import TextProcessor


class KeywordExtractor:
    """Class for extracting keywords from text using various methods."""
    
    def __init__(self, text_processor: TextProcessor):
        """Initialize with a text processor instance."""
        self.text_processor = text_processor
    
    def calculate_tf_idf(self, documents: List[str], top_n: int = 5) -> List[Tuple[str, float]]:
        """Calculate TF-IDF scores for keywords across documents."""
        if not documents:
            return []
        
        processed_docs = [self.text_processor.preprocess_text(doc) for doc in documents]
        doc_freq = defaultdict(int)
        
        for doc in processed_docs:
            for term in set(doc):
                doc_freq[term] += 1
        
        tfidf_scores = defaultdict(float)
        num_docs = len(processed_docs)
        
        for doc in processed_docs:
            term_freq = Counter(doc)
            doc_length = len(doc)
            
            for term in set(doc):
                tf = term_freq[term] / doc_length if doc_length > 0 else 0
                idf = math.log(num_docs / doc_freq[term]) if doc_freq[term] > 0 else 0
                tfidf_scores[term] += tf * idf
        
        return sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    def extract_keywords_basic(self, text_list: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
        """Basic keyword extraction using frequency analysis."""
        all_tokens = []
        for text in text_list:
            all_tokens.extend(self.text_processor.preprocess_text(text))
        
        return Counter(all_tokens).most_common(top_n)
    
    def extract_keywords(self, text_list: List[str], top_n: int = 5, 
                        use_tfidf: bool = True) -> List[Tuple[str, float]]:
        """Extract keywords using either TF-IDF or basic frequency analysis."""
        if use_tfidf and len(text_list) > 1:
            return self.calculate_tf_idf(text_list, top_n)
        
        freq_results = self.extract_keywords_basic(text_list, top_n)
        return [(word, float(freq)) for word, freq in freq_results]