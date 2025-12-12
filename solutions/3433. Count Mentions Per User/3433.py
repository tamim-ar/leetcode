from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        """
        Count the number of mentions for each user based on events.
      
        Args:
            numberOfUsers: Total number of users in the system
            events: List of events, each containing [event_type, timestamp, data]
                   - "OFFLINE": User goes offline
                   - "MESSAGE": Message event with mentions
                   - Other events may include "ALL" mentions or "HERE" mentions
      
        Returns:
            List of mention counts for each user
        """
        # Sort events by timestamp (as integer), then by event type priority
        # The [2] index suggests prioritizing certain event types over others
        events.sort(key=lambda event: (int(event[1]), event[0][2]))
      
        # Initialize mention count for each user
        mention_counts = [0] * numberOfUsers
      
        # Track when each user will be online until (offline at timestamp + 60)
        online_until = [0] * numberOfUsers
      
        # Counter for "ALL" mentions that will be applied to all users later
        all_mentions_count = 0
      
        # Process each event in chronological order
        for event_type, timestamp_str, data in events:
            current_time = int(timestamp_str)
          
            # Check the first character of event type to determine action
            if event_type[0] == "O":  # "OFFLINE" event
                # User goes offline, but remains available for mentions for 60 time units
                user_id = int(data)
                online_until[user_id] = current_time + 60
              
            elif data[0] == "A":  # "ALL" mention
                # Increment counter for mentions that affect all users
                all_mentions_count += 1
              
            elif data[0] == "H":  # "HERE" mention
                # Mention all users who are currently online
                for user_id, offline_time in enumerate(online_until):
                    if offline_time <= current_time:  # User is online
                        mention_counts[user_id] += 1
                      
            else:  # Specific user mentions
                # Parse space-separated user IDs (format: "id:X id:Y ...")
                for mention in data.split():
                    # Extract user ID from format "id:123"
                    user_id = int(mention[2:])
                    mention_counts[user_id] += 1
      
        # Apply "ALL" mentions to every user
        if all_mentions_count:
            for user_id in range(numberOfUsers):
                mention_counts[user_id] += all_mentions_count
              
        return mention_counts