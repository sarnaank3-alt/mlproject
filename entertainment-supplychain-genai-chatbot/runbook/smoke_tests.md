# Smoke Tests for Entertainment Supply Chain GenAI Chatbot

## Overview
This document outlines the smoke tests designed to validate the basic functionality of the Entertainment Supply Chain Generative AI Chatbot. These tests ensure that the core components of the system are operational and can handle expected interactions.

## Smoke Test Cases

### 1. Chatbot Initialization
- **Objective**: Verify that the chatbot initializes correctly.
- **Steps**:
  1. Start the Streamlit UI.
  2. Check that the UI loads without errors.
  3. Ensure that the chatbot is responsive.
- **Expected Result**: The chatbot should be fully operational and ready to accept user input.

### 2. Basic Query Handling
- **Objective**: Test the chatbot's ability to handle a simple query.
- **Steps**:
  1. Input a basic query (e.g., "What are the rights management processes?").
  2. Submit the query.
- **Expected Result**: The chatbot should return a relevant answer with proper citation.

### 3. Tool Call Limit Enforcement
- **Objective**: Ensure that the tool call limit is enforced correctly.
- **Steps**:
  1. Simulate a session where the user makes 25 tool calls.
  2. Attempt to make a 26th tool call.
- **Expected Result**: The chatbot should deny the request and inform the user of the tool call limit.

### 4. SQL Agent Functionality
- **Objective**: Validate the SQL agent's ability to execute safe queries.
- **Steps**:
  1. Input a query that requires database access (e.g., "Get the list of active projects.").
  2. Submit the query.
- **Expected Result**: The SQL agent should return the correct data without executing any unsafe commands.

### 5. RDS Failover Handling
- **Objective**: Test the system's response to RDS unavailability.
- **Steps**:
  1. Simulate an RDS failure.
  2. Attempt to retrieve data that would normally require RDS access.
- **Expected Result**: The system should serve read-only data from the latest S3 snapshot and display a graceful message for write attempts.

### 6. Feedback Collection
- **Objective**: Verify that user feedback is collected correctly.
- **Steps**:
  1. After receiving a response, provide feedback (e.g., "Did this answer help?").
  2. Submit the feedback.
- **Expected Result**: The feedback should be recorded in the database with a reference to the session.

### 7. Monitoring and Logging
- **Objective**: Ensure that monitoring and logging are functioning as expected.
- **Steps**:
  1. Perform various interactions with the chatbot.
  2. Check CloudWatch for logs related to token usage, latency, and tool call counts.
- **Expected Result**: All interactions should be logged correctly, and metrics should reflect the activity.

## Conclusion
These smoke tests are essential for ensuring that the Entertainment Supply Chain Generative AI Chatbot operates as intended. Regular execution of these tests will help maintain system integrity and performance.