# Election_Analysis

## Project Overview
A Colorado Board of Elections employee havs given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.47.3

## Summary 
The analysis of the election shows that:
- There were "x" votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes
    - Diana DeGette received 73.8% of the vote and 272,892 total votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes
 - The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 total votes
    
## Challenge Overview

### Overview of Election Audit
The purpose of the election audit was to write a python script that could take a CSV file of raw electoral data and convert it into a user friendly report that tells us who won an election, how many votes were cast, and the percentage breakdown of votes for candidates/counties.  

### Election Audit Results
-	369,711 total votes were cast across three counties

-	County Results:
    - Jefferson County: 38,855 votes cast. 10.51% of the total vote. 
    - Denver County: 306,055 votes cast. 82.78% of the total vote. 
    - Arapahoe County: 24,801 votes cast. 6.71% of the total vote. 
    
-	Largest County Turnout: Denver

-	Candidate Results:
    - Charles Casper Stockham: 23.0% of the vote, 85,213 total votes
    - Diana DeGette: 73.8% of the vote, 272,892 total votes
    - Raymon Anthony Doane: 3.1% of the vote,  11,606 total votes
        
-	Winning Candidate: Diana DeGette with 73.8% of the vote (272,892 total votes)

 
 ## Challenge Summary
 This script is built so that it can be easily applied to other elections across the state, nation, or world. This is because the lists and dictionaries the script uses to write and perform calculations are dynamically built as the code executes through a dataset.  
One modification that may be necessary when running this script across other elections is to edit the indexes in which the script recognizes candidate name and county name. Depending on how the data is organized and how much information is pulled the candidate and county names could be in different columns of a CSV file. The code as is would not recognize this and would assign whatever data is in indexes 1 & 2 as unique candidates or counties. To mitigate this the script could be edited to assign the county and candidate index based on a search of where those category names show up in the header of the our data. Sample code below:


![alt text](https://github.com/cclark1016/Election_Analysis/blob/master/Resources/Resources/Election_code_1.png)

Another modification could be made if the winner of an election is not determined by a simple majority. For example if a candidate needed to secure the most votes AND have at least 50% of the total electorate vote for them we would need to modify the subset of code that determines a winning candidate. 
In this case the initial winning candidate variable could be changed to the below:

![alt text](https://github.com/cclark1016/Election_Analysis/blob/master/Resources/Resources/Election_code_2.png)

And a condition added to the if statement to not execute if a candidates vote percentage is less than 50%:

![alt_text](https://github.com/cclark1016/Election_Analysis/blob/master/Resources/Resources/Election_code_3.png)
