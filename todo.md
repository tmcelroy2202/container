# TODO

* fix known bugs
  - whole database deleted on failure of any function that interacts with the database
* git commit on addition to database / other backup solution?
  - see if this could get me time added on items, as git would track that. im thinking just grepping through the git diff for first + containing the item name. would also work for time removed. I could also implement search history maybe. 
* write tests for
  - libdb ( DONE ) 
  - libdbcc (DONE)
  - ledcontrol (  DONE )
  - bridgeutils 
  - main ( by writing to inputs.txt examples, and checking db.txt after. maybe add debug logs too. )
* write documentation
  - libdb documentation for each function
  - libdbcc documentation for each function
  - installation instructions and setup with YOUR container.
* environment setup / first time setup script
  - things to be included:
    - wled ip ( done ) 
    - number of containers ( appliances ) 
    - type of container for each container specified ( highlight or grid ) ( done but only for one container ) 
    - wled segments to skip ( done ) 
    - git setup maybe    
* research other database implementations
* move away from just having db.txt and cc.txt, but instead have numbered versions of each one, which can be passed to any libdb or libdbcc functions. e.g. addpos(2,"power adapter",4) adds a power adapter to the 3rd slot ( 0, 1, 2 ) of the 5th container ( 0, 1, 2, 3 4, 5 )
  - this would allow for multiple of each container system ( e.g. 5 highlight containers )
* nicer ui for manual interaction with database, for when voice control is insufficient
* nice demo video 
* selfhosted voice control
  - all i really need is local hotword detection 
