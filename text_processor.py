import string
from typing import List

NLTK_AVAILABLE = False
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
    
    try:
        stopwords.words('english')
        word_tokenize("test")
        WordNetLemmatizer().lemmatize("test")
        NLTK_AVAILABLE = True
    except LookupError:
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
            nltk.download('wordnet', quiet=True)
            nltk.download('omw-1.4', quiet=True)
            NLTK_AVAILABLE = True
        except Exception:
            NLTK_AVAILABLE = False
except ImportError:
    NLTK_AVAILABLE = False


class TextProcessor:
    def __init__(self, use_nltk: bool = True):
        self.use_nltk = use_nltk and NLTK_AVAILABLE
        
        if self.use_nltk:
            self.stop_words = set(stopwords.words('english'))
            self.lemmatizer = WordNetLemmatizer()
        else:
            self.stop_words = {
                'the', 'is', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
                'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before', 'after',
                'above', 'below', 'between', 'among', 'a', 'an', 'as', 'are', 'was', 'were',
                'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
                'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her',
                'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'what',
                'where', 'when', 'why', 'how', 'which', 'who', 'whom', 'whose', 'if', 'so',
                'than', 'too', 'very', 'just', 'now', 'here', 'there', 'then', 'also',
                'only', 'other', 'some', 'any', 'each', 'every', 'all', 'both', 'few',
                'more', 'most', 'many', 'much', 'such', 'same', 'different', 'new', 'old',
                'first', 'last', 'long', 'great', 'little', 'own', 'right', 'big', 'high',
                'small', 'large', 'next', 'early', 'young', 'important', 'public', 'bad', 'able'
            }
    
    def preprocess_text(self, text: str) -> List[str]:
        if self.use_nltk:
            tokens = word_tokenize(text.lower())
            tokens = [token for token in tokens if token.isalpha() and len(token) > 2]
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
            return [token for token in tokens if token not in self.stop_words]
        else:
            translator = str.maketrans('', '', string.punctuation)
            clean_text = text.lower().translate(translator)
            words = clean_text.split()
            return [word for word in words if word not in self.stop_words and len(word) > 2]
    
    @property
    def is_nltk_available(self) -> bool:
        return self.use_nltk
