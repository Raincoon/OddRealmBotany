# Odd Realm Botany Index  

\---  
Feedback may be given in both finnish and english  
\---  

This project will deal with categorising grow times, biome occurrences, etc. of various crops (and trees) in the colony-building game Odd Realm.  
In the game, plants and trees can be sown and cultivated from seed and may also grow naturally depending on season and chosen biome. Some tree varieties may also yield fruit.  
<sub>Tracking fruit<->tree relations specifically is not planned, as such occurrences are few and fairly obvious (apples from apple trees, coconuts from palm trees); similar functionality can be achieved with matching tags.</sub>


Current major features  
 - login with username+password for plant tracking  
 - add, edit and/or remove entries for plants and tags  
 - find botanical items by tag  
 
[Link to the Heroku app](https://oddrealmbotany.herokuapp.com/)  
Short instructions for Heroku:  
You may either log in with username: 'user' password: 'password' or create your own account by clicking on the 'Sign up' link.  
(If you do create your own test user, keep in mind that while passwords are stored as salted hashes, usernames are stored in plaintext.)  
[User guide](./documentation/user_guide.md)  
[How to install the project locally](./documentation/installguide.md)  
[Link to the user stories file](./documentation/userstories.md)



Database relationship diagram:  
![current database structure](./documentation/DBdiagram.png "Database diagram image")  
