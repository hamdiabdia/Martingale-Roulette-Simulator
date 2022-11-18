# Martingale Roulette Strategy Simulator

## Tools Utilized

* VSCode
* Python 3.8.5

### Python Libraries

* NumPy
* Matplotlib

###  Martingale Strategy in American Roulette Wheel

The martingale strategy in American Roulette is where you start with a low bet, typically $1 and every time 

Win Probability in an American Roulette Wheel is 18/38, since we have an 18 out of 38 chance of either landing in red or black if we happen to choose only one of them. 

####  Unlimited Bankroll

If `has_bankroll` is `False` then the following conditions will take place

* keep playing until I have reach 100 wins

####  Limited Bankroll

If `has_bankroll` is `True` then the following conditions will take place

* The conditions prior to unlimited bankroll will still be in place
* Our current bank roll amount is 256
    * if we win add `bet_amount` to our bank roll
    * if we lose, keep playing until bet amount is greater than bankroll and just go all in

## Installation 

```
pip3 install numpy
```

```
pip3 install matplotlib
```
### Findings

These are some of the findings I have noticed while making this simulator

* The martingale strategy is more successful if you have more money, so unlimited bankroll is the ideal condition for this strategy

### Images

Here are some of the results from the program:
