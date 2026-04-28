class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # sort position in decending order
        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            
            if not stack:
                stack.append(time)

            elif time > stack[-1]:
                stack.append(time)
            else:
                pass # joins the previous car

        return len(stack)


