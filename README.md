# dream11
design a low level dream11 backend server

FCL (Modified version of Dream 11)    

RULES:    

There are 11 defined teams in this league, and each team has 11 players.  
IND [1 - 11], PAK[12 - 22 ], SLC[23 - 33], SA[34 - 44], WI [45 - 55], BAN [56 - 66], AUS [67 - 77], ENG[78 - 88], NZ [89 - 99], AFG [100 - 110], ZWE[111 - 121]    

Note: Numbers mentioned above in the [] are the names of the players for simplicity. Where the first 6 numbers are batsmen and the next 5 numbers are bowlers.     	 	

A game will be played between two teams. 	 	 	
Multiple games can happen parallelly. 	 	 	
Each team has 6 batsmen and 5 bowlers 	 	 	
Users can create their own team for game mixing players from both teams, provided they should have 6 batsmen and 5 bowlers. 	 	 	
Each ball bowled will result in one of the outcomes - 1,2,4,6 run or Batsman getting out (represented as -1). 	 	 	
These are the following points assigned to batsmen or the bowler based on the outcome,  	 		 		
1 run - Batsmen : 0.5 point , Bowler : 0 point 		 		 		
2 runs - Batsmen : 1 point , Bowler : (- 0.5) point 		 		 		
4 runs - Batsmen : 2 points, Bowler : (-1) point 		 		 		
6 runs - Batsmen : 3 points, Bowler : (-2 ) points 		 		 		
Batsmen getting out - Batsmen: (- 2) points, Bowler: 4 points 		 	 	 	 	

A game can be ended at any point in time. In that case, the user with the highest points wins. 	 	 	

You don’t need to maintain any of the cricket rules in your code. 	 	 	

Based on the above rules, you should implement the following Signature, 	      

Create a game    
public int createGame (String team1, String team2) {}    
Explanation:  Given two team names, create a game and return a unique ID for this game.    

Create a team for a user (in a game)    
public void createTeamForUser(Int gameId, ListInteger players, String userName)    
Explanation:  Given a gameId and List of players, a team should be created for the user      

Start Game  public void startGame(int gameId)    
Explanation:  Given a gameId, start the game. Hint - Certain functions will work only when the game is running.      

Play Game    public void play(Int gameId, Int batsmen, Int bowler, int outcome)    
Explanation:  An external system will call you with the outcome of each ball. Given a gameId Batsmen id, bowler id, and outcome, increment/decrement points accordingly for users associated with this game. To keep it simple, We just follow what the external system sends us, and we don’t need to maintain the cricket rules in our logic.      

Get top k user for a game    
public ListString getTopKUsers(int gameId, int K)    
Explanation:  Given a gameId, get the top k user who has maximum points so far. Top K users will be displayed in the app, and people keep refreshing now and then to see the top k users      

End a game    
public String endGame(int gameId)    
Explanation:  Given a gameId, end the game and return the user who is the winner with maximum points. Additional - In case of a tie, use your own strategy for tie-breaking.    

Instructions - 
You will be evaluated on 4 core things    
- Approach towards the problem    
- - Code Structure   
- - Correctness    
- - Race Conditions      
- 
- - Please go through the entire document and ask if you have any doubts  
- - Use in-memory data structure but try to structure the code so that you can swap in-memory data-structures with a database easily.  
- - The code will be checked manually by the interviewer towards the end of interview  
- - Focus on correctness and code structure first. Code should be workable towards the interview.  
- - Think of this system running in a production setting. Try to find which functions will be called more often than others and then structure your code accordingly.
