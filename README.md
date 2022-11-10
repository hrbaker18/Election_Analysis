# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast. 
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
3. Calculate the county with the largest number of votes.
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 
5. Determine the winner of the election based on popular vote and provide their vote count and percentage of votes received.

## Resources
- Data Source: [election_results.csv](/Resources/election_results.csv)
- Software: Python 3.10.5, Visual Studio Code, 1.69.2

## Election- Audit Results:
The analysis of the election show that: 

There were 369,711 votes cast in the congressional election. 

The county voting results were:
  - Jefferson county had 10.5% votes cast and 38,855 number of votes.
  - Denver county had 82.8% votes cast and 306,055 number of votes.
  - Arapahoe county had 6.7% votes cast and 11,606 number of votes.

The county with the largest amount of votes was <b> Denver </b> with 82.8% of votes and 306,055 number of votes. 
 
The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 38,855 number of votes.
  - Diana DeGette received 73.8% of the vote and 272, 892 number of votes.
  - Raymon Anthony Doana received 3.1% of the vote and 11,606 number of votes.

The winner of the election was <b> Diana DeGette </b> with 73.8% of the vote and 272,892 number of votes. 

## Election- Audit Summary

The script written for the election audit has provided the Board of Elections with the information that <b> Diana DeGette</b> was the winner of the Congressional Election, and <b> Denver County </b> had the highest voter turnout. 

### For Future Use and Modifications

This script can be saved and modified for any election by first altering the csv file where the data will be pulled from. In this script our data is loaded from: `file_to_load = os.path.join("Resources", "election_results.csv")`
For a future election simply modify the csv file to the file containing data from the new election and begin to proceed. For example: `file_to_load = os.path.join("Resources", "election_results_22.csv")`

This script can also be modified to view additional metrics from the data, such as gender, party, or polling place. In order to view a breakdown of voters by gender a list and dictionary would need to be added : `gender = []`, `gender_votes = {}`

Then gender would need to be extracted from the dataset `gender_name = row[x]`

Next an if statement would need to be written to ensure that the genders are added to the list `if gender_name not in gender:`
                                                                                                                                                                                                                                                                        `gender.append(gender_name)`

Finally, the number of votes according to gender would need to be counted `gender_votes[gender_name] +=1`, `gender = gender_votes.get(gender_name)`, `gender_percentage = float(gender) / float(total_votes) * 100`

#### Closing Notes 

There are endless options to modify this script for future elections, and for viewing breakdowns of different data that would enhance the scope of the election audit. This script is a great template for an election audit, in that it can be modified and data can be looked at in depth. As it saves and writes to a text file, the results can be read and interpreted easily by anyone. 
