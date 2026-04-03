class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        """
        Find the maximum number of walls that can be covered by robots.
        Each robot at position robots[i] can move distance[i] units left or right.
      
        Args:
            robots: List of robot positions
            distance: List of maximum distances each robot can move
            walls: List of wall positions
      
        Returns:
            Maximum number of walls that can be covered
        """
        n = len(robots)
      
        # Sort robots by position and pair with their distances
        robot_distance_pairs = sorted(zip(robots, distance), key=lambda x: x[0])
      
        # Sort walls for binary search
        walls.sort()
      
        @cache
        def dp(robot_idx: int, prev_robot_moved_right: int) -> int:
            """
            Dynamic programming function to find max walls covered.
          
            Args:
                robot_idx: Current robot index being processed
                prev_robot_moved_right: 0 if previous robot moved left, 1 if moved right
          
            Returns:
                Maximum walls that can be covered from robots 0 to robot_idx
            """
            # Base case: no robots left to process
            if robot_idx < 0:
                return 0
          
            current_pos = robot_distance_pairs[robot_idx][0]
            current_distance = robot_distance_pairs[robot_idx][1]
          
            # Option 1: Current robot moves left
            left_boundary = current_pos - current_distance
          
            # Ensure no overlap with previous robot if it exists
            if robot_idx > 0:
                prev_pos = robot_distance_pairs[robot_idx - 1][0]
                left_boundary = max(left_boundary, prev_pos + 1)
          
            # Count walls covered when moving left
            left_wall_idx = bisect_left(walls, left_boundary)
            right_wall_idx = bisect_left(walls, current_pos + 1)
            walls_covered_left = dp(robot_idx - 1, 0) + right_wall_idx - left_wall_idx
          
            # Option 2: Current robot moves right
            right_boundary = current_pos + current_distance
          
            # Ensure no overlap with next robot if it exists
            if robot_idx + 1 < n:
                next_pos = robot_distance_pairs[robot_idx + 1][0]
                next_distance = robot_distance_pairs[robot_idx + 1][1]
              
                if prev_robot_moved_right == 0:
                    # Next robot can move left, so adjust boundary
                    right_boundary = min(right_boundary, next_pos - next_distance - 1)
                else:
                    # Next robot cannot move left, must stay at position or move right
                    right_boundary = min(right_boundary, next_pos - 1)
          
            # Count walls covered when moving right
            left_wall_idx = bisect_left(walls, current_pos)
            right_wall_idx = bisect_left(walls, right_boundary + 1)
            walls_covered_right = dp(robot_idx - 1, 1) + right_wall_idx - left_wall_idx
          
            # Return maximum of both options
            return max(walls_covered_left, walls_covered_right)
      
        # Start from the last robot, assuming it can move right
        return dp(n - 1, 1)