import numpy as np
import Parameters as pm
import matplotlib
import matplotlib.pyplot as plt

#This file contains all of the functions necessary for running tournament simulations. The key function here is "simulatio(iterations)"

#define class team that will basically initialize hold all the static parameters belonging to some team
class team:
    def __init__(self, teamName):
        """Constructor for Team Class"""
        
        for i in range (4):
            for j in range(16):
                if (teamName == pm.R1teams[i, j]):
                    self.regional, self.position = i, j
                    break
        
        self.totWin = pm.totWin[self.regional][self.position]
        self.awayWin = pm.awayWin[self.regional][self.position]
        self.recency = pm.recency[self.regional][self.position]
        self.seed = pm.seed[self.position]
        self.name = pm.R1teams[self.regional][self.position]
        
        # Define Parameter Weights
        weightTotWin = 1/3
        weightAwayWin = 1/2
        weightRecency = 1/6
    
        self.score = weightTotWin*self.totWin + weightAwayWin*self.awayWin + weightRecency*self.recency


#Create dictionary that will have all the terms as keys and all the definitions as that teams object and index in the main R1teams array
teamDict = {}
for i in range(4):     # loop over regionals
    for j in range(16):    # loop over positions
        teamDict[pm.R1teams[i, j]] = np.array([team(pm.R1teams[i, j]), i, j])
        
#function for the rounds up to the semi finals (Final Four)
def regionalRound(round, Rteams, nextTeams):
    for i in range(4):     # loop over regionals
        for j in range(int(8/2**(round-1))):    # loop over positions
            a = teamDict[Rteams[i, 2*j]][0]
            b = teamDict[Rteams[i, 2*j+1]][0]
            sa = pm.seedMatch[a.seed - 1][b.seed - 1]  #seed advantage for a
            sb = pm.seedMatch[b.seed - 1][a.seed - 1]  #seed advantage for b
            if (sa == "na" or sb == "na" or round > 1):  #if no seed infrmation, ignore it
                #Pa = a.score*(1-b.score) / (a.score*(1-b.score) + b.score*(1-a.score))
                Pa = a.score/(a.score+b.score)
            else:
                #Pa = a.score*(1-b.score)*sa / (a.score*(1-b.score)*sa + b.score*(1-a.score)*sb)
                Pa = a.score*sa/(a.score*sa+b.score*(1-sa))
            chance = np.random.random()
            if (Pa > chance):
                nextTeams[i, j] = a.name
            else :
                nextTeams[i, j] = b.name
    return nextTeams


#Function for the semifinal and fial
def advancedRounds(round, Rteams, nextTeams):
    for i in range(8-round):
        if (round == 6):
            a = teamDict[Rteams[2*i, 0]][0]
            b = teamDict[Rteams[2*i+1, 0]][0]
        elif (round == 7):
            a = teamDict[Rteams[2*i]][0]
            b = teamDict[Rteams[2*i+1]][0]
        Pa = a.score / (a.score + b.score)
        chance = np.random.random()
        if (Pa > chance):
            nextTeams[i] = a.name
        else :
            nextTeams[i] = b.name
    return nextTeams
            

def count(array, value):
    """Counts number of times a value appears in an array"""
    count = 0
    for i in range (len(array)):
        if (array[i] == value):
            count += 1
    return count
        
            

def setupDistribution(tournamentsWon1):
    """Sets up arrays for the probability density distribution of times won in the tournament"""
    timesWon = np.sort(np.unique(tournamentsWon1))
    numberTimesWon = np.zeros_like(timesWon)
    for i in range (len(timesWon)):
        numberTimesWon[i] = count(tournamentsWon1, timesWon[i])
    return timesWon, numberTimesWon

#main function of the program which depends on the others. Simulates as many iterations of tournaments as specified
def simulation(iterations):
    # set up arrays for storing teams
    R2teams = np.empty((4, 8), dtype=object)
    R3teams = np.empty((4, 4), dtype=object)
    R4teams = np.empty((4, 2), dtype=object)
    R5teams = np.empty((4, 1), dtype=object)
    R6teams = np.empty(2, dtype=object)
    R7teams = np.empty(1, dtype=object)
    
    #create array that store the number of tournaments a team has won
    tournamentsWon = np.zeros((4, 16))
    
    
    # set up array that will save the amount of times a complete round has been guessed correctly with respect to iteration #
    R2array = np.zeros(iterations)
    R3array = np.zeros(iterations)
    R4array = np.zeros(iterations)
    R5array = np.zeros(iterations)
    R6array = np.zeros(iterations)
    R7array = np.zeros(iterations)
    #creates an array for iterations ... will be useful for plot
    iterationsArray = np.arange(1, iterations+1, 1)
    
    # initialize stat variables
    R7times = 0
    R6times = 0
    R5times = 0
    R4times = 0
    R3times = 0
    R2times = 0
    
    #Initialize Martinez-Katterman Benchmark
    benchmarkSum = 0
    
    for iteration in range(1, iterations+1):   # simulate tournaments
        R2teams = regionalRound(1, pm.R1teams, R2teams)
        R3teams = regionalRound(2, R2teams, R3teams)
        R4teams = regionalRound(3, R3teams, R4teams)
        R5teams = regionalRound(4, R4teams, R5teams)
        R6teams = advancedRounds(6, R5teams, R6teams)
        R7teams = advancedRounds(7, R6teams, R7teams)
        
        # count the number of times all of the winners of a roud are guessed correctly
        if (np.all(np.equal(R2teams, pm.winnersR1))):
            R2times += 1
            
        if (np.all(np.equal(R3teams, pm.winnersR2))):
            R3times += 1
            
        if (np.all(np.equal(R4teams, pm.winnersR3))):
            R4times += 1
            
        if (np.all(np.equal(R5teams, pm.winnersR4))):
            R5times += 1
            
        if (np.all(np.equal(R6teams, pm.winnersR5))):
            R6times += 1
            
        if (np.all(np.equal(R7teams, pm.winnersR6))):
            R7times += 1
        
        # Count the number of games that were guessed correctly
        
        # Loop over round 2 games
        for i in range (4):
            for j in range (8):
                if (pm.winnersR1[i, j] == R2teams[i, j]):
                    benchmarkSum += 1
        # Lo0p over round 3 games
        for i in range (4):
            for j in range (4):
                if (pm.winnersR2[i, j] == R3teams[i, j]):
                    benchmarkSum += 1
        # Loop over round 4 games
        for i in range (4):
            for j in range (2):
                if (pm.winnersR3[i, j] == R4teams[i, j]):
                    benchmarkSum += 1
        # Loop over round 5 games
        for i in range (4):
            if (pm.winnersR4[i, 0] == R5teams[i, 0]):
                benchmarkSum += 1
        # Loop over round 6 games
        for i in range (2):
            if (pm.winnersR5[i] == R6teams[i]):
                benchmarkSum += 1
        # Loop over the round 7 game
        if (pm.winnersR6[0] == R7teams[0]):
            benchmarkSum += 1
        
        #set the probability that an iteration has had a complete guess of a round to an array
        R2array[iteration-1] = R2times/iteration
        R3array[iteration-1] = R3times/iteration
        R4array[iteration-1] = R4times/iteration
        R5array[iteration-1] = R5times/iteration
        R6array[iteration-1] = R6times/iteration
        R7array[iteration-1] = R7times/iteration
        
        #Add one to winners tournament count
        index1 = teamDict[R7teams[0]][1]
        index2 = teamDict[R7teams[0]][2]
        tournamentsWon[index1, index2] += 1
        

    tournWonOneDim = np.append(np.append(np.append(tournamentsWon[0,:], tournamentsWon[1,:]), tournamentsWon[2,:]), \
                                    tournamentsWon[3,:])
    
    #set up stuff for distribution of # of times won in tournament
    timesWon, numberTimesWon = setupDistribution(tournWonOneDim)
    
    #Normalize Martinez-Katterman Benchmark
    MKBenchmark = benchmarkSum/(63*iterations)
    
    #set up stuff for bar graph
    topten = np.zeros(10)
    topten = tournWonOneDim.argsort()[-10:] #top ten locations
    toptenValues = np.zeros(10)
    topTenNames = np.empty(10, dtype=object)
    toptenValues[:] = tournWonOneDim[topten[:]]
    topTenNames[:] = pm.R1teamsOneDim[topten[:]]
    
    #plot bargraph
    N = np.arange(10)
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(211)
    rects1 = ax.bar(N, toptenValues, 0.7, color='black')
    ax.set_ylabel('Tournaments Won')
    ax.set_title('Top Ten Winning Teams')
    ax.set_xticks(N+0.3)
    ax.set_xticklabels((topTenNames[0], topTenNames[1], topTenNames[2], topTenNames[3], topTenNames[4], topTenNames[5], topTenNames[6], \
                        topTenNames[7], topTenNames[8], topTenNames[9]))
    plt.savefig("Bar Graph")
    plt.show()
    
    #plot distribution
    
    ax1 = plt.subplot(111)
    ax1.plot(timesWon, numberTimesWon, 'ro')
    ax1.set_ylabel('Number of Teams')
    ax1.set_xlabel('Times tournament was won')
    ax.set_title('Probability distribution for tournaments won')
    #plt.xlim(0, 100)
    plt.ylim(0, 9)
    plt.savefig("Distribution")
    plt.show()
    
    
    #graph iterations vs odds
    ax2 = plt.subplot(111)
    ax2.plot(iterationsArray, R2array)
    ax2.set_ylabel('Odds')
    ax2.set_xlabel('Iterations')
    ax2.set_title('Odds of guessing all of Round 2 correctly vs. # of Iterations')
    plt.savefig("Round 2")
    plt.show()
    
    ax2 = plt.subplot(111)
    ax2.plot(iterationsArray, R3array)
    ax2.set_ylabel('Odds')
    ax2.set_xlabel('Iterations')
    ax2.set_title('Odds of guessing all of Round 3 correctly vs. # of Iterations')
    plt.savefig("Round 3")
    plt.show()
    
    ax2 = plt.subplot(111)
    ax2.plot(iterationsArray, R4array)
    ax2.set_ylabel('Odds')
    ax2.set_xlabel('Iterations')
    ax2.set_title('Odds of guessing all of Round 4 correctly vs. # of Iterations')
    plt.savefig("Round 4")
    plt.show()
    
    ax2 = plt.subplot(111)
    ax2.plot(iterationsArray, R5array)
    ax2.set_ylabel('Odds')
    ax2.set_xlabel('Iterations')
    ax2.set_title('Odds of guessing all of Round 5 correctly vs. # of Iterations')
    plt.savefig("Round 5")
    plt.show()
    
    ax2 = plt.subplot(111)
    ax2.plot(iterationsArray, R6array)
    ax2.set_ylabel('Odds')
    ax2.set_xlabel('Iterations')
    ax2.set_title('Odds of guessing all of Round 6 correctly vs. # of Iterations')
    plt.savefig("Round 6")
    plt.show()
    
    ax2 = plt.subplot(111)
    ax2.plot(iterationsArray, R7array)
    ax2.set_ylabel('Odds')
    ax2.set_xlabel('Iterations')
    ax2.set_title('Odds of guessing all of Round 7 correctly vs. # of Iterations')
    plt.savefig("Round 7")
    plt.show()
    
    print(tournamentsWon)
    
    return numberTimesWon, timesWon, tournamentsWon, MKBenchmark