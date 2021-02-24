Petstore api

Welcome to the Pet House. It is a RESTful api built using FLASK and SQLITE3

structure of pets database:
pets table
###pet_name TEXT PRIMARY KEY,
### pet_type TEXT NOT NULL,
###owner TEXT NOT NULL

json to be sent for POST request:
{
    "pet_name": "oreo",
    "pet_type": "mouse",
    "owner": "abhuday"
}


possible routes:
1.'/allpets' : gets all the pets available in the petstore
[GET]sample call: localhost:5000/allpets

2.'/pet' : takes an arguement 'id' which will be the petname and gets the details of the pet
[GET]sample call: localhost:5000/pet?id=rocky

3.'/newpet': accepts json and adds the new pet to the database
[POST]sample call: localhost:5000/newpet

4.'/updatepet': accepts json with pet_name(primary key) and other details changed so that they can be updated, make sure to enter all details even if unchanged
[POST]sample call: localhost:5000/updatepet

5.'/delpet': accepts 'id' which is the petname, delete the pet from the database (say bye, cause that lucky guy is going home)
[DELETE]sample call: localhost:5000/delpet?id=rocky

6.'/mypets': accepts 'id' which will be the owner name, returns all the pets owner has
[GET]sample call: localhost:5000/mypets?id=abhi

7.'/whosepet': accepts 'id' which will be the petname, find who is the owner of a pet.
[GET]sample call: localhost:5000/whosepet?id=rocky

8.'/owner': returns all the owners registered to the pet store.
[GET]sample call: localhost:5000/owner

9.'/hello': all animals say hello
[GET]sample call: localhost:5000/hello