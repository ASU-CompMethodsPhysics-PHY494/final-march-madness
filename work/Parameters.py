import numpy as np

#This file contains the arrays for the parameters

R1teams = np.zeros((4, 16))
totWin = np.zeros_like(R1teams)
recency = np.zeros_like(R1teams)
awayWin = np.zeros_like(R1teams)
seed = np.zeros(16)

#order of how teams are ordered in terms of their seed qualification
seed = np.array([1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15])

R1teams = np.array([["Kansas", "Austin Peay", "Colorado", "Connecticut", "Maryland", "South Dakota State", "California", "Hawaii", "Arizona", "Wichita State", "Miami", "Buffalo", "Iowa", "Temple", "Villanova", "UNC Asheville"],
                ["Oregon", "Holy Cross", "Saint Joseph's", "Cincinnatti", "Baylor", "Yale", "Duke", "UNC Wilmington", "Texas", "Northern Iowa", "Texan A&M", "Green Bay", "Oregon State", "VCU", "Oklahoma", "Cal State Bakersfield"],
                ["North Carolina", "Florida Gulf Coast", "USC", "Providence", "Indiana", "Chattanooga", "Kentucky", "Stony Brook", "Notre Dame", "Michigan", "West Virginia", "Stephen F Austin", "Wisconsin", "Pittsburgh", "Xavier", "Weber State"], 
                ["Virginia", "Hampton", "Texas Tech", "Butler", "Purdue", "Ankansas-Little Rock", "Iowa State", "Iona", "Seton Hall", "Gonzaga", "Utah", "Fresno State", "Dayton", "Syracuse", "Michigan State", "Middle Tennessee"]])

#same as previous array, but one dimensional for getting the 10 highest winning teams
R1teamsOneDim = np.array(["Kansas", "Austin Peay", "Colorado", "Connecticut", "Maryland", "South Dakota State", "California", "Hawaii", "Arizona", "Wichita State", "Miami", "Buffalo", "Iowa", "Temple", "Villanova", "UNC Asheville",
                "Oregon", "Holy Cross", "Saint Joseph's", "Cincinnatti", "Baylor", "Yale", "Duke", "UNC Wilmington", "Texas", "Northern Iowa", "Texan A&M", "Green Bay", "Oregon State", "VCU", "Oklahoma", "Cal State Bakersfield",
                "North Carolina", "Florida Gulf Coast", "USC", "Providence", "Indiana", "Chattanooga", "Kentucky", "Stony Brook", "Notre Dame", "Michigan", "West Virginia", "Stephen F Austin", "Wisconsin", "Pittsburgh", "Xavier", "Weber State", 
                "Virginia", "Hampton", "Texas Tech", "Butler", "Purdue", "Ankansas-Little Rock", "Iowa State", "Iona", "Seton Hall", "Gonzaga", "Utah", "Fresno State", "Dayton", "Syracuse", "Michigan State", "Middle Tennessee"])

winnersR1 = np.array([["Kansas", "Connecticut", "Maryland", "Hawaii", "Wichita St", "Miami", "Iowa", "Villanova"], 
                    ["Oregon", "Saint Joseph's", "Yale", "Duke", "Northern Iowa", "Texas A&M", "VCU", "Oklahoma"], 
                    ["North Carolina", "Providence", "Indiana", "Kentucky", "Notre Dame", "Stephen F Austin", "Wisconsin", "Xavier"], 
                    ["Virginia", "Butler", "Arkansas-Little Rock", "Iowa St", "Gonzaga", "Utah", "Syracuse", "Middle Tennessee"]]) 

winnersR2 = np.array([["Kansas", "Maryland", "Miami", "Villanova"], 
                      ["Oregon", "Duke", "Texas A&M", "Oklahoma"], 
                      ["North Carolina", "Indiana", "Notre Dame", "Wisconsin"], 
                      ["Virginia", "Iowa St", "Gonzaga", "Syracuse"]])


winnersR3 = np.array([["Kansas", "Villanova"], 
                      ["Oregon", "Oklahoma"], 
                      ["North Carolina", "Notre Dame"], 
                      ["Virginia","Syracuse"]])

winnersR4 = np.array([["Villanova"], ["Oklahoma"], ["North Carolina"], ["Syracuse"]])

winnersR5 = np.array(["Villanova", "North Carolina"])

winnersR6 = np.array(["Villanova"])


#total wins in the seson before competition
totWin = np.array([[30/34, 18/35, 22/33, 24/34, 25/33, 26/33, 23/33, 27/32, 25/33, 24/32, 25/32, 20/34, 21/31, 21/32, 29/34, 22/33],
            [28/34, 14/33, 27/34, 22/32, 22/33, 22/28, 23/33, 25/32, 20/32, 22/34, 26/34, 23/35, 19/31, 24/34, 25/32, 24/32],
            [28/34, 20/33, 21/33, 23/33, 25/32, 29/34, 26/34, 26/32, 21/32, 22/34, 26/34, 27/32, 20/32, 21/32, 27/32, 26/34], 
            [26/33, 21/31, 19/31, 21/31, 26/34, 29/33, 21/32, 22/32, 25/33, 26/33, 26/34, 25/34, 25/32, 19/32, 29/34, 24/33]])

#The team's results in the past 10 games before copetition
recency = np.array([[10/10, 8/10, 5/10, 7/10, 5/10, 8/10, 8/10, 8/10, 7/10, 7/10, 7/10, 6/10, 4/10, 7/10, 8/10, 7/10],
            [8/10, 5/10, 7/10, 6/10, 5/10, 9/10, 6/10, 8/10, 5/10, 9/10, 8/10, 8/10, 6/10, 7/10, 6/10, 9/10],
            [8/10, 7/10, 3/10, 5/10, 7/10, 8/10, 8/10, 8/10, 6/10, 5/10, 7/10, 10/10, 7/10, 4/10, 7/10, 9/10], 
            [7/10, 8/10, 6/10, 7/10, 7/10, 8/10, 5/10, 9/10, 8/10, 8/10, 9/10, 9/10, 6/10, 5/10, 9/10, 7/10]])

#total away wins in the season before competition
awayWin = np.array([[13/17, 11/21, 6/16, 10/17, 9/16, 13/20, 5/15, 10/12, 8/15, 10/17, 10/16, 10/19, 8/16, 10/18, 14/18, 11/19],
            [10/16, 6/19, 15/18, 8/15, 8/14, 10/16, 8/15, 13/18, 6/15, 11/20, 9/16, 12/21, 7/16, 9/17, 11/17, 10/17],
            [13/18, 4/13, 5/15, 10/16, 8/15, 16/20, 9/17, 11/16, 7/16, 9/17, 13/19, 13/18, 7/14, 6/13, 12/16, 18/20], 
            [11/18, 12/20, 5/14, 8/15, 9/16, 15/19, 7/17, 11/19, 12/17, 15/18, 10/17, 9/16, 11/15, 6/15, 15/18, 13/19]])

# Historical outcomes of seed matchups from NCAA March Madness tournaments from 1985-2015 (all tournaments since 64 teams started competing)
# Matrix setup as shown below with numbers in cells representing the outcome of vertical seed's chance of beating horizontal seed
# Cells with "na" values are seeds that have never faced each other in the history of the tournament (since 1985) 
# seed 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16
#   1
#   2
#   3
#   4
#   5
#   6
#   7
#   8
#   9
#  10
#  11
#  12
#  13
#  14
#  15
#  16

seedMatch = ([[18/36, 33/59, 17/28, 39/56, 34/41, 8/12, 4/5, 52/65, 57/62, 4/4, 3/6, 19/19, 4/4, "na", "na", 124/124],
              [26/59, 3/6, 25/45, 3/8, 1/4, 23/29, 55/72, 3/8, 0/1, 26/45, 13/14, 1/1, "na", "na", 117/124, "na"],
              [11/28, 17/45, 1/2, 4/7, 2/3, 38/66, 7/12, 1/1, 1/1, 9/13, 26/39, "na", "na", 104/124, 1/1, "na"],
              [17/56, 5/8, 3/7, 1/2, 36/66, 2/4, 2/4, 3/8, 2/2, 2/2, "na", 21/33, 99/124, "na", "na", "na"],
              [7/41, 3/4, 1/3, 30/66, 1/2, 1/1, "na", 1/3, 1/2, 1/1, "na", 80/124, 11/14, "na", "na", "na"],
              [4/12, 6/29, 28/66, 2/4, 0/1, 0.5, 3/6, 0/1, "na", 4/6, 81/124, "na", "na", 12/14, "na", "na"],
              [1/5, 17/72, 5/12, 2/4, "na", 3/6, 0.5, 1/2, "na", 75/124, 0/3, "na", "na", 1/1, 2/3, "na"],
              [13/65, 5/8, 0/1, 5/8, 2/3, 1/1, 1/2, 0.5, 63/124, "na", 1/1, 0/1, 1/1, "na", "na", "na"],
              [5/62, 1/1, 0/1, 0/2, 1/2, "na", "na", 61/124, 0.5, "na", "na", "na", 1/1, "na", "na", "na"],
              [0/4, 19/45, 4/13, 0/2, 0/1, 2/6, 49/124, "na", "na", 0.5, 0/2, "na", "na", 1/1, 0/4, "na"],
              [3/6, 1/14, 13/39, "na", "na", 43/124, 3/3, 0/1, "na", 2/2, 0.5, "na", "na", 5/5, "na", "na"],
              [0/19, 0/1, "na", 12/33, 44/124, "na", "na", 1/1, "na", "na", "na", 0.5, 8/11, "na", "na", "na"],
              [0/4, "na", "na", 25/124, 3/14, "na", "na", 0/1, 0/1, "na", "na", 3/11, 0.5, "na", "na", "na"],
              ["na", "na", 20/124, "na", "na", 2/14, 0/1, "na", "na", 0/1, 0/5, "na", "na", 0.5, "na", "na"],
              ["na", 7/124, 0/1, "na", "na", "na", 1/3, "na", "na", 0/4, "na", "na", "na", "na", 0.5, "na"],
              [0/124, "na", "na", "na", "na", "na", "na", "na", "na", "na", "na", "na", "na", "na", "na", 0.5]])