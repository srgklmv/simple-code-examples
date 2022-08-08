import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs.keys():
            for _ in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, num):
        list_of_balls = []
        for _ in range(num):
            try:
                list_of_balls.append(self.contents.pop(random.randrange(len(self.contents))))
            except:
                break
        return list_of_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    successful = 0
    experiment_dict = {}
    ball_in_hat = 0

    for _ in range(num_experiments):
        start_hat = hat.contents.copy()
        balls = hat.draw(num_balls_drawn)
        for ball in balls:
            experiment_dict[ball] = experiment_dict.setdefault(ball, 0) + 1
        for key in expected_balls.keys():
            if key in experiment_dict.keys() and expected_balls[key] <= experiment_dict[key]:
                ball_in_hat += 1
            else:
                break
        if ball_in_hat == len(expected_balls):
            successful += 1
        ball_in_hat = 0
        experiment_dict.clear()
        hat.contents = start_hat.copy()

    probability = successful / num_experiments

    return probability



