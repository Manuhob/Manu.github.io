# Erwartungswert

## Abstract
In this note, we will discuss the concept of a random variable and its expected value. We will follow the format example $\rightarrow$ intuition $\rightarrow$ theory. We finish with an historic example.

## To answer a test at random

In a multiple option question with four options, and choosing the answer at random, we have
-  Probability to guess correctly: $P = 1/4$
-  Probability to guess incorrectly: $P = 3/4$. 

In the next Figure, we chose option (c), but the correct answer was (a)

| (a) | (b) | (c) | (d) |
| ---- | ---- | ---- | ---- | 
|0| |x| |

In the presence of two questions with four multiple options, in order to guess exactly one question, we must

1. Guess correctly the first and incorrectly the second: $P = (1/4) \times (3/4) = 0.1875$, 

| Inciso | (a) | (b) | (c) | (d) |
| --- | ---- | --- | --- | ---|
| 1.- | o x | | | |
| 2.- | | o | x | |

2. or guess incorrectly the first and correctly the second: $P = (3/4) \times (1/4) = 0.1875$

| Inciso | (a) | (b) | (c) | (d) |
| --- | ---- | --- | --- | ---|
| 1.- | o | x | | |
| 2.- | | o x | | |

having the total probability $2 \times (1/4) \times (3/4) = 0.375$ of guessing correctly exactly one question.
### Example

In a test with four questions of multiple option (four options each), and each correct exercise is worth 10 points, the probabilities of getting each score are:

| Number of rightly guessed exercises | Score | Probability | 
| --- | --- | --- |
| 0 | 0 | $(3/4)^4$ |
| 1 | 10 | $4 \times (1/4) \times (3/4)^3$ | 
| 2 | 20 | $6 \times (1/4)^2 \times (3/4)^2$ |
| 3 | 30 | $4 \times (1/4)^3 \times (3/4)$ |
| 4 | 40 | $(1/4)^4$ |

To obtain the **Expected Value**, we multiply each score times the probability of obtaining such score and add everything together. In the previous example, the expected value is:
$$  \mathbb{E} = 0 + 4.21875 + 4.21875 + 1.40625 + 0.15625 = 10.     $$
### Generalizating the example
In a more general case, where we have a test with n exercises. If we have a probability $p$ of guessing correctly each exercise ($p = 1/4$ in the previous example), then we have a probability $(1-p)$ of guessing incorrectly each exercise. If we want exactly $k$ correct exercises when guessing at random, we need
- Possible combinations of right-wrong guessings: ${n \choose k}$, 
- Probability of ocurrence in each combination: $p^k (1-p)^{n-k}$ .
So, the probability of guessing exactly $k$ exercises in an $n$-test scenario is ${n \choose k} p^k (1-p)^{n-k}$. The total probability is
$$ \sum_{k=0}^n {n \choose k} p^k(1-p)^{n-k} = (p + 1-p)^n = 1^n = 1.$$
This is called a [**Binomial distribution**](https://en.wikipedia.org/wiki/Binomial_distribution).

## Theoretic description

Here is a summary of the theoretic ingredients to compute the expected value of a random variable, comparing each step with the previous example.

1. **Set of events** $\Omega$. This is the set of possibilities of your random event.  
	*In the example, an event in $\Omega$ is making exactly one election of answers in each question. An event of this style would be to guess correctly the exercises $1)$, $2)$, $4)$ and guessing incorrectly the exercise $3)$.*

2. A **random variable** $X : \Omega \rightarrow \mathbb{R}$, which gives us a numeric value in a finite set $\{x_1,\cdots , x_r\}$, for each event in $\Omega$. It is called a random variable as it cannot be predicted.
	*In the example, the random variable $X$ is the score obtained for the corresponding choosing of random answers.*
        
3. A **probability distribution**, which for each value $x_j$, gives us the probability $0 \leq p_j = P(X = x_j) \leq 1$, of the random variable take the value $x_j$. It must satisfy the condition $\sum_{j = 1}^n p_j = 1$.
	*In the example, the probability distribution is computed as the probability to obtain certain number of correct answers and follows the binomial distribution.*
        
4. The **expected value** (sometimes called expectancy or expectation) of the random variable $X$, is computed with the previous ingredients as:
		$$  \mathbb{E}(X) = \sum_{j = 1}^n x_j p_j.     $$
		*In the example, the expected value is 10.*



### Warning!

The previous description applies only for a random variable with a finite amount of values. If the random variable takes a discrete but infinite amount of values, the sum becomes a series
   $$ \mathbb{E}(X) = \sum_{j = 1}^\infty x_j P(X = x_j),$$    
and if the random variable takes a continua of values (for example, if $X$ is the amount of glucose in an orange, or the amount of time necessary to run a mile), the expected value becomes an integral
    $$ \mathbb{E}(X) = \int_\mathbb{R} x P(X = x) dx.$$

### Theorem (Strong law of large numbers)
The **strong law of large numbers** (also called [Kolmogorov](https://en.wikipedia.org/wiki/Andrey_Kolmogorov "Andrey Kolmogorov")'s law) states that the sample average [converges almost surely](https://en.wikipedia.org/wiki/Almost_sure_convergence "Almost sure convergence") to the expected value

$$\overline{X}_n \rightarrow_{a.s.} \mathbb{E}(X), \quad \text{when} \quad n \rightarrow \infty.$$
In other words, the law of large numbers, tells us that if we repeat an experiment plenty of times, then the average of the values of the random variable tends to the expected value $\mathbb{E}(X)$.

*The law of large numbers tells us that if a lot of students answer randomly the test with four multiple option questions as in the example, then the average obtained score would be close to $\mathbb{E}(X) = 10$. So, the most probable outcome for a student answering at random the test is to obtain a score of  $10/40 = 2.5$.*


## Two more examples 

### Example: Throwing dice at random

When throwing a cubic six-side dice at random, we consider $X$, the random variable which gives us the amount of dots of the face "looking up". So, the possible values for $X$ are $\{1,2,3,4,5,6\}$, and all of them have the same probability $1/6$. The expected value of the random variable is thus:
    $$  \mathbb{E}(X) = 1 \times \frac{1}{6} + 2 \times \frac{1}{6} + 3 \times \frac{1}{6} + 4 \times \frac{1}{6} + 5 \times \frac{1}{6} + 6 \times \frac{1}{6} = 3.5 $$

### Example: An historic problem
Two players are betting their belongings in a game of "coin tossing", so that the first player who wins $4$ games takes all. The first player has won $2$ games and the second has won only $1$, but the encounter is interrupted by the police and they cannot continue. They decide to divide the belongings, but **what is the fair distribution for this scenario?** Using the expected value to compute the possibilities for the winning of one or the other player, it can be concluded that the fair distribution is that $68.75 \%$ of the belongings go to the first player.

### An historic note

The last example is known as the problem of division of stakes (also called [problem of points](https://en.wikipedia.org/wiki/Problem_of_points)) and it was thought for many years to be unsolvable. The solution to this problem by Blaise Pascal and Pierre de Fermat originated the concept of expected value and boosted the advance in probability and statistics.

## Bibliografía

1. **[Ra]** *R E. Walpole,  R H Myers y S L Myers*, *Probabilidad y estadística para ingenieros*, 6a. ed. PRENTICE-HALL HISPANOAMERICA, S.A. México, 1999

2. **[Poin]** [The problem of points](\url{https://probabilityandstats.wordpress.com/2016/11/06/the-problem-of-points/)



