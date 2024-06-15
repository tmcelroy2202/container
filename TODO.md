# TODO

* fix known bugs
  - things are wrong with the remove thing for libdb
    - index out of bounds every once in a while 
    - whole database deleted on failure, and it fails often.
    - led lights not lighting up on removal for libdb, which is weird. 
  - libdb as a whole is untested / im not sure if it works really at all
* git commit on addition to database / other backup solution?
  - see if this could get me time added on items, as git would track that. im thinking just grepping through the git diff for first + containing the item name. would also work for time removed. I could also implement search history maybe. 
* change bridge file name from balls.txt to something more professional.
* write tests for
  - libdb ( DONE ) 
  - libdbcc
  - ledcontrol ( Via checking if payloads are correct, cant check if wled works )
  - bridgeutils 
  - main ( by writing to balls.txt examples, and checking db.txt after. maybe add debug logs too. )
* write documentation
  - libdb documentation for each function
  - libdbcc documentation for each function
  - installation instructions and setup with YOUR container.
* environment setup / first time setup script
* research other database implementations
* nicer ui for manual interaction with database, for when voice control is insufficient
* selfhosted voice control
  - all i really need is local hotword detection 