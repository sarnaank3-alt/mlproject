from datetime import datetime
import json

class ToolCallAccounting:
    def __init__(self, tool_call_limit=25):
        self.tool_call_limit = tool_call_limit
        self.tool_calls_count = 0
        self.logs = []

    def increment_tool_call(self, user_id, session_id):
        if self.tool_calls_count < self.tool_call_limit:
            self.tool_calls_count += 1
            self.log_tool_call(user_id, session_id)
            return True
        else:
            return False

    def log_tool_call(self, user_id, session_id):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "session_id": session_id,
            "tool_calls_count": self.tool_calls_count
        }
        self.logs.append(log_entry)

    def reset_tool_calls(self):
        self.tool_calls_count = 0

    def get_logs(self):
        return json.dumps(self.logs, indent=4)