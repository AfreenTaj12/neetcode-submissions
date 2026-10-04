class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Step 1: Buy an empty storage cabinet
        baskets = {}
        
        # Step 2: Look at each word in our input list one by one
        for word in strs:
            
            # Step 2a: Sort the letters of the word to create the drawer label
            # Example: "tea" -> sorted turns it into ['a', 'e', 't']
            # "".join() glues it back into a string -> "aet"
            sorted_label = "".join(sorted(word))
            
            # Step 3: Does this drawer label already exist in our cabinet?
            if sorted_label in baskets:
                # YES! Open that drawer and append the word inside the list
                baskets[sorted_label].append(word)
            else:
                # NO! Create a brand new drawer with that label and add the word
                baskets[sorted_label] = [word]
                
        # Step 4: The loop is done. Grab ONLY the lists inside the drawers
        return list(baskets.values())

        
            