class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ball_hash = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for char in text: 
            if char in ball_hash: 
                ball_hash[char] += 1
            
        ball_hash['o'] =  ball_hash['o'] // 2
        ball_hash['l'] =  ball_hash['l'] // 2
        
        instances = min(ball_hash.values())
        
        return instances
        
        
        
        #         ball_hash = {'b': 1, 'a': 2, 'l': 10, 'o': 2, 'n': 2}

    
    # see ur vs code for notes
                
                