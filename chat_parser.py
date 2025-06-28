from typing import Dict


class ChatParser:
    def parse_chat_log(self, file_path: str) -> Dict:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        chat_data = {
            'user_messages': [],
            'ai_messages': [],
            'total_exchanges': 0,
            'all_text': []
        }
        
        lines = content.strip().split('\n')
        current_speaker = None
        current_message = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('User:'):
                if current_speaker and current_message:
                    message_text = ' '.join(current_message)
                    self._add_message(chat_data, current_speaker, message_text)
                
                current_speaker = 'user'
                current_message = [line[5:].strip()]
                
            elif line.startswith('AI:'):
                if current_speaker and current_message:
                    message_text = ' '.join(current_message)
                    self._add_message(chat_data, current_speaker, message_text)
                
                current_speaker = 'ai'
                current_message = [line[3:].strip()]
                
            else:
                if current_speaker:
                    current_message.append(line)
        
        if current_speaker and current_message:
            message_text = ' '.join(current_message)
            self._add_message(chat_data, current_speaker, message_text)
        
        chat_data['total_exchanges'] = min(len(chat_data['user_messages']), 
                                         len(chat_data['ai_messages']))
        return chat_data
    
    def _add_message(self, chat_data: Dict, speaker: str, message: str) -> None:
        if speaker == 'user':
            chat_data['user_messages'].append(message)
        else:
            chat_data['ai_messages'].append(message)
        chat_data['all_text'].append(message)
