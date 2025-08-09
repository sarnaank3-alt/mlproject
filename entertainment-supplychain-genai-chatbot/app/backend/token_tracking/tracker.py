from datetime import datetime
import logging

class TokenTracker:
    def __init__(self):
        self.token_usage = {}
        logging.basicConfig(level=logging.INFO)

    def track_tokens(self, user_id, session_id, tokens_prompt, tokens_response):
        total_tokens = tokens_prompt + tokens_response
        timestamp = datetime.utcnow().isoformat()

        if user_id not in self.token_usage:
            self.token_usage[user_id] = []

        self.token_usage[user_id].append({
            'session_id': session_id,
            'timestamp': timestamp,
            'tokens_prompt': tokens_prompt,
            'tokens_response': tokens_response,
            'total_tokens': total_tokens
        })

        logging.info(f"Tracked tokens for user {user_id}: {total_tokens} tokens in session {session_id}")

    def get_usage(self, user_id):
        return self.token_usage.get(user_id, [])

    def reset_usage(self, user_id):
        if user_id in self.token_usage:
            del self.token_usage[user_id]
            logging.info(f"Reset token usage for user {user_id}")