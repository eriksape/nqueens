# NQueen Problem

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example, following are a solutions for 4 Queen problem.

![4x4_solution_1](https://github.com/eriksape/nqueens/blob/master/.github/4x4_soluion_1.png?raw=true)
![4x4_solution_2](https://github.com/eriksape/nqueens/blob/master/.github/4x4_solution_2.png?raw=true)

These are known solutions for the NQueen problem

![known_solutions](https://github.com/eriksape/nqueens/blob/master/.github/known_solutions.png?raw=true)

We need to generate and store most solutions in < 10 minutes


## Backtraking:

Generating from 8x8 to 13x13 N size we have the next results:
![backtracking_8x8_to_13x13](https://github.com/eriksape/nqueens/blob/master/.github/backtracking_8x8_to_13x13.png?raw=true)


## Bitwise:

Generating from 8x8 to 15x15 N size we have the next results:
![bitwise_8x8_to_15x15.png](https://github.com/eriksape/nqueens/blob/master/.github/bitwise_8x8_to_15x15.png?raw=true)

The problem here is that we have 2,279,184 solutions that we want to store in a database. With some optimizations with SQLAlchemy we can have the next results:

![bitwise_8x8_to_15x15_to_database](https://github.com/eriksape/nqueens/blob/master/.github/bitwise_8x8_to_15x15_to_database.png?raw=true)

We can see the count per record in the datase with the next query:

![stored_solutions](https://github.com/eriksape/nqueens/blob/master/.github/stored_solutions.png?raw=true)

We can see there are not solutions listed for dimension 2x2 or 3x3, that's because are not known solutions as we can see on the follow query:

![query_cases](https://github.com/eriksape/nqueens/blob/master/.github/query_cases.png?raw=true)

## References

- Martin Richards https://www.cl.cam.ac.uk/~mr10/backtrk.pdf
- Andrés Muñoz https://www.youtube.com/watch?v=XQYGwKiqV3Y

## Extra

We can see the stored solutions in http://localhost:1001/

![web_stored_solutions](https://github.com/eriksape/nqueens/blob/master/.github/web__stored_solutions.png?raw=true)

To run the project we need Docker installed in your system.
`docker-compose up`

To create the database run the script
`docker-compose run nqueens flask initdb`

To run the tests we have some scripts:

 - This is to check from 1x1 to 12x12 `docker-compose run nqueens python -m pytest app/tests/tests.py` helped me with some refactors
 - This is to run from 8x8 to 15x15 `docker-compose run nqueens python -m pytest app/tests/tests_solutions_not_saving.py`
 - This is to run from 8x8 to 15x15 and save it into database `docker-compose run nqueens python -m pytest app/tests/tests_solutions.py`
 - This is to run from 8x8 to 15x15 from database `docker-compose run nqueens python -m pytest app/tests/tests_solutions_stored.py`
 
**Tests are automated thanks to github actions** ♥️

[Here](https://github.com/eriksape/nqueens/actions) are automated test runned in this project
