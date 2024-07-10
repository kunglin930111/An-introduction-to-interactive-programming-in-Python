# Mini-project #1 - Rock-paper-scissor-lizard-Spock

Rock-paper-scissors is a hand game that is played by two people. The players count to three in unison and simultaneously "throw” one of three hand signals that correspond to rock, paper or scissors. The winner is determined by the rules:

Rock smashes scissors
Scissors cuts paper
Paper covers rock
Rock-paper-scissors is a surprisingly popular game that many people play seriously (see the 
Wikipedia article
 for details). Due to the fact that a tie happens around 1/3 of the time, several variants of Rock-Paper-Scissors exist that include more choices to make ties less likely.

Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". The 
Wikipedia entry
 for RPSLS gives the complete description of the details of the game.

In our first mini-project, we will build a Python function 
rpsls(name)
rpsls(name) that takes as input the string 
name
name, which is one of 
"rock"
"rock", 
"paper"
"paper", 
"scissors"
"scissors", 
"lizard"
"lizard", or 
"Spock"
"Spock". The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.

While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of 
if
if/
elif
elif/
else
else clauses in your mini-project code. A simpler method for determining the winner is to assign each of the five choices a number:

0 — rock
1 — Spock
2 — paper
3 — lizard
4 — scissors
In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).

In all of the mini-projects for this class, we will provide a walk through of the steps involved in building your project to aid its development. A template for your mini-project is 
available here
. Please work from this template.

# Mini-project #2 - "Guess the Number!"

One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in some known range while the second player attempts to guess the number. After each guess, the first player answers either “Higher”, “Lower” or “Correct!” depending on whether the secret number is higher, lower or equal to the guess. In this project, you will build a simple interactive program in Python where the computer will take the role of the first player while you play as the second player.

When discussing ranges in this mini-project, we will follow the standard Python convention of including the low end of the range and excluding the high end of the range. Mathematically, we will express ranges via the notation 
[low, high)
[low, high). The square bracket of the left of the range indicates that the corresponding bound should be included. The left parenthesis on the right of the range indicates that corresponding bound should be excluded. For example, the range 
[0, 3)
[0, 3) consists of numbers starting at 0 up to, but not including 3. In other words 0, 1, and 2.

You will interact with your program using an input field and several buttons. For this project, we will ignore the canvas and print the computer's responses in the console. Building an initial version of your project that prints information in the console is a development strategy that you should use in later projects as well. Focusing on getting the logic of the program correct before trying to make it display the information in some “nice” way on the canvas usually saves lots of time since debugging logic errors in graphical output can be tricky.

# Mini-project #3 - Stopwatch: The Game

Our mini-project for this week will focus on combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons. To help guide you through this project, we suggest that you download the provided 
program template


# Mini-project #4 - Pong

In this project, we will build a version of 
Pong
, one of the first arcade video games (1972). While Pong is not particularly exciting compared to today's video games, Pong is relatively simple to build and provides a nice opportunity to work on the skills that you will need to build a game like Asteroids. As usual, we have provided a 
program template
 that can be used to guide your development of Pong.


# Mini-project #5 - Memory

Memory is a card game in which the player deals out a set of cards face down. In Memory, a turn (or a move) consists of the player flipping over two cards. If they match, the player leaves them face up. If they don't match, the player flips the cards back face down. The goal of Memory is to end up with all of the cards flipped face up in the minimum number of turns. For this project, we will keep our model for Memory fairly simple. A Memory deck consists of eight pairs of matching cards.


# Mini-project #6 - Blackjack

Blackjack is a simple, popular card game that is played in many casinos. Cards in Blackjack have the following values: an ace may be valued as either 1 or 11 (player's choice), face cards (kings, queens and jacks) are valued at 10 and the value of the remaining cards corresponds to their number. During a round of Blackjack, the players plays against a dealer with the goal of building a hand (a collection of cards) whose cards have a total value that is higher than the value of the dealer's hand, but not over 21.  (A round of Blackjack is also sometimes referred to as a hand.)

The game logic for oursimplified version of Blackjack is as follows. The player and the dealer are each dealt two cards initially with one of the dealer's cards being dealt faced down (his hole card). The player may then ask for the dealer to repeatedly "hit" his hand by dealing him another card. If, at any point, the value of the player's hand exceeds 21, the player is "busted" and loses immediately. At any point prior to busting, the player may "stand" and the dealer will then hit his hand until the value of his hand is 17 or more. (For the dealer, aces count as 11 unless it causes the dealer's hand to bust). If the dealer busts, the player wins. Otherwise, the player and dealer then compare the values of their hands and the hand with the higher value wins. The dealer wins ties in our version.

# Mini Project #7 - Spaceship

In our last two mini-projects, we will build a 2D space game RiceRocks that is inspired by the classic arcade game Asteroids (1979). Asteroids is a relatively simple game by today's standards, but was still immensely popular during its time. (Joe spent countless quarters playing it.) In the game, the player controls a spaceship via four buttons: two buttons that rotate the spaceship clockwise or counterclockwise (independent of its current velocity), a thrust button that accelerates the ship in its forward direction and a fire button that shoots missiles. Large asteroids spawn randomly on the screen with random velocities. The player's goal is to destroy these asteroids before they strike the player's ship. In the arcade version, a large rock hit by a missile split into several fast moving small asteroids that themselves must be destroyed. Occasionally, a flying saucer also crosses the screen and attempts to destroy the player's spaceship. Searching for "asteroids arcade" yields links to multiple versions of Asteroids that are available on the web (including an updated version by Atari, the original creator of Asteroids).

# Mini Project #8 - RiceRocks 

For our last mini-project, we will complete the implementation of RiceRocks, an updated version of Asteroids,  that we began last week.  You may start with either your code or the 
program template
 which includes a full implementation of Spaceship and will be released immediately after the deadline for the Spaceship mini-project (by making the preceding link live).  If you start with your own code, you should add the splash screen image that you dismiss with a mouse click before starting this mini-project.  We strongly recommend using Chrome for this mini-project since Chrome's superior performance will become apparent when your program attempts to draw dozens of sprites.
 
