class StarShardCalculator:
    """
    Calculates the total required shards to reach the target star level.
    """
    @staticmethod
    def calculate_required_shards(full_stars: int, current_tier: int, target_star: int) -> int:
        if full_stars < 0 or full_stars > 4:
            raise ValueError("Current star must be between 0 and 4.")
        
        if target_star < 1 or target_star > 5:
            raise ValueError("Target star must be between 1 and 5.")
        
        if current_tier < 0 or current_tier > 5:
            raise ValueError("Current fragments must be between 0 and 5.")
        
        if target_star <= full_stars:
            raise ValueError("Target star must be greater than to the current star.")
        
        total_shards = 0
        
        # Shard costs per fragment for each star
        shard_cost_per_fragment = [5, 10, 20, 60, 100]
        
        # Complete the current star (remaining fragments)
        if full_stars <= 4:
            remaining_fragments = 5 - current_tier
            total_shards += remaining_fragments * shard_cost_per_fragment[full_stars]
            
            # Now we have filled one star virtually
            full_stars += 1
        
        # Calculate full shards for intermediate stars
        for i in range(full_stars + 1, target_star + 1):
            total_shards += 5 * shard_cost_per_fragment[i - 1]
        
        return total_shards