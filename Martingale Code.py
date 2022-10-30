import numpy as np
import matplotlib.pyplot as plt
	  		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def get_spin(win_prob):  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, 
    the function returns whether the probability will result in a win.	
    true for a win, false for a loss 	   		  	  		  		  		    	 		 		   		 		  
    """
    result = False
    bet = np.random.random()
    if bet <= win_prob:
        result = True  		  	   		  	  		  		  		    	 		 		   		 		  
    return result

#function that would run all of our experiments
def run_experiments():
    win_prob = 18/38  #probability of a win according to an American Roulette wheel
    #30 Episodes of American Roulette
    monte_carlo_sim(30, win_prob, False)

    unlimited_mean(1000, win_prob)
    unlimited_median(1000, win_prob)

    limited_mean(1000, win_prob)
    limited_median(1000, win_prob)


def roulette_simulator(win_prob, has_bankroll):
    winnings = 100
    res = np.full((1001),winnings)
    episode_winnings = 0
    total_episodes = 0       #to keep track of number of episodes
    money = 256            #Money for more realistic gambling experiment
    win_counter = 0

    while episode_winnings < winnings and total_episodes < 1000:
        won = False
        bet_amount = 1 #the intial bet amount is always a dollar at the start of an episode
        while not won: #while you haven't won, keep playing
            won = get_spin(win_prob)
            if won == True:
                episode_winnings += bet_amount
                win_counter+=1
            else:
                episode_winnings -= bet_amount
                bet_amount = bet_amount * 2
                if has_bankroll == True:
                    if episode_winnings == -money:
                        res[total_episodes:] = episode_winnings
                        return res
                    #if my bet is more than what I currently have, just go all in
                    if episode_winnings - bet_amount < -money:
                        bet_amount = episode_winnings + money
            res[total_episodes] = episode_winnings
            total_episodes+=1

    return res

def monte_carlo_sim(episodes, win_prob, has_bankroll):

    total_episodes = 0
    plt.axis([0,275,-300,200])
    plt.title('30 Episodes of American Roulette with unlimited Money')
    plt.ylabel('Winnings')
    plt.xlabel('Bets')

    while total_episodes < episodes:
        current_episode = roulette_simulator(win_prob, has_bankroll)
        plt.plot(current_episode)
        total_episodes += 1

    plt.savefig('images/figure1')

    plt.show()

def unlimited_mean(episodes, win_prob):

    total_episodes = 0

    plt.axis([0,300,-350,500])
    plt.ylabel('Winnings')
    plt.xlabel('Bets')
    res = np.zeros((1000,1001))

    plt.title('Mean of Winning with Unlimited Money')

    while total_episodes < episodes:

        current_episode = roulette_simulator(win_prob, False)
        res[total_episodes] = current_episode
        total_episodes+=1

    mean = np.mean(res, axis = 0)
    std = np.std(res, axis = 0)
    mean_pus = mean + std
    mean_minus = mean- std


    plt.plot(mean, label = "mean")
    plt.plot(mean_pus, label = "mean + stdev")
    plt.plot(mean_minus, label = "mean - stdev")

    plt.legend()
    plt.show()

def limited_mean(episodes, win_prob):

    total_episodes = 0

    plt.axis([0,200,-256,200])
    plt.ylabel('Winnings')
    plt.xlabel('Bets')
    res = np.zeros((1000,1001))

    plt.title('Mean of Winning with Limited Money')

    while total_episodes < episodes:

        current_episode = roulette_simulator(win_prob, True)
        res[total_episodes] = current_episode
        total_episodes+=1

    mean = np.mean(res, axis = 0)
    std = np.std(res, axis = 0)
    mean_pus = mean + std
    mean_minus = mean- std


    plt.plot(mean, label = "mean")
    plt.plot(mean_pus, label = "mean + stdev")
    plt.plot(mean_minus, label = "mean - stdev")

    plt.legend()
    plt.show()

def unlimited_median(episodes, win_prob):

    total_episodes = 0

    plt.axis([0,300,-350,500])
    plt.ylabel('Winnings')
    plt.xlabel('Bets')
    res = np.zeros((1000,1001))

    plt.title('Median of Winning with Unlimited Money')

    while total_episodes < episodes:
        current_episode = roulette_simulator(win_prob, False)
        res[total_episodes] = current_episode
        total_episodes+=1

    median = np.median(res, axis = 0)
    stdev = np.std(res, axis = 0)
    median_plus = median + stdev
    median_minus = median- stdev

    plt.plot(median, label = "mean")
    plt.plot(median_plus, label = "mean + stdev")
    plt.plot(median_minus, label = "mean - stdev")

    plt.legend()
    plt.show()

def limited_median(episodes, win_prob):

    total_episodes = 0

    plt.axis([0,300,-200,300])
    plt.ylabel('Winnings')
    plt.xlabel('Bets')
    res = np.zeros((1000,1001))

    plt.title('Median of Winning with Limited Money')

    while total_episodes < episodes:
        current_episode = roulette_simulator(win_prob, True)
        res[total_episodes] = current_episode
        total_episodes+=1

    median = np.median(res, axis = 0)
    stdev = np.std(res, axis = 0)
    median_plus = median + stdev
    median_minus = median- stdev

    plt.plot(median, label = "mean")
    plt.plot(median_plus, label = "mean + stdev")
    plt.plot(median_minus, label = "mean - stdev")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_experiments()  		  	   		  	  		  		  		    	 		 		   		 		  
