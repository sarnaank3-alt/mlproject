from flask import Flask, request, jsonify
from rag_pipeline.retrieval import retrieve_documents
from rag_pipeline.rerank import rerank_documents
from rag_pipeline.summarizer import summarize_text
from sql_agent.agent import SQLAgent
from tool_call.accounting import ToolCallAccounting
from token_tracking.tracker import TokenTracker
from metrics.endpoints import MetricsEndpoints
import config

app = Flask(__name__)

# Initialize components
sql_agent = SQLAgent()
tool_call_accounting = ToolCallAccounting()
token_tracker = TokenTracker()
metrics = MetricsEndpoints()

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    user_id = request.json.get('user_id')
    
    # Track tokens
    token_tracker.track_tokens(user_message)
    
    # Check tool call limits
    if not tool_call_accounting.check_limit(user_id):
        return jsonify({"error": "Tool call limit exceeded."}), 429
    
    # Retrieve documents
    retrieval_results = retrieve_documents(user_message)
    
    # Rerank documents if necessary
    reranked_results = rerank_documents(retrieval_results)
    
    # Generate a response
    response = summarize_text(reranked_results)
    
    # Log metrics
    metrics.log_metrics(user_id, response)
    
    return jsonify({"response": response})

@app.route('/api/sql', methods=['POST'])
def sql_query():
    query = request.json.get('query')
    user_id = request.json.get('user_id')
    
    # Execute SQL query
    result = sql_agent.execute_query(query)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)