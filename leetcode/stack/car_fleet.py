class Solution:
    def carFleet(self, target, position, speed):
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []
        
        for car in cars:
            car_time = (target - car[0]) / car[1]
            if not stack:
                stack.append(car_time)
            else:
                fleet_time = stack[-1]
                if car_time > fleet_time:
                    stack.append(car_time)

        return len(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))