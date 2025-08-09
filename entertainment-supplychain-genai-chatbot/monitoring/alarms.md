# CloudWatch Alarms Documentation

This document outlines the CloudWatch alarms configured for monitoring the entertainment supply chain Generative AI chatbot. These alarms are essential for ensuring the reliability, performance, and security of the application.

## Alarms Overview

1. **Token Spikes Alarm**
   - **Purpose**: To monitor sudden increases in token usage, which may indicate unexpected behavior or abuse of the system.
   - **Metric**: `TokenUsage`
   - **Threshold**: Greater than 1000 tokens in a 5-minute period.
   - **Actions**: Notify the development team via SNS.

2. **Tool-Call Budget Exhaustion Alarm**
   - **Purpose**: To alert when a user exceeds their tool-call budget, ensuring compliance with business rules.
   - **Metric**: `ToolCallsCount`
   - **Threshold**: Equal to or greater than 25 tool calls in a single session.
   - **Actions**: Trigger a notification to the support team.

3. **RDS Failover Alarm**
   - **Purpose**: To detect when the RDS instance is unavailable, allowing for quick response to potential outages.
   - **Metric**: `RDSInstanceStatus`
   - **Threshold**: Status changes to `Unavailable`.
   - **Actions**: Notify the operations team and initiate failover procedures.

4. **High Latency Alarm**
   - **Purpose**: To monitor the latency of API responses, ensuring that the user experience remains optimal.
   - **Metric**: `APILatency`
   - **Threshold**: Greater than 2 seconds for 95th percentile latency over a 5-minute period.
   - **Actions**: Notify the performance engineering team.

5. **Error Rate Alarm**
   - **Purpose**: To track the rate of errors occurring in the application, which may indicate underlying issues.
   - **Metric**: `ErrorCount`
   - **Threshold**: Greater than 5 errors in a 1-minute period.
   - **Actions**: Trigger an alert to the development team for immediate investigation.

## Alarm Configuration

Each alarm is configured in the CloudWatch console with the specified metrics, thresholds, and actions. Regular reviews of alarm settings and performance metrics are recommended to ensure they remain aligned with application needs and user expectations.

## Conclusion

These CloudWatch alarms play a critical role in maintaining the health and performance of the Generative AI chatbot. By monitoring key metrics and responding to alerts, the team can proactively address issues and enhance the user experience.