![pQ9YzVY](https://github.com/Demonware023/alx-system_engineering-devops/assets/134267322/69cfad98-3575-4e37-a3b1-d2a69c99ed71)

Incident Report: API Query Overload Outage

Issue Summary

On June 2, 2024, from 2:00 PM to 2:45 PM PST, our API infrastructure experienced a significant outage. During this period, our backend was overwhelmed by excessive requests, causing slow responses and timeouts for all users. Approximately 90% of our user base was affected, experiencing delays in page loads and failures in retrieving data. The root cause was identified as an excessive number of queries (100 per page request) being sent to the backend for each page requested by users.

Timeline
1:50 PM: Configuration change deployed to improve user data fetching efficiency.
2:00 PM: Outage begins, with a noticeable slowdown in response times.
2:02 PM: Monitoring alerts triggered, indicating high server load and increased response times.
2:05 PM: Engineers begin investigation, assuming a temporary traffic spike.
2:10 PM: Initial investigation focuses on network traffic and server performance metrics.
2:20 PM: Misleading path taken by checking external API dependencies.
2:25 PM: Escalation to the backend engineering team.
2:30 PM: Root cause identified as a loop in the frontend code causing 100 queries per page request.
2:35 PM: Temporary fix implemented by throttling incoming requests.
2:45 PM: Full resolution achieved by rolling back the recent configuration change.
2:45 PM: 100% of traffic back online, with normal response times restored.


Root Cause and Resolution

The issue stemmed from a recent configuration change aimed at improving user data fetching efficiency. A bug in the frontend code caused each page request to trigger 100 queries to the backend instead of the intended single query. This overwhelmed the backend servers, causing a queue buildup and delayed responses.

Upon detection, the incident response team initially investigated network traffic and server performance, assuming a temporary traffic spike. This path was misleading as it did not identify the source of the excessive requests. The problem was escalated to the backend engineering team, which quickly identified the loop in the frontend code.

The immediate resolution involved throttling incoming requests to prevent further server overload. Subsequently, the recent configuration change was rolled back, and the frontend code was corrected to ensure only one query per page request. This rollback and fix restored normal operation by 2:45 PM PST.


Corrective and Preventative Measures

In response to this incident, several measures are being implemented to prevent future occurrences:

Review and Audit Configuration Changes: Implement a rigorous review process for configuration changes to catch potential bugs before deployment.

Enhanced Monitoring: Improve monitoring to detect unusual request patterns and spikes in query volume promptly.

Rate Limiting: Introduce rate limiting on the backend to prevent overload from excessive requests.

Staged Rollouts: Implement staged rollouts for configuration changes, starting in a testing environment before moving to production.

Automated Testing: Develop automated tests to simulate various load conditions and identify issues in the frontend and backend interaction.
Tasks to Address the Issue:

Patch Frontend Code: Fix the loop causing multiple queries per page request.

Implement Rate Limiting: Configure backend servers to limit the number of requests from a single client within a specified timeframe.

Review Configuration Deployment Process: Enhance the process to include a mandatory review and testing stage.

Improve Monitoring: Add detailed metrics for request patterns and server load to quickly identify anomalies.

Develop Load Testing Suite: Create automated tests to simulate high-load scenarios and ensure stability under stress.

Training for Engineers: Conduct training sessions to familiarize the engineering team with new processes and monitoring tools.

By implementing these corrective and preventative measures, we aim to improve the reliability and stability of our API infrastructure, ensuring a seamless experience for our users. We apologize for the inconvenience caused and appreciate the continued support of our users and developers.
